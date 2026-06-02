# Propact 🚀 Protocol Pact via Markdown



## Contents

- [Metadata](#metadata)
- [Architecture](#architecture)
- [Interfaces](#interfaces)
- [Workflows](#workflows)
- [Configuration](#configuration)
- [Deployment](#deployment)
- [Environment Variables (`.env.example`)](#environment-variables-envexample)
- [Release Management (`goal.yaml`)](#release-management-goalyaml)
- [Makefile Targets](#makefile-targets)
- [Code Analysis](#code-analysis)
- [Call Graph](#call-graph)
- [Test Contracts](#test-contracts)
- [Intent](#intent)

## Metadata

- **name**: `propact`
- **version**: `0.0.0`
- **ecosystem**: SUMD + DOQL + testql + taskfile
- **generated_from**: pyproject.toml, Makefile, testql(2), app.doql.less, goal.yaml, .env.example, project/(3 analysis files)

## Architecture

```
SUMD (description) → DOQL/source (code) → taskfile (automation) → testql (verification)
```

### DOQL Application Declaration (`app.doql.less`)

```less markpact:doql path=app.doql.less
// LESS format — define @variables here as needed

app {
  name: propact;
  version: 0.0.0;
}

workflow[name="install"] {
  trigger: manual;
  step-1: run cmd=poetry install;
}

workflow[name="dev"] {
  trigger: manual;
  step-1: run cmd=poetry install --with dev;
}

workflow[name="test"] {
  trigger: manual;
  step-1: run cmd=poetry run pytest -vv;
}

workflow[name="test-cov"] {
  trigger: manual;
  step-1: run cmd=poetry run pytest --cov=propact --cov-report=html --cov-report=term;
}

workflow[name="lint"] {
  trigger: manual;
  step-1: run cmd=poetry run ruff check src/ tests/;
  step-2: run cmd=poetry run ruff format src/ tests/;
}

workflow[name="type-check"] {
  trigger: manual;
  step-1: run cmd=poetry run mypy src/;
}

workflow[name="check"] {
  trigger: manual;
  step-1: depend target=lint;
  step-2: depend target=type-check;
  step-3: depend target=test;
}

workflow[name="clean"] {
  trigger: manual;
  step-1: run cmd=rm -rf dist/;
  step-2: run cmd=rm -rf *.egg-info/;
  step-3: run cmd=rm -rf .pytest_cache/;
  step-4: run cmd=rm -rf .coverage;
  step-5: run cmd=rm -rf htmlcov/;
  step-6: run cmd=find . -type d -name __pycache__ -exec rm -rf {} +;
  step-7: run cmd=find . -type f -name "*.pyc" -delete;
}

workflow[name="build"] {
  trigger: manual;
  step-1: run cmd=poetry build;
}

workflow[name="publish"] {
  trigger: manual;
  step-1: run cmd=poetry publish;
}

workflow[name="publish-test"] {
  trigger: manual;
  step-1: run cmd=poetry publish --repository testpypi;
}

workflow[name="docs"] {
  trigger: manual;
  step-1: run cmd=echo "Documentation generation not yet implemented";
}

workflow[name="dev-server"] {
  trigger: manual;
  step-1: run cmd=echo "No development server available";
}

workflow[name="format"] {
  trigger: manual;
  step-1: run cmd=poetry run ruff format src/ tests/;
}

workflow[name="fix"] {
  trigger: manual;
  step-1: run cmd=poetry run ruff check --fix src/ tests/;
}

workflow[name="llm-test"] {
  trigger: manual;
  step-1: run cmd=poetry run python -c "from propact.llm_proxy import LiteLLMProxy; print('LiteLLM import OK')";
  step-2: run cmd=poetry run propact --help | grep -q llm-provider && echo "CLI LLM flags OK";
  step-3: run cmd=echo "✅ LiteLLM multi-provider configuration OK!";
}

workflow[name="llm-bench"] {
  trigger: manual;
  step-1: run cmd=echo "Benchmarking LLM providers...";
  step-2: run cmd=poetry run python -c "import asyncio; from propact.llm_proxy import quick_generate; asyncio.run(quick_generate('Say hello', provider='local'))" 2>/dev/null || echo "Ollama not available";
  step-3: run cmd=echo "✅ LLM benchmark complete";
}

workflow[name="public-demo"] {
  trigger: manual;
  step-1: run cmd=echo "🚀 Running public APIs demo...";
  step-2: run cmd=cd examples/public-apis && ./demo-public.sh;
}

workflow[name="install-llm"] {
  trigger: manual;
  step-1: run cmd=poetry install --extras llm;
}

deploy {
  target: makefile;
}

environment[name="local"] {
  runtime: docker-compose;
}
```

## Interfaces

### testql Scenarios

#### `testql-scenarios/generated-cli-tests.testql.toon.yaml`

```toon markpact:testql path=testql-scenarios/generated-cli-tests.testql.toon.yaml
# SCENARIO: CLI Command Tests
# TYPE: cli
# GENERATED: true

CONFIG[2]{key, value}:
  cli_command, python -m propact
  timeout_ms, 10000

# Test 1: CLI help command
SHELL "python -m propact --help" 5000
ASSERT_EXIT_CODE 0
ASSERT_STDOUT_CONTAINS "usage"

# Test 2: CLI version command
SHELL "python -m propact --version" 5000
ASSERT_EXIT_CODE 0

# Test 3: CLI main workflow (dry-run)
SHELL "python -m propact --help" 10000
ASSERT_EXIT_CODE 0
```

#### `testql-scenarios/generated-from-pytests.testql.toon.yaml`

```toon markpact:testql path=testql-scenarios/generated-from-pytests.testql.toon.yaml
# SCENARIO: Auto-generated from Python Tests
# TYPE: integration
# GENERATED: true

CONFIG[2]{key, value}:
  base_url, ${api_url:-http://localhost:8101}
  timeout_ms, 10000

# Converted 12 assertions from pytest
ASSERT[12]{field, operator, expected}:
  request.method, ==, HTTPMethod.GET
  request.url, ==, "https://api.example.com/test"
  request.headers.Content-Type, ==, "application/json"
  request.method, ==, HTTPMethod.GET
  request.url, ==, "https://api.example.com/test"
  request.headers.Content-Type, ==, "application/json"
  request.method, ==, HTTPMethod.GET
  request.url, ==, "https://api.example.com/test"
  request.headers.Content-Type, ==, "application/json"
  request.method, ==, HTTPMethod.GET
  request.url, ==, "https://api.example.com/test"
  request.headers.Content-Type, ==, "application/json"
```

## Workflows

## Configuration

```yaml
project:
  name: propact
  version: 0.0.0
  env: local
```

## Deployment

```bash markpact:run
pip install propact

# development install
pip install -e .[dev]
```

## Environment Variables (`.env.example`)

| Variable | Default | Description |
|----------|---------|-------------|
| `OPENAI_API_KEY` | `your_openai_api_key_here` | OpenAI Configuration |
| `OPENAI_BASE_URL` | `https://api.openai.com/v1` |  |
| `GRPC_HOST` | `localhost` | gRPC Configuration |
| `GRPC_PORT` | `50051` |  |
| `MQTT_HOST` | `localhost` | MQTT Configuration |
| `MQTT_PORT` | `1883` |  |
| `MQTT_USERNAME` | `*(not set)*` |  |
| `MQTT_PASSWORD` | `*(not set)*` |  |
| `MQTT_CLIENT_ID` | `propact_client` |  |
| `SMTP_HOST` | `smtp.gmail.com` | SMTP Configuration |
| `SMTP_PORT` | `587` |  |
| `SMTP_USERNAME` | `your_email@gmail.com` |  |
| `SMTP_PASSWORD` | `your_app_password` |  |
| `SMTP_FROM` | `propact@example.com` |  |
| `WS_HOST` | `localhost` | WebSocket Configuration |
| `WS_PORT` | `8080` |  |
| `SERVER_HOST` | `0.0.0.0` | Server Configuration |
| `SERVER_PORT` | `8080` |  |
| `MCP_HOST` | `localhost` | MCP Configuration |
| `MCP_PORT` | `8080` |  |
| `LOG_LEVEL` | `INFO` | Logging Configuration |
| `LOG_FORMAT` | `%(asctime)s - %(name)s - %(levelname)s - %(message)s` |  |
| `DEBUG` | `false` | Development Configuration |
| `TEST_MODE` | `false` |  |
| `DATA_DIR` | `./data` | File Paths |
| `CACHE_DIR` | `./cache` |  |
| `TEMP_DIR` | `./temp` |  |
| `REQUEST_TIMEOUT` | `30` | Timeout Configuration |
| `WEBSOCKET_TIMEOUT` | `60` |  |
| `GRPC_TIMEOUT` | `30` |  |
| `RATE_LIMIT_REQUESTS` | `100` | Rate Limiting |
| `RATE_LIMIT_WINDOW` | `60` |  |
| `CORS_ORIGINS` | `*` | Security |
| `API_KEY` | `*(not set)*` |  |

## Release Management (`goal.yaml`)

- **versioning**: `semver`
- **commits**: `conventional` scope=`propact`
- **changelog**: `keep-a-changelog`
- **build strategies**: `python`, `nodejs`, `rust`
- **version files**: `VERSION`, `pyproject.toml:version`, `venv/lib/python3.13/site-packages/httpcore/__init__.py:__version__`

## Makefile Targets

- `install` — Install dependencies
- `dev` — Install development dependencies
- `test` — Run tests
- `test-cov` — Run tests with coverage
- `lint` — Run linting
- `type-check` — Run type checking
- `check` — Run all checks
- `clean` — Clean build artifacts
- `build` — Build package
- `publish` — Publish to PyPI
- `publish-test` — Publish to test PyPI
- `docs` — Generate documentation
- `dev-server` — Run development server (if applicable)
- `format` — Format code
- `fix` — Fix linting issues
- `llm-test` — LLM testing targets
- `llm-bench`
- `public-demo`
- `install-llm`

## Code Analysis

### `project/map.toon.yaml`

```toon markpact:analysis path=project/map.toon.yaml
# propact | 64f 10185L | python:32,shell:31,less:1 | 2026-06-01
# stats: 44 func | 78 cls | 64 mod | CC̄=3.4 | critical:5 | cycles:0
# alerts[5]: CC universal=17; CC file=15; CC display_results=12; CC run_example=12; CC string=11
# hotspots[5]: main fan=31; send_email fan=13; file fan=12; batch fan=12; test_matcher fan=11
# evolution: baseline
# Keys: M=modules, D=details, i=imports, e=exports, c=classes, f=functions, m=methods
M[64]:
  app.doql.less,124
  examples/01-shell-upload/run.sh,40
  examples/02-openapi-rest/run.sh,37
  examples/03-mcp-tool/run.sh,37
  examples/04-ws-chat/run.sh,37
  examples/05-md-server/run.sh,37
  examples/05-security-hardening/run.sh,52
  examples/05-security-hardening/secure_handler.py,255
  examples/06-openai-vision/run.sh,37
  examples/07-ffmpeg-cli/run.sh,37
  examples/08-grpc-inference/run.sh,37
  examples/09-imgur/run.sh,47
  examples/10-slack/run.sh,47
  examples/11-discord/run.sh,46
  examples/12-openai-vision/run.sh,47
  examples/13-github-gist/run.sh,43
  examples/14-stripe/run.sh,43
  examples/15-youtube/run.sh,43
  examples/16-notion/run.sh,47
  examples/17-twitter/run.sh,48
  examples/18-todo-api/run.sh,41
  examples/19-users-api/run.sh,41
  examples/20-posts-api/run.sh,41
  examples/21-albums-api/run.sh,38
  examples/22-comments-api/run.sh,38
  examples/23-photos-api/run.sh,38
  examples/public-apis/demo-public.sh,50
  examples/run-all.sh,372
  examples/run-new-examples.sh,42
  examples/smart-test/test_matcher.py,45
  project.sh,50
  src/propact/__init__.py,30
  src/propact/adapters.py,367
  src/propact/attachments.py,94
  src/propact/cli.py,667
  src/propact/config.py,365
  src/propact/constants.py,63
  src/propact/converter.py,376
  src/propact/core.py,237
  src/propact/dsl_converter.py,812
  src/propact/enhanced.py,417
  src/propact/error_handler.py,362
  src/propact/importer.py,116
  src/propact/llm_proxy.py,279
  src/propact/matcher.py,445
  src/propact/optimization.py,362
  src/propact/parser.py,101
  src/propact/protocols/__init__.py,9
  src/propact/protocols/mcp.py,111
  src/propact/protocols/rest.py,128
  src/propact/protocols/shell.py,75
  src/propact/protocols/ws.py,150
  src/propact/query_gen.py,202
  src/propact/security.py,264
  src/propact/testing.py,202
  src/propact/uniconverter.py,760
  src/propact/validation.py,415
  test_all_examples.sh,95
  test_examples_final.sh,101
  tests/__init__.py,5
  tests/test_core.py,185
  tests/test_error_handler.py,174
  tests/test_protocols.py,162
  verify_examples.sh,117
D:
  examples/05-security-hardening/secure_handler.py:
    e: demo_security,SecurityEventHandler,SecureMarkdownHandler
    SecurityEventHandler: __init__(0),handle_violation(2),get_report(0)  # Handles security events and logging.
    SecureMarkdownHandler: __init__(1),process(2),get_security_report(0)  # Secure handler for processing markdown content.
    demo_security()
  examples/smart-test/test_matcher.py:
    e: test_matcher
    test_matcher()
  src/propact/__init__.py:
  src/propact/adapters.py:
    e: get_protocol_adapter,BaseProtocolAdapter,GRPCAdapter,GraphQLAdapter,MQTTAdapter,SOAPAdapter,EmailAdapter
    BaseProtocolAdapter: __init__(1),send(1),is_available(0)  # Base class for protocol adapters.
    GRPCAdapter: __init__(1),is_available(0),send(1)  # Adapter for gRPC protocol.
    GraphQLAdapter: is_available(0),send(1)  # Adapter for GraphQL protocol.
    MQTTAdapter: __init__(1),is_available(0),send(1)  # Adapter for MQTT protocol.
    SOAPAdapter: __init__(1),is_available(0),send(1)  # Adapter for SOAP protocol.
    EmailAdapter: __init__(1),send(1)  # Adapter for Email protocol.
    get_protocol_adapter(protocol;endpoint)
  src/propact/attachments.py:
    e: AttachmentHandler
    AttachmentHandler: __init__(0),load_attachment(1),save_attachment(2),encode_base64(1),decode_base64(1),get_mime_type(1),extract_from_markdown(2)  # Handles binary attachments in Protocol Pact documents.
  src/propact/cli.py:
    e: cli,main,list_blocks,display_results,convert,file,string,formats,universal,send_email,batch
    cli()
    main(file_path;protocol;endpoint;openapi;base_url;openapi_llm_session;generate_spec;llm_key;error_mode;max_retries;schema;mode;port;list;verbose;dry_run;llm_provider;llm_model;method)
    list_blocks(pact)
    display_results(results;verbose)
    convert()
    file(input_file;from_format;to_format;output;dialect;table_name;operation;api_type;db_connection)
    string(content;from_format;to_format;dialect;table_name;operation;api_type)
    formats()
    universal(input_path;to_md;to_pdf;to_docx;to_pptx;to_xlsx;to_html;to_email;output)
    send_email(markdown_file;to_emails;subject;smtp_host;smtp_port;smtp_user;smtp_password;from_email;attach)
    batch(directory;to_md;output_dir;pattern)
  src/propact/config.py:
    e: get_config,init_config,reload_config,get_openai_config,get_grpc_config,get_mqtt_config,get_smtp_config,get_websocket_config,get_server_config,is_debug,is_test_mode,OpenAIConfig,GRPCConfig,MQTTConfig,SMTPConfig,WebSocketConfig,ServerConfig,MCPConfig,LoggingConfig,PathConfig,SecurityConfig,Config,ConfigManager
    OpenAIConfig:  # OpenAI API configuration.
    GRPCConfig:  # gRPC configuration.
    MQTTConfig:  # MQTT configuration.
    SMTPConfig:  # SMTP configuration for email.
    WebSocketConfig:  # WebSocket configuration.
    ServerConfig:  # Server configuration.
    MCPConfig:  # MCP configuration.
    LoggingConfig:  # Logging configuration.
    PathConfig:  # Path configuration.
    SecurityConfig:  # Security configuration.
    Config:  # Main configuration class.
    ConfigManager: __init__(1),_find_env_file(0),_load_env(0),_get_env_bool(2),_get_env_int(2),_get_env_path(2),config(0),_load_config(0),reload(0)  # Manages configuration loading and access.
    get_config()
    init_config(env_file)
    reload_config()
    get_openai_config()
    get_grpc_config()
    get_mqtt_config()
    get_smtp_config()
    get_websocket_config()
    get_server_config()
    is_debug()
    is_test_mode()
  src/propact/constants.py:
  src/propact/converter.py:
    e: MediaType,ExtractedContent,MDConverter
    MediaType:  # Supported media types for conversion.
    ExtractedContent: __post_init__(0)  # Represents content extracted from markdown.
    MDConverter: response_to_markdown(3),_binary_to_markdown(2),_dict_to_markdown(2),_text_to_markdown(2),extract_from_markdown(1),prepare_payload(2),_prepare_openapi_payload(2),_prepare_multipart_payload(1),_prepare_json_payload(1),_prepare_form_payload(1),embed_media(2),_get_mime_type(1),create_codeblock(2),merge_markdown(0)  # Universal converter for markdown ↔ various formats.
  src/propact/core.py:
    e: ToonPact
    ToonPact: __init__(1),smart_send(6),load(0),execute(1),_execute_shell(1),_execute_mcp(1),_execute_rest(1),_execute_ws(1)  # Main class for executing Protocol Pact documents.
  src/propact/dsl_converter.py:
    e: ConversionResult,BaseConverter,SQLConverter,GraphQLConverter,YAMLConverter,CSVConverter,XMLConverter,DSLConverter
    ConversionResult: __post_init__(0)  # Result of a conversion operation.
    BaseConverter: __init__(0),to_markdown(1),from_markdown(1),_parse_md_table(1),_create_md_table(3)  # Base class for format converters.
    SQLConverter: __init__(0),to_markdown(1),from_markdown(1),_mock_sql_result(1)  # Converter for SQL ↔ Markdown tables.
    GraphQLConverter: to_markdown(1),from_markdown(1),_extract_structured_data(1),_generate_github_query(1),_generate_stripe_query(1),_generate_generic_query(1)  # Converter for GraphQL ↔ Markdown.
    YAMLConverter: to_markdown(1),from_markdown(1),_dict_to_markdown(2),_list_to_markdown(1),_markdown_to_dict(1)  # Converter for YAML ↔ Markdown.
    CSVConverter: to_markdown(1),from_markdown(1)  # Converter for CSV ↔ Markdown tables.
    XMLConverter: to_markdown(1),from_markdown(1),_markdown_to_dict(1)  # Converter for XML ↔ Markdown.
    DSLConverter: __init__(0),convert(3),list_formats(0),register_converter(2)  # Main DSL converter using strategy pattern.
  src/propact/enhanced.py:
    e: SplitContent,Propact
    SplitContent: __post_init__(0)  # Represents split content ready for transport.
    Propact: __init__(4),_introspect_schema(1),_smart_split_md(2),_detect_schema_type(1),_adapt_to_openapi(2),_adapt_to_shell(2),_adapt_to_mcp(2),_get_mime_type(1),send_to_endpoint(1),_send_rest(3),_send_mcp(2),_send_ws(2),_send_shell(2),_response_to_md(1),server_mode(1)  # Enhanced Propact class with schema introspection and intelli
  src/propact/error_handler.py:
    e: ErrorMode,MatchError,PropactErrorHandler
    ErrorMode:  # Error handling modes.
    MatchError:  # Error information for recovery strategies.
    PropactErrorHandler: __init__(4),handle_match_failure(3),_llm_self_correct(2),_llm_self_correct_litellm(2),_llm_self_correct_ollama(2),_fallback_search(2),_fix_client_error(2),_fix_client_error_litellm(2),_fix_client_error_ollama(2),_retry_with_backoff(1),_simplify_and_retry(2),_generic_fallback(2),_extract_intent(1),_extract_keywords(1),_confirm_fix(0)  # Multi-layer error recovery system for Propact.
  src/propact/importer.py:
    e: OpenAPILLMImporter
    OpenAPILLMImporter: import_browser_spec(1),from_browser_session(2),is_llm_enhanced(1),extract_llm_descriptions(1)  # Imports and enhances OpenAPI specs generated by openapi-llm.
  src/propact/llm_proxy.py:
    e: quick_generate,match_intent,self_correct,LLMConfig,LiteLLMProxy
    LLMConfig:  # Configuration for an LLM provider.
    LiteLLMProxy: __init__(2),_load_config(2),generate(4),astream(2),generate_sync(2),list_providers(1),from_env(2)  # Unified interface for 100+ LLM providers via LiteLLM.
    quick_generate(prompt;provider)
    match_intent(query;candidates;provider)
    self_correct(error;context;provider)
  src/propact/matcher.py:
    e: create_matcher,create_llm_matcher,EndpointMatcher,OpenAPILLMMatcher
    EndpointMatcher: __init__(2),extract_intent(1),extract_endpoints(1),compute_similarities(2),match(3),match_from_file(3)  # Matches markdown content to OpenAPI endpoints using semantic
    OpenAPILLMMatcher: __init__(2),_llm_select(4),match(4),_extract_intent(1),_extract_candidates(1),hybrid_match(4)  # LLM-based semantic matcher for fast/accurate endpoint select
    create_matcher(model_name;error_handler)
    create_llm_matcher(fast_provider;accurate_provider)
  src/propact/optimization.py:
    e: create_optimizer,OptimizationConfig,MediaRefManager,MDOptimizer
    OptimizationConfig: __post_init__(0)  # Configuration for payload optimization.
    MediaRefManager: __init__(1),generate_ref(2),should_externalize(2)  # Manages external media references.
    MDOptimizer: __init__(1),optimize(1),_optimize_base64_images(1),_optimize_image(2),_optimize_code_blocks(1),_add_compression_metadata(1),create_chunks(2),get_optimization_report(2)  # Markdown payload optimizer.
    create_optimizer(enable_compression;enable_image_optimization;chunk_size)
  src/propact/parser.py:
    e: ProtocolType,ProtocolBlock,MarkdownParser
    ProtocolType:  # Supported protocol types.
    ProtocolBlock: __post_init__(0)  # Represents a protocol block in markdown.
    MarkdownParser: __init__(0),parse(1),_extract_attachments(1),_extract_metadata(1)  # Parser for extracting protocol blocks from markdown document
  src/propact/protocols/__init__.py:
  src/propact/protocols/mcp.py:
    e: MCPMessage,MCPProtocol
    MCPMessage:  # MCP message structure.
    MCPProtocol: __init__(1),register_tool(3),register_resource(4),execute_tool(2),get_resource(1),create_list_tools_response(1),create_list_resources_response(1)  # Handles MCP (Model Context Protocol) communication within Pr
  src/propact/protocols/rest.py:
    e: HTTPMethod,RESTRequest,RESTResponse,RESTProtocol
    HTTPMethod:  # HTTP methods supported by REST protocol.
    RESTRequest:  # REST request structure.
    RESTResponse:  # REST response structure.
    RESTProtocol: __init__(2),execute(1),get(3),post(3),put(3),delete(2)  # Handles REST API communication within Protocol Pact.
  src/propact/protocols/shell.py:
    e: ShellProtocol
    ShellProtocol: __init__(1),execute(3),execute_script(3)  # Handles shell command execution within Protocol Pact.
  src/propact/protocols/ws.py:
    e: WebSocketState,WebSocketMessage,WebSocketProtocol
    WebSocketState:  # WebSocket connection states.
    WebSocketMessage:  # WebSocket message structure.
    WebSocketProtocol: __init__(2),connect(0),disconnect(0),send(1),receive(0),add_message_handler(1),remove_message_handler(1)  # Handles WebSocket communication within Protocol Pact.
  src/propact/query_gen.py:
    e: query_to_md,batch_generate,QueryGenerator
    QueryGenerator: __init__(1),generate_md(1),generate_from_spec(3),suggest_endpoint(3),enhance_template(3),_render_template(1)  # Generate Propact MD templates from natural language queries 
    query_to_md(query;provider)
    batch_generate(queries;provider)
  src/propact/security.py:
    e: create_sanitizer,SanitizationConfig,MDSanitizer
    SanitizationConfig: __post_init__(0)  # Configuration for markdown sanitization.
    MDSanitizer: __init__(1),sanitize(2),_remove_scripts(1),_sanitize_links(1),_sanitize_base64_images(1),_sanitize_html(1),_strict_sanitization(1),audit(1)  # Markdown sanitizer for security protection.
    create_sanitizer(strict;allow_html)
  src/propact/testing.py:
    e: run_example,ExampleHelper
    ExampleHelper: create_sample_file(3),cleanup_files(0),check_dependencies(1),check_env_var(1),print_status(2),run_example(5)  # Helper class for creating and managing example files.
    run_example(example_dir;endpoint;schema;mode;port)
  src/propact/uniconverter.py:
    e: ConversionResult,EmailConfig,UniConverter
    ConversionResult: __post_init__(0)  # Result of a universal conversion operation.
    EmailConfig:  # Configuration for email sending.
    UniConverter: __init__(0),to_markdown(2),from_markdown(3),send_email(5),_markitdown_to_md(1),_html_to_md(1),_email_to_md(1),_pandoc_to_md(2),_md_to_pdf(2),_md_to_html(2),_md_to_docx(2),_md_to_pptx(2),_md_to_xlsx(2),_md_to_email(2),_pandoc_from_md(3),get_supported_formats(0)  # Universal document converter supporting 15+ formats.
  src/propact/validation.py:
    e: ValidationResult,SchemaInfo,SchemaRegistry,ValidationPipeline
    ValidationResult:  # Result of validation.
    SchemaInfo:  # Information about a schema.
    SchemaRegistry: __init__(1),_load_schemas(0),get_schema(2),register_schema(3),detect_drift(3)  # Registry for managing API schemas.
    ValidationPipeline: __init__(3),validate(4),_validate_against_schema(2),_validate_types(1),create_schema_pin(3),detect_schema_drift(1)  # Pipeline for validating markdown content.
  tests/__init__.py:
  tests/test_core.py:
    e: sample_markdown,parser,attachment_handler,TestMarkdownParser,TestAttachmentHandler,TestProtocolBlock,TestToonPact
    TestMarkdownParser: test_parse_shell_block(2),test_parse_mcp_block(2),test_parse_rest_block(2),test_parse_ws_block(2),test_parse_empty_content(1)  # Test cases for MarkdownParser.
    TestAttachmentHandler: test_encode_decode_base64(1),test_get_mime_type(1)  # Test cases for AttachmentHandler.
    TestProtocolBlock: test_protocol_block_creation(0),test_protocol_block_defaults(0)  # Test cases for ProtocolBlock dataclass.
    TestToonPact: temp_markdown_file(2),test_load_document(1),test_execute_shell_protocol(1)  # Test cases for ToonPact class.
    sample_markdown()
    parser()
    attachment_handler()
  tests/test_error_handler.py:
    e: test_no_match_recovery,test_validation_error_recovery,test_fallback_search,test_retry_logic,test_interactive_mode,main
    test_no_match_recovery()
    test_validation_error_recovery()
    test_fallback_search()
    test_retry_logic()
    test_interactive_mode()
    main()
  tests/test_protocols.py:
    e: TestShellProtocol,TestMCPProtocol,TestRESTProtocol,TestWebSocketProtocol
    TestShellProtocol: test_execute_simple_command(0),test_execute_failing_command(0)  # Test cases for ShellProtocol.
    TestMCPProtocol: test_register_tool(0),test_register_resource(0),test_execute_tool_not_implemented(0)  # Test cases for MCPProtocol.
    TestRESTProtocol: test_rest_request_creation(0),test_execute_get_request(0),test_get_method(0),test_post_method(0)  # Test cases for RESTProtocol.
    TestWebSocketProtocol: test_websocket_creation(0),test_connect_disconnect(0),test_send_message(0),test_receive_message(0)  # Test cases for WebSocketProtocol.
```

### `project/logic.pl`

```prolog markpact:analysis path=project/logic.pl
% ── Project Metadata ─────────────────────────────────────
project_metadata('propact', '0.0.0', 'python').

% ── Project Files ────────────────────────────────────────
project_file('app.doql.less', 124, 'less').
project_file('examples/01-shell-upload/run.sh', 40, 'shell').
project_file('examples/02-openapi-rest/run.sh', 37, 'shell').
project_file('examples/03-mcp-tool/run.sh', 37, 'shell').
project_file('examples/04-ws-chat/run.sh', 37, 'shell').
project_file('examples/05-md-server/run.sh', 37, 'shell').
project_file('examples/05-security-hardening/run.sh', 52, 'shell').
project_file('examples/05-security-hardening/secure_handler.py', 255, 'python').
project_file('examples/06-openai-vision/run.sh', 37, 'shell').
project_file('examples/07-ffmpeg-cli/run.sh', 37, 'shell').
project_file('examples/08-grpc-inference/run.sh', 37, 'shell').
project_file('examples/09-imgur/run.sh', 47, 'shell').
project_file('examples/10-slack/run.sh', 47, 'shell').
project_file('examples/11-discord/run.sh', 46, 'shell').
project_file('examples/12-openai-vision/run.sh', 47, 'shell').
project_file('examples/13-github-gist/run.sh', 43, 'shell').
project_file('examples/14-stripe/run.sh', 43, 'shell').
project_file('examples/15-youtube/run.sh', 43, 'shell').
project_file('examples/16-notion/run.sh', 47, 'shell').
project_file('examples/17-twitter/run.sh', 48, 'shell').
project_file('examples/18-todo-api/run.sh', 41, 'shell').
project_file('examples/19-users-api/run.sh', 41, 'shell').
project_file('examples/20-posts-api/run.sh', 41, 'shell').
project_file('examples/21-albums-api/run.sh', 38, 'shell').
project_file('examples/22-comments-api/run.sh', 38, 'shell').
project_file('examples/23-photos-api/run.sh', 38, 'shell').
project_file('examples/public-apis/demo-public.sh', 50, 'shell').
project_file('examples/run-all.sh', 372, 'shell').
project_file('examples/run-new-examples.sh', 42, 'shell').
project_file('examples/smart-test/test_matcher.py', 45, 'python').
project_file('project.sh', 50, 'shell').
project_file('src/propact/__init__.py', 30, 'python').
project_file('src/propact/adapters.py', 367, 'python').
project_file('src/propact/attachments.py', 94, 'python').
project_file('src/propact/cli.py', 667, 'python').
project_file('src/propact/config.py', 365, 'python').
project_file('src/propact/constants.py', 63, 'python').
project_file('src/propact/converter.py', 376, 'python').
project_file('src/propact/core.py', 237, 'python').
project_file('src/propact/dsl_converter.py', 812, 'python').
project_file('src/propact/enhanced.py', 417, 'python').
project_file('src/propact/error_handler.py', 362, 'python').
project_file('src/propact/importer.py', 116, 'python').
project_file('src/propact/llm_proxy.py', 279, 'python').
project_file('src/propact/matcher.py', 445, 'python').
project_file('src/propact/optimization.py', 362, 'python').
project_file('src/propact/parser.py', 101, 'python').
project_file('src/propact/protocols/__init__.py', 9, 'python').
project_file('src/propact/protocols/mcp.py', 111, 'python').
project_file('src/propact/protocols/rest.py', 128, 'python').
project_file('src/propact/protocols/shell.py', 75, 'python').
project_file('src/propact/protocols/ws.py', 150, 'python').
project_file('src/propact/query_gen.py', 202, 'python').
project_file('src/propact/security.py', 264, 'python').
project_file('src/propact/testing.py', 202, 'python').
project_file('src/propact/uniconverter.py', 760, 'python').
project_file('src/propact/validation.py', 415, 'python').
project_file('test_all_examples.sh', 95, 'shell').
project_file('test_examples_final.sh', 101, 'shell').
project_file('tests/__init__.py', 5, 'python').
project_file('tests/test_core.py', 185, 'python').
project_file('tests/test_error_handler.py', 174, 'python').
project_file('tests/test_protocols.py', 162, 'python').
project_file('verify_examples.sh', 117, 'shell').

% ── Python Functions ─────────────────────────────────────
python_function('examples/05-security-hardening/secure_handler.py', 'demo_security', 0, 9, 9).
python_function('examples/smart-test/test_matcher.py', 'test_matcher', 0, 4, 11).
python_function('src/propact/adapters.py', 'get_protocol_adapter', 2, 2, 4).
python_function('src/propact/cli.py', 'cli', 0, 1, 1).
python_function('src/propact/cli.py', 'main', 19, 2, 31).
python_function('src/propact/cli.py', 'list_blocks', 1, 4, 8).
python_function('src/propact/cli.py', 'display_results', 2, 12, 7).
python_function('src/propact/cli.py', 'convert', 0, 1, 1).
python_function('src/propact/cli.py', 'file', 9, 15, 12).
python_function('src/propact/cli.py', 'string', 7, 11, 9).
python_function('src/propact/cli.py', 'formats', 0, 2, 9).
python_function('src/propact/cli.py', 'universal', 9, 17, 11).
python_function('src/propact/cli.py', 'send_email', 9, 6, 13).
python_function('src/propact/cli.py', 'batch', 4, 8, 12).
python_function('src/propact/config.py', 'get_config', 0, 2, 1).
python_function('src/propact/config.py', 'init_config', 1, 1, 1).
python_function('src/propact/config.py', 'reload_config', 0, 2, 1).
python_function('src/propact/config.py', 'get_openai_config', 0, 1, 1).
python_function('src/propact/config.py', 'get_grpc_config', 0, 1, 1).
python_function('src/propact/config.py', 'get_mqtt_config', 0, 1, 1).
python_function('src/propact/config.py', 'get_smtp_config', 0, 1, 1).
python_function('src/propact/config.py', 'get_websocket_config', 0, 1, 1).
python_function('src/propact/config.py', 'get_server_config', 0, 1, 1).
python_function('src/propact/config.py', 'is_debug', 0, 1, 1).
python_function('src/propact/config.py', 'is_test_mode', 0, 1, 1).
python_function('src/propact/llm_proxy.py', 'quick_generate', 2, 1, 2).
python_function('src/propact/llm_proxy.py', 'match_intent', 3, 2, 5).
python_function('src/propact/llm_proxy.py', 'self_correct', 3, 3, 9).
python_function('src/propact/matcher.py', 'create_matcher', 2, 2, 1).
python_function('src/propact/matcher.py', 'create_llm_matcher', 2, 2, 1).
python_function('src/propact/optimization.py', 'create_optimizer', 3, 1, 2).
python_function('src/propact/query_gen.py', 'query_to_md', 2, 1, 2).
python_function('src/propact/query_gen.py', 'batch_generate', 2, 2, 3).
python_function('src/propact/security.py', 'create_sanitizer', 2, 2, 2).
python_function('src/propact/testing.py', 'run_example', 5, 12, 1).
python_function('tests/test_core.py', 'sample_markdown', 0, 1, 0).
python_function('tests/test_core.py', 'parser', 0, 1, 1).
python_function('tests/test_core.py', 'attachment_handler', 0, 1, 1).
python_function('tests/test_error_handler.py', 'test_no_match_recovery', 0, 3, 6).
python_function('tests/test_error_handler.py', 'test_validation_error_recovery', 0, 2, 4).
python_function('tests/test_error_handler.py', 'test_fallback_search', 0, 2, 4).
python_function('tests/test_error_handler.py', 'test_retry_logic', 0, 4, 4).
python_function('tests/test_error_handler.py', 'test_interactive_mode', 0, 1, 3).
python_function('tests/test_error_handler.py', 'main', 0, 1, 6).

% ── Python Classes ───────────────────────────────────────
python_class('examples/05-security-hardening/secure_handler.py', 'SecurityEventHandler').
python_method('SecurityEventHandler', '__init__', 0, 1, 1).
python_method('SecurityEventHandler', 'handle_violation', 2, 1, 4).
python_method('SecurityEventHandler', 'get_report', 0, 1, 1).
python_class('examples/05-security-hardening/secure_handler.py', 'SecureMarkdownHandler').
python_method('SecureMarkdownHandler', '__init__', 1, 1, 6).
python_method('SecureMarkdownHandler', 'process', 2, 8, 15).
python_method('SecureMarkdownHandler', 'get_security_report', 0, 1, 1).
python_class('src/propact/adapters.py', 'BaseProtocolAdapter').
python_method('BaseProtocolAdapter', '__init__', 1, 1, 0).
python_method('BaseProtocolAdapter', 'send', 1, 16, 0).
python_method('BaseProtocolAdapter', 'is_available', 0, 1, 0).
python_class('src/propact/adapters.py', 'GRPCAdapter').
python_method('GRPCAdapter', '__init__', 1, 1, 3).
python_method('GRPCAdapter', 'is_available', 0, 1, 0).
python_method('GRPCAdapter', 'send', 1, 16, 7).
python_class('src/propact/adapters.py', 'GraphQLAdapter').
python_method('GraphQLAdapter', 'is_available', 0, 1, 0).
python_method('GraphQLAdapter', 'send', 1, 16, 8).
python_class('src/propact/adapters.py', 'MQTTAdapter').
python_method('MQTTAdapter', '__init__', 1, 1, 3).
python_method('MQTTAdapter', 'is_available', 0, 1, 0).
python_method('MQTTAdapter', 'send', 1, 16, 14).
python_class('src/propact/adapters.py', 'SOAPAdapter').
python_method('SOAPAdapter', '__init__', 1, 1, 3).
python_method('SOAPAdapter', 'is_available', 0, 1, 0).
python_method('SOAPAdapter', 'send', 1, 16, 6).
python_class('src/propact/adapters.py', 'EmailAdapter').
python_method('EmailAdapter', '__init__', 1, 1, 4).
python_method('EmailAdapter', 'send', 1, 16, 20).
python_class('src/propact/attachments.py', 'AttachmentHandler').
python_method('AttachmentHandler', '__init__', 0, 1, 0).
python_method('AttachmentHandler', 'load_attachment', 1, 2, 4).
python_method('AttachmentHandler', 'save_attachment', 2, 1, 3).
python_method('AttachmentHandler', 'encode_base64', 1, 1, 2).
python_method('AttachmentHandler', 'decode_base64', 1, 1, 2).
python_method('AttachmentHandler', 'get_mime_type', 1, 2, 2).
python_method('AttachmentHandler', 'extract_from_markdown', 2, 6, 6).
python_class('src/propact/config.py', 'OpenAIConfig').
python_class('src/propact/config.py', 'GRPCConfig').
python_class('src/propact/config.py', 'MQTTConfig').
python_class('src/propact/config.py', 'SMTPConfig').
python_class('src/propact/config.py', 'WebSocketConfig').
python_class('src/propact/config.py', 'ServerConfig').
python_class('src/propact/config.py', 'MCPConfig').
python_class('src/propact/config.py', 'LoggingConfig').
python_class('src/propact/config.py', 'PathConfig').
python_class('src/propact/config.py', 'SecurityConfig').
python_class('src/propact/config.py', 'Config').
python_class('src/propact/config.py', 'ConfigManager').
python_method('ConfigManager', '__init__', 1, 2, 2).
python_method('ConfigManager', '_find_env_file', 0, 3, 2).
python_method('ConfigManager', '_load_env', 0, 3, 1).
python_method('ConfigManager', '_get_env_bool', 2, 1, 3).
python_method('ConfigManager', '_get_env_int', 2, 2, 3).
python_method('ConfigManager', '_get_env_path', 2, 1, 2).
python_method('ConfigManager', 'config', 0, 2, 1).
python_method('ConfigManager', '_load_config', 0, 1, 16).
python_method('ConfigManager', 'reload', 0, 1, 1).
python_class('src/propact/converter.py', 'MediaType').
python_class('src/propact/converter.py', 'ExtractedContent').
python_method('ExtractedContent', '__post_init__', 0, 4, 0).
python_class('src/propact/converter.py', 'MDConverter').
python_method('MDConverter', 'response_to_markdown', 3, 6, 6).
python_method('MDConverter', '_binary_to_markdown', 2, 7, 3).
python_method('MDConverter', '_dict_to_markdown', 2, 7, 8).
python_method('MDConverter', '_text_to_markdown', 2, 7, 3).
python_method('MDConverter', 'extract_from_markdown', 1, 13, 14).
python_method('MDConverter', 'prepare_payload', 2, 6, 6).
python_method('MDConverter', '_prepare_openapi_payload', 2, 6, 4).
python_method('MDConverter', '_prepare_multipart_payload', 1, 3, 3).
python_method('MDConverter', '_prepare_json_payload', 1, 1, 0).
python_method('MDConverter', '_prepare_form_payload', 1, 3, 4).
python_method('MDConverter', 'embed_media', 2, 3, 7).
python_method('MDConverter', '_get_mime_type', 1, 2, 2).
python_method('MDConverter', 'create_codeblock', 2, 5, 5).
python_method('MDConverter', 'merge_markdown', 0, 3, 2).
python_class('src/propact/core.py', 'ToonPact').
python_method('ToonPact', '__init__', 1, 1, 3).
python_method('ToonPact', 'smart_send', 6, 13, 20).
python_method('ToonPact', 'load', 0, 1, 2).
python_method('ToonPact', 'execute', 1, 9, 6).
python_method('ToonPact', '_execute_shell', 1, 1, 1).
python_method('ToonPact', '_execute_mcp', 1, 1, 0).
python_method('ToonPact', '_execute_rest', 1, 1, 0).
python_method('ToonPact', '_execute_ws', 1, 1, 0).
python_class('src/propact/dsl_converter.py', 'ConversionResult').
python_method('ConversionResult', '__post_init__', 0, 4, 0).
python_class('src/propact/dsl_converter.py', 'BaseConverter').
python_method('BaseConverter', '__init__', 0, 1, 1).
python_method('BaseConverter', 'to_markdown', 1, 4, 0).
python_method('BaseConverter', 'from_markdown', 1, 4, 0).
python_method('BaseConverter', '_parse_md_table', 1, 15, 6).
python_method('BaseConverter', '_create_md_table', 3, 15, 7).
python_class('src/propact/dsl_converter.py', 'SQLConverter').
python_method('SQLConverter', '__init__', 0, 1, 2).
python_method('SQLConverter', 'to_markdown', 1, 4, 12).
python_method('SQLConverter', 'from_markdown', 1, 4, 14).
python_method('SQLConverter', '_mock_sql_result', 1, 3, 2).
python_class('src/propact/dsl_converter.py', 'GraphQLConverter').
python_method('GraphQLConverter', 'to_markdown', 1, 4, 2).
python_method('GraphQLConverter', 'from_markdown', 1, 4, 7).
python_method('GraphQLConverter', '_extract_structured_data', 1, 5, 3).
python_method('GraphQLConverter', '_generate_github_query', 1, 1, 1).
python_method('GraphQLConverter', '_generate_stripe_query', 1, 1, 0).
python_method('GraphQLConverter', '_generate_generic_query', 1, 1, 0).
python_class('src/propact/dsl_converter.py', 'YAMLConverter').
python_method('YAMLConverter', 'to_markdown', 1, 4, 6).
python_method('YAMLConverter', 'from_markdown', 1, 4, 5).
python_method('YAMLConverter', '_dict_to_markdown', 2, 5, 5).
python_method('YAMLConverter', '_list_to_markdown', 1, 3, 4).
python_method('YAMLConverter', '_markdown_to_dict', 1, 5, 3).
python_class('src/propact/dsl_converter.py', 'CSVConverter').
python_method('CSVConverter', 'to_markdown', 1, 4, 10).
python_method('CSVConverter', 'from_markdown', 1, 4, 9).
python_class('src/propact/dsl_converter.py', 'XMLConverter').
python_method('XMLConverter', 'to_markdown', 1, 4, 4).
python_method('XMLConverter', 'from_markdown', 1, 4, 6).
python_method('XMLConverter', '_markdown_to_dict', 1, 5, 3).
python_class('src/propact/dsl_converter.py', 'DSLConverter').
python_method('DSLConverter', '__init__', 0, 1, 6).
python_method('DSLConverter', 'convert', 3, 9, 6).
python_method('DSLConverter', 'list_formats', 0, 1, 2).
python_method('DSLConverter', 'register_converter', 2, 1, 1).
python_class('src/propact/enhanced.py', 'SplitContent').
python_method('SplitContent', '__post_init__', 0, 4, 0).
python_class('src/propact/enhanced.py', 'Propact').
python_method('Propact', '__init__', 4, 2, 5).
python_method('Propact', '_introspect_schema', 1, 14, 8).
python_method('Propact', '_smart_split_md', 2, 1, 6).
python_method('Propact', '_detect_schema_type', 1, 5, 2).
python_method('Propact', '_adapt_to_openapi', 2, 6, 2).
python_method('Propact', '_adapt_to_shell', 2, 1, 0).
python_method('Propact', '_adapt_to_mcp', 2, 1, 0).
python_method('Propact', '_get_mime_type', 1, 2, 2).
python_method('Propact', 'send_to_endpoint', 1, 18, 15).
python_method('Propact', '_send_rest', 3, 17, 14).
python_method('Propact', '_send_mcp', 2, 1, 4).
python_method('Propact', '_send_ws', 2, 1, 4).
python_method('Propact', '_send_shell', 2, 7, 2).
python_method('Propact', '_response_to_md', 1, 11, 4).
python_method('Propact', 'server_mode', 1, 1, 1).
python_class('src/propact/error_handler.py', 'ErrorMode').
python_class('src/propact/error_handler.py', 'MatchError').
python_class('src/propact/error_handler.py', 'PropactErrorHandler').
python_method('PropactErrorHandler', '__init__', 4, 3, 2).
python_method('PropactErrorHandler', 'handle_match_failure', 3, 9, 8).
python_method('PropactErrorHandler', '_llm_self_correct', 2, 4, 4).
python_method('PropactErrorHandler', '_llm_self_correct_litellm', 2, 7, 7).
python_method('PropactErrorHandler', '_llm_self_correct_ollama', 2, 5, 8).
python_method('PropactErrorHandler', '_fallback_search', 2, 14, 6).
python_method('PropactErrorHandler', '_fix_client_error', 2, 4, 3).
python_method('PropactErrorHandler', '_fix_client_error_litellm', 2, 3, 4).
python_method('PropactErrorHandler', '_fix_client_error_ollama', 2, 3, 3).
python_method('PropactErrorHandler', '_retry_with_backoff', 1, 4, 5).
python_method('PropactErrorHandler', '_simplify_and_retry', 2, 2, 1).
python_method('PropactErrorHandler', '_generic_fallback', 2, 6, 3).
python_method('PropactErrorHandler', '_extract_intent', 1, 2, 5).
python_method('PropactErrorHandler', '_extract_keywords', 1, 3, 5).
python_method('PropactErrorHandler', '_confirm_fix', 0, 4, 3).
python_class('src/propact/importer.py', 'OpenAPILLMImporter').
python_method('OpenAPILLMImporter', 'import_browser_spec', 1, 6, 8).
python_method('OpenAPILLMImporter', 'from_browser_session', 2, 1, 0).
python_method('OpenAPILLMImporter', 'is_llm_enhanced', 1, 5, 1).
python_method('OpenAPILLMImporter', 'extract_llm_descriptions', 1, 8, 3).
python_class('src/propact/llm_proxy.py', 'LLMConfig').
python_class('src/propact/llm_proxy.py', 'LiteLLMProxy').
python_method('LiteLLMProxy', '__init__', 2, 2, 2).
python_method('LiteLLMProxy', '_load_config', 2, 4, 2).
python_method('LiteLLMProxy', 'generate', 4, 8, 3).
python_method('LiteLLMProxy', 'astream', 2, 6, 3).
python_method('LiteLLMProxy', 'generate_sync', 2, 1, 2).
python_method('LiteLLMProxy', 'list_providers', 1, 1, 2).
python_method('LiteLLMProxy', 'from_env', 2, 1, 3).
python_class('src/propact/matcher.py', 'EndpointMatcher').
python_method('EndpointMatcher', '__init__', 2, 2, 3).
python_method('EndpointMatcher', 'extract_intent', 1, 4, 6).
python_method('EndpointMatcher', 'extract_endpoints', 1, 8, 5).
python_method('EndpointMatcher', 'compute_similarities', 2, 4, 6).
python_method('EndpointMatcher', 'match', 3, 3, 9).
python_method('EndpointMatcher', 'match_from_file', 3, 3, 8).
python_class('src/propact/matcher.py', 'OpenAPILLMMatcher').
python_method('OpenAPILLMMatcher', '__init__', 2, 2, 2).
python_method('OpenAPILLMMatcher', '_llm_select', 4, 4, 6).
python_method('OpenAPILLMMatcher', 'match', 4, 3, 3).
python_method('OpenAPILLMMatcher', '_extract_intent', 1, 5, 7).
python_method('OpenAPILLMMatcher', '_extract_candidates', 1, 4, 6).
python_method('OpenAPILLMMatcher', 'hybrid_match', 4, 7, 4).
python_class('src/propact/optimization.py', 'OptimizationConfig').
python_method('OptimizationConfig', '__post_init__', 0, 2, 1).
python_class('src/propact/optimization.py', 'MediaRefManager').
python_method('MediaRefManager', '__init__', 1, 2, 1).
python_method('MediaRefManager', 'generate_ref', 2, 2, 4).
python_method('MediaRefManager', 'should_externalize', 2, 3, 1).
python_class('src/propact/optimization.py', 'MDOptimizer').
python_method('MDOptimizer', '__init__', 1, 2, 5).
python_method('MDOptimizer', 'optimize', 1, 4, 5).
python_method('MDOptimizer', '_optimize_base64_images', 1, 1, 12).
python_method('MDOptimizer', '_optimize_image', 2, 9, 11).
python_method('MDOptimizer', '_optimize_code_blocks', 1, 1, 12).
python_method('MDOptimizer', '_add_compression_metadata', 1, 2, 3).
python_method('MDOptimizer', 'create_chunks', 2, 6, 4).
python_method('MDOptimizer', 'get_optimization_report', 2, 3, 1).
python_class('src/propact/parser.py', 'ProtocolType').
python_class('src/propact/parser.py', 'ProtocolBlock').
python_method('ProtocolBlock', '__post_init__', 0, 3, 0).
python_class('src/propact/parser.py', 'MarkdownParser').
python_method('MarkdownParser', '__init__', 0, 1, 1).
python_method('MarkdownParser', 'parse', 1, 2, 8).
python_method('MarkdownParser', '_extract_attachments', 1, 2, 3).
python_method('MarkdownParser', '_extract_metadata', 1, 4, 3).
python_class('src/propact/protocols/mcp.py', 'MCPMessage').
python_class('src/propact/protocols/mcp.py', 'MCPProtocol').
python_method('MCPProtocol', '__init__', 1, 1, 0).
python_method('MCPProtocol', 'register_tool', 3, 1, 1).
python_method('MCPProtocol', 'register_resource', 4, 1, 1).
python_method('MCPProtocol', 'execute_tool', 2, 1, 0).
python_method('MCPProtocol', 'get_resource', 1, 1, 0).
python_method('MCPProtocol', 'create_list_tools_response', 1, 1, 1).
python_method('MCPProtocol', 'create_list_resources_response', 1, 1, 1).
python_class('src/propact/protocols/rest.py', 'HTTPMethod').
python_class('src/propact/protocols/rest.py', 'RESTRequest').
python_class('src/propact/protocols/rest.py', 'RESTResponse').
python_class('src/propact/protocols/rest.py', 'RESTProtocol').
python_method('RESTProtocol', '__init__', 2, 2, 0).
python_method('RESTProtocol', 'execute', 1, 4, 5).
python_method('RESTProtocol', 'get', 3, 1, 2).
python_method('RESTProtocol', 'post', 3, 1, 2).
python_method('RESTProtocol', 'put', 3, 1, 2).
python_method('RESTProtocol', 'delete', 2, 1, 2).
python_class('src/propact/protocols/shell.py', 'ShellProtocol').
python_method('ShellProtocol', '__init__', 1, 1, 0).
python_method('ShellProtocol', 'execute', 3, 6, 4).
python_method('ShellProtocol', 'execute_script', 3, 1, 1).
python_class('src/propact/protocols/ws.py', 'WebSocketState').
python_class('src/propact/protocols/ws.py', 'WebSocketMessage').
python_class('src/propact/protocols/ws.py', 'WebSocketProtocol').
python_method('WebSocketProtocol', '__init__', 2, 2, 0).
python_method('WebSocketProtocol', 'connect', 0, 1, 1).
python_method('WebSocketProtocol', 'disconnect', 0, 1, 1).
python_method('WebSocketProtocol', 'send', 1, 3, 2).
python_method('WebSocketProtocol', 'receive', 0, 2, 4).
python_method('WebSocketProtocol', 'add_message_handler', 1, 1, 1).
python_method('WebSocketProtocol', 'remove_message_handler', 1, 2, 1).
python_class('src/propact/query_gen.py', 'QueryGenerator').
python_method('QueryGenerator', '__init__', 1, 1, 1).
python_method('QueryGenerator', 'generate_md', 1, 1, 1).
python_method('QueryGenerator', 'generate_from_spec', 3, 1, 5).
python_method('QueryGenerator', 'suggest_endpoint', 3, 2, 5).
python_method('QueryGenerator', 'enhance_template', 3, 2, 2).
python_method('QueryGenerator', '_render_template', 1, 1, 2).
python_class('src/propact/security.py', 'SanitizationConfig').
python_method('SanitizationConfig', '__post_init__', 0, 4, 0).
python_class('src/propact/security.py', 'MDSanitizer').
python_method('MDSanitizer', '__init__', 1, 3, 4).
python_method('MDSanitizer', 'sanitize', 2, 4, 5).
python_method('MDSanitizer', '_remove_scripts', 1, 1, 1).
python_method('MDSanitizer', '_sanitize_links', 1, 1, 6).
python_method('MDSanitizer', '_sanitize_base64_images', 1, 1, 5).
python_method('MDSanitizer', '_sanitize_html', 1, 3, 3).
python_method('MDSanitizer', '_strict_sanitization', 1, 1, 4).
python_method('MDSanitizer', 'audit', 1, 13, 8).
python_class('src/propact/testing.py', 'ExampleHelper').
python_method('ExampleHelper', 'create_sample_file', 3, 9, 6).
python_method('ExampleHelper', 'cleanup_files', 0, 4, 3).
python_method('ExampleHelper', 'check_dependencies', 1, 1, 1).
python_method('ExampleHelper', 'check_env_var', 1, 1, 1).
python_method('ExampleHelper', 'print_status', 2, 1, 2).
python_method('ExampleHelper', 'run_example', 5, 12, 7).
python_class('src/propact/uniconverter.py', 'ConversionResult').
python_method('ConversionResult', '__post_init__', 0, 4, 0).
python_class('src/propact/uniconverter.py', 'EmailConfig').
python_class('src/propact/uniconverter.py', 'UniConverter').
python_method('UniConverter', '__init__', 0, 3, 3).
python_method('UniConverter', 'to_markdown', 2, 9, 11).
python_method('UniConverter', 'from_markdown', 3, 11, 13).
python_method('UniConverter', 'send_email', 5, 9, 20).
python_method('UniConverter', '_markitdown_to_md', 1, 5, 7).
python_method('UniConverter', '_html_to_md', 1, 3, 6).
python_method('UniConverter', '_email_to_md', 1, 11, 14).
python_method('UniConverter', '_pandoc_to_md', 2, 3, 3).
python_method('UniConverter', '_md_to_pdf', 2, 3, 5).
python_method('UniConverter', '_md_to_html', 2, 2, 4).
python_method('UniConverter', '_md_to_docx', 2, 23, 16).
python_method('UniConverter', '_md_to_pptx', 2, 9, 10).
python_method('UniConverter', '_md_to_xlsx', 2, 10, 11).
python_method('UniConverter', '_md_to_email', 2, 2, 8).
python_method('UniConverter', '_pandoc_from_md', 3, 3, 3).
python_method('UniConverter', 'get_supported_formats', 0, 1, 2).
python_class('src/propact/validation.py', 'ValidationResult').
python_class('src/propact/validation.py', 'SchemaInfo').
python_class('src/propact/validation.py', 'SchemaRegistry').
python_method('SchemaRegistry', '__init__', 1, 2, 4).
python_method('SchemaRegistry', '_load_schemas', 0, 4, 12).
python_method('SchemaRegistry', 'get_schema', 2, 1, 1).
python_method('SchemaRegistry', 'register_schema', 3, 2, 8).
python_method('SchemaRegistry', 'detect_drift', 3, 2, 1).
python_class('src/propact/validation.py', 'ValidationPipeline').
python_method('ValidationPipeline', '__init__', 3, 2, 3).
python_method('ValidationPipeline', 'validate', 4, 16, 15).
python_method('ValidationPipeline', '_validate_against_schema', 2, 4, 3).
python_method('ValidationPipeline', '_validate_types', 1, 4, 2).
python_method('ValidationPipeline', 'create_schema_pin', 3, 1, 2).
python_method('ValidationPipeline', 'detect_schema_drift', 1, 8, 9).
python_class('tests/test_core.py', 'TestMarkdownParser').
python_method('TestMarkdownParser', 'test_parse_shell_block', 2, 6, 2).
python_method('TestMarkdownParser', 'test_parse_mcp_block', 2, 5, 2).
python_method('TestMarkdownParser', 'test_parse_rest_block', 2, 5, 2).
python_method('TestMarkdownParser', 'test_parse_ws_block', 2, 5, 2).
python_method('TestMarkdownParser', 'test_parse_empty_content', 1, 2, 2).
python_class('tests/test_core.py', 'TestAttachmentHandler').
python_method('TestAttachmentHandler', 'test_encode_decode_base64', 1, 2, 2).
python_method('TestAttachmentHandler', 'test_get_mime_type', 1, 4, 1).
python_class('tests/test_core.py', 'TestProtocolBlock').
python_method('TestProtocolBlock', 'test_protocol_block_creation', 0, 5, 1).
python_method('TestProtocolBlock', 'test_protocol_block_defaults', 0, 3, 1).
python_class('tests/test_core.py', 'TestToonPact').
python_method('TestToonPact', 'temp_markdown_file', 2, 1, 1).
python_method('TestToonPact', 'test_load_document', 1, 2, 3).
python_method('TestToonPact', 'test_execute_shell_protocol', 1, 5, 3).
python_class('tests/test_protocols.py', 'TestShellProtocol').
python_method('TestShellProtocol', 'test_execute_simple_command', 0, 4, 2).
python_method('TestShellProtocol', 'test_execute_failing_command', 0, 3, 2).
python_class('tests/test_protocols.py', 'TestMCPProtocol').
python_method('TestMCPProtocol', 'test_register_tool', 0, 3, 3).
python_method('TestMCPProtocol', 'test_register_resource', 0, 3, 3).
python_method('TestMCPProtocol', 'test_execute_tool_not_implemented', 0, 3, 2).
python_class('tests/test_protocols.py', 'TestRESTProtocol').
python_method('TestRESTProtocol', 'test_rest_request_creation', 0, 4, 1).
python_method('TestRESTProtocol', 'test_execute_get_request', 0, 4, 4).
python_method('TestRESTProtocol', 'test_get_method', 0, 3, 2).
python_method('TestRESTProtocol', 'test_post_method', 0, 3, 2).
python_class('tests/test_protocols.py', 'TestWebSocketProtocol').
python_method('TestWebSocketProtocol', 'test_websocket_creation', 0, 3, 1).
python_method('TestWebSocketProtocol', 'test_connect_disconnect', 0, 5, 3).
python_method('TestWebSocketProtocol', 'test_send_message', 0, 2, 3).
python_method('TestWebSocketProtocol', 'test_receive_message', 0, 3, 3).

% ── Dependencies ─────────────────────────────────────────

% ── Makefile Targets ─────────────────────────────────────
makefile_target('install', 'Install dependencies').
makefile_target('dev', 'Install development dependencies').
makefile_target('test', 'Run tests').
makefile_target('test-cov', 'Run tests with coverage').
makefile_target('lint', 'Run linting').
makefile_target('type-check', 'Run type checking').
makefile_target('check', 'Run all checks').
makefile_target('clean', 'Clean build artifacts').
makefile_target('build', 'Build package').
makefile_target('publish', 'Publish to PyPI').
makefile_target('publish-test', 'Publish to test PyPI').
makefile_target('docs', 'Generate documentation').
makefile_target('dev-server', 'Run development server (if applicable)').
makefile_target('format', 'Format code').
makefile_target('fix', 'Fix linting issues').
makefile_target('llm-test', 'LLM testing targets').
makefile_target('llm-bench', '').
makefile_target('public-demo', '').
makefile_target('install-llm', '').

% ── Taskfile Tasks ───────────────────────────────────────

% ── Environment Variables ────────────────────────────────
env_variable('OPENAI_API_KEY', 'your_openai_api_key_here', 'OpenAI Configuration').
env_variable('OPENAI_BASE_URL', 'https://api.openai.com/v1', '').
env_variable('GRPC_HOST', 'localhost', 'gRPC Configuration').
env_variable('GRPC_PORT', '50051', '').
env_variable('MQTT_HOST', 'localhost', 'MQTT Configuration').
env_variable('MQTT_PORT', '1883', '').
env_variable('MQTT_USERNAME', '*(not set)*', '').
env_variable('MQTT_PASSWORD', '*(not set)*', '').
env_variable('MQTT_CLIENT_ID', 'propact_client', '').
env_variable('SMTP_HOST', 'smtp.gmail.com', 'SMTP Configuration').
env_variable('SMTP_PORT', '587', '').
env_variable('SMTP_USERNAME', 'your_email@gmail.com', '').
env_variable('SMTP_PASSWORD', 'your_app_password', '').
env_variable('SMTP_FROM', 'propact@example.com', '').
env_variable('WS_HOST', 'localhost', 'WebSocket Configuration').
env_variable('WS_PORT', '8080', '').
env_variable('SERVER_HOST', '0.0.0.0', 'Server Configuration').
env_variable('SERVER_PORT', '8080', '').
env_variable('MCP_HOST', 'localhost', 'MCP Configuration').
env_variable('MCP_PORT', '8080', '').
env_variable('LOG_LEVEL', 'INFO', 'Logging Configuration').
env_variable('LOG_FORMAT', '%(asctime)s - %(name)s - %(levelname)s - %(message)s', '').
env_variable('DEBUG', 'false', 'Development Configuration').
env_variable('TEST_MODE', 'false', '').
env_variable('DATA_DIR', './data', 'File Paths').
env_variable('CACHE_DIR', './cache', '').
env_variable('TEMP_DIR', './temp', '').
env_variable('REQUEST_TIMEOUT', '30', 'Timeout Configuration').
env_variable('WEBSOCKET_TIMEOUT', '60', '').
env_variable('GRPC_TIMEOUT', '30', '').
env_variable('RATE_LIMIT_REQUESTS', '100', 'Rate Limiting').
env_variable('RATE_LIMIT_WINDOW', '60', '').
env_variable('CORS_ORIGINS', '*', 'Security').
env_variable('API_KEY', '*(not set)*', '').

% ── TestQL Scenarios ─────────────────────────────────────
testql_scenario('generated-cli-tests.testql.toon.yaml', 'cli').
testql_scenario('generated-from-pytests.testql.toon.yaml', 'integration').

% ── Semantic Facts from SUMD.md ──────────────────────────
```

## Call Graph

*19 nodes · 15 edges · 10 modules · CC̄=3.5*

### Hubs (by degree)

| Function | CC | in | out | total |
|----------|----|----|-----|-------|
| `smart_send` *(in src.propact.core.ToonPact)* | 13 ⚠ | 0 | 32 | **32** |
| `send` *(in src.propact.adapters.MQTTAdapter)* | 7 | 0 | 17 | **17** |
| `run_example` *(in src.propact.testing.ExampleHelper)* | 12 ⚠ | 0 | 15 | **15** |
| `get_config` *(in src.propact.config)* | 2 | 9 | 1 | **10** |
| `_llm_self_correct_litellm` *(in src.propact.error_handler.PropactErrorHandler)* | 7 | 0 | 10 | **10** |
| `self_correct` *(in src.propact.llm_proxy)* | 3 | 1 | 9 | **10** |
| `__init__` *(in src.propact.adapters.EmailAdapter)* | 1 | 0 | 9 | **9** |
| `__init__` *(in examples.05-security-hardening.secure_handler.SecureMarkdownHandler)* | 1 | 0 | 6 | **6** |

```toon markpact:analysis path=project/calls.toon.yaml
# code2llm call graph | /home/tom/github/pactown-com/propact
# generated in 0.06s
# nodes: 19 | edges: 15 | modules: 10
# CC̄=3.5

HUBS[20]:
  src.propact.core.ToonPact.smart_send
    CC=13  in:0  out:32  total:32
  src.propact.adapters.MQTTAdapter.send
    CC=7  in:0  out:17  total:17
  src.propact.testing.ExampleHelper.run_example
    CC=12  in:0  out:15  total:15
  src.propact.config.get_config
    CC=2  in:9  out:1  total:10
  src.propact.error_handler.PropactErrorHandler._llm_self_correct_litellm
    CC=7  in:0  out:10  total:10
  src.propact.llm_proxy.self_correct
    CC=3  in:1  out:9  total:10
  src.propact.adapters.EmailAdapter.__init__
    CC=1  in:0  out:9  total:9
  examples.05-security-hardening.secure_handler.SecureMarkdownHandler.__init__
    CC=1  in:0  out:6  total:6
  src.propact.security.create_sanitizer
    CC=2  in:1  out:2  total:3
  src.propact.optimization.create_optimizer
    CC=1  in:1  out:2  total:3
  src.propact.config.get_smtp_config
    CC=1  in:2  out:1  total:3
  src.propact.config.get_server_config
    CC=1  in:1  out:1  total:2
  src.propact.config.get_mqtt_config
    CC=1  in:1  out:1  total:2
  src.propact.matcher.create_matcher
    CC=2  in:1  out:1  total:2
  src.propact.config.is_test_mode
    CC=1  in:0  out:1  total:1
  src.propact.config.get_openai_config
    CC=1  in:0  out:1  total:1
  src.propact.config.get_grpc_config
    CC=1  in:0  out:1  total:1
  src.propact.config.is_debug
    CC=1  in:0  out:1  total:1
  src.propact.config.get_websocket_config
    CC=1  in:0  out:1  total:1

MODULES:
  examples.05-security-hardening.secure_handler  [1 funcs]
    __init__  CC=1  out:6
  src.propact.adapters  [2 funcs]
    __init__  CC=1  out:9
    send  CC=7  out:17
  src.propact.config  [9 funcs]
    get_config  CC=2  out:1
    get_grpc_config  CC=1  out:1
    get_mqtt_config  CC=1  out:1
    get_openai_config  CC=1  out:1
    get_server_config  CC=1  out:1
    get_smtp_config  CC=1  out:1
    get_websocket_config  CC=1  out:1
    is_debug  CC=1  out:1
    is_test_mode  CC=1  out:1
  src.propact.core  [1 funcs]
    smart_send  CC=13  out:32
  src.propact.error_handler  [1 funcs]
    _llm_self_correct_litellm  CC=7  out:10
  src.propact.llm_proxy  [1 funcs]
    self_correct  CC=3  out:9
  src.propact.matcher  [1 funcs]
    create_matcher  CC=2  out:1
  src.propact.optimization  [1 funcs]
    create_optimizer  CC=1  out:2
  src.propact.security  [1 funcs]
    create_sanitizer  CC=2  out:2
  src.propact.testing  [1 funcs]
    run_example  CC=12  out:15

EDGES:
  examples.05-security-hardening.secure_handler.SecureMarkdownHandler.__init__ → src.propact.security.create_sanitizer
  examples.05-security-hardening.secure_handler.SecureMarkdownHandler.__init__ → src.propact.optimization.create_optimizer
  src.propact.config.get_openai_config → src.propact.config.get_config
  src.propact.config.get_grpc_config → src.propact.config.get_config
  src.propact.config.get_mqtt_config → src.propact.config.get_config
  src.propact.config.get_smtp_config → src.propact.config.get_config
  src.propact.config.get_websocket_config → src.propact.config.get_config
  src.propact.config.get_server_config → src.propact.config.get_config
  src.propact.config.is_debug → src.propact.config.get_config
  src.propact.config.is_test_mode → src.propact.config.get_config
  src.propact.adapters.MQTTAdapter.send → src.propact.config.get_mqtt_config
  src.propact.adapters.EmailAdapter.__init__ → src.propact.config.get_smtp_config
  src.propact.error_handler.PropactErrorHandler._llm_self_correct_litellm → src.propact.llm_proxy.self_correct
  src.propact.testing.ExampleHelper.run_example → src.propact.config.get_config
  src.propact.core.ToonPact.smart_send → src.propact.matcher.create_matcher
```

## Test Contracts

*Scenarios as contract signatures — what the system guarantees.*

### Cli (1)

**`CLI Command Tests`**

### Integration (1)

**`Auto-generated from Python Tests`**

## Intent


