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
sumd_declared_file('app.doql.less', 'doql').
sumd_declared_file('testql-scenarios/generated-cli-tests.testql.toon.yaml', 'testql').
sumd_declared_file('testql-scenarios/generated-from-pytests.testql.toon.yaml', 'testql').
sumd_declared_file('project/map.toon.yaml', 'analysis').
sumd_declared_file('project/logic.pl', 'analysis').
sumd_declared_file('project/calls.toon.yaml', 'analysis').
sumd_workflow('install', 'manual').
sumd_workflow_step('install', 1, 'poetry install').
sumd_workflow('dev', 'manual').
sumd_workflow_step('dev', 1, 'poetry install --with dev').
sumd_workflow('test', 'manual').
sumd_workflow_step('test', 1, 'poetry run pytest -vv').
sumd_workflow('test-cov', 'manual').
sumd_workflow_step('test-cov', 1, 'poetry run pytest --cov=propact --cov-report=html --cov-report=term').
sumd_workflow('lint', 'manual').
sumd_workflow_step('lint', 1, 'poetry run ruff check src/ tests/').
sumd_workflow_step('lint', 2, 'poetry run ruff format src/ tests/').
sumd_workflow('type-check', 'manual').
sumd_workflow_step('type-check', 1, 'poetry run mypy src/').
sumd_workflow('check', 'manual').
sumd_workflow('clean', 'manual').
sumd_workflow_step('clean', 1, 'rm -rf dist/').
sumd_workflow_step('clean', 2, 'rm -rf *.egg-info/').
sumd_workflow_step('clean', 3, 'rm -rf .pytest_cache/').
sumd_workflow_step('clean', 4, 'rm -rf .coverage').
sumd_workflow_step('clean', 5, 'rm -rf htmlcov/').
sumd_workflow('build', 'manual').
sumd_workflow_step('build', 1, 'poetry build').
sumd_workflow('publish', 'manual').
sumd_workflow_step('publish', 1, 'poetry publish').
sumd_workflow('publish-test', 'manual').
sumd_workflow_step('publish-test', 1, 'poetry publish --repository testpypi').
sumd_workflow('docs', 'manual').
sumd_workflow_step('docs', 1, 'echo "Documentation generation not yet implemented"').
sumd_workflow('dev-server', 'manual').
sumd_workflow_step('dev-server', 1, 'echo "No development server available"').
sumd_workflow('format', 'manual').
sumd_workflow_step('format', 1, 'poetry run ruff format src/ tests/').
sumd_workflow('fix', 'manual').
sumd_workflow_step('fix', 1, 'poetry run ruff check --fix src/ tests/').
sumd_workflow('llm-test', 'manual').
sumd_workflow_step('llm-test', 1, 'poetry run python -c "from propact.llm_proxy import LiteLLMProxy').
sumd_workflow_step('llm-test', 2, 'poetry run propact --help | grep -q llm-provider && echo "CLI LLM flags OK"').
sumd_workflow_step('llm-test', 3, 'echo "✅ LiteLLM multi-provider configuration OK!"').
sumd_workflow('llm-bench', 'manual').
sumd_workflow_step('llm-bench', 1, 'echo "Benchmarking LLM providers..."').
sumd_workflow_step('llm-bench', 2, 'poetry run python -c "import asyncio').
sumd_workflow_step('llm-bench', 3, 'echo "✅ LLM benchmark complete"').
sumd_workflow('public-demo', 'manual').
sumd_workflow_step('public-demo', 1, 'echo "🚀 Running public APIs demo..."').
sumd_workflow_step('public-demo', 2, 'cd examples/public-apis && ./demo-public.sh').
sumd_workflow('install-llm', 'manual').
sumd_workflow_step('install-llm', 1, 'poetry install --extras llm').

