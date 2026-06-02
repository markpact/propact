# Propact 🚀 Protocol Pact via Markdown

SUMD - Structured Unified Markdown Descriptor for AI-aware project refactorization

## Contents

- [Metadata](#metadata)
- [Architecture](#architecture)
- [Workflows](#workflows)
- [Call Graph](#call-graph)
- [Test Contracts](#test-contracts)
- [Refactoring Analysis](#refactoring-analysis)
- [Intent](#intent)

## Metadata

- **name**: `propact`
- **version**: `0.0.0`
- **ecosystem**: SUMD + DOQL + testql + taskfile
- **generated_from**: pyproject.toml, Makefile, testql(2), app.doql.less, goal.yaml, .env.example, project/(6 analysis files)

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

## Workflows

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

## Refactoring Analysis

*Pre-refactoring snapshot — use this section to identify targets. Generated from `project/` toon files.*

### Call Graph & Complexity (`project/calls.toon.yaml`)

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

### Code Analysis (`project/analysis.toon.yaml`)

```toon markpact:analysis path=project/analysis.toon.yaml
# code2llm | 63f 11319L | python:27,shell:25,json:5,yaml:3,toml:1 | 2026-06-01
# generated in 0.03s
# CC̅=3.5 | critical:10/290 | dups:0 | cycles:0

HEALTH[11]:
  🔴 GOD   src/propact/dsl_converter.py = 811L, 8 classes, 30m, max CC=18
  🟡 CC    file CC=15 (limit:15)
  🟡 CC    universal CC=17 (limit:15)
  🟡 CC    _parse_md_table CC=15 (limit:15)
  🟡 CC    _create_md_table CC=15 (limit:15)
  🟡 CC    from_markdown CC=18 (limit:15)
  🟡 CC    send CC=16 (limit:15)
  🟡 CC    validate CC=16 (limit:15)
  🟡 CC    send_to_endpoint CC=18 (limit:15)
  🟡 CC    _send_rest CC=17 (limit:15)
  🟡 CC    _md_to_docx CC=23 (limit:15)

REFACTOR[2]:
  1. split src/propact/dsl_converter.py  (god module)
  2. split 10 high-CC methods  (CC>15)

PIPELINES[225]:
  [1] Src [__init__]: __init__
      PURITY: 100% pure
  [2] Src [handle_violation]: handle_violation
      PURITY: 100% pure
  [3] Src [get_report]: get_report
      PURITY: 100% pure
  [4] Src [__init__]: __init__ → create_sanitizer
      PURITY: 100% pure
  [5] Src [process]: process
      PURITY: 100% pure
  [6] Src [get_security_report]: get_security_report
      PURITY: 100% pure
  [7] Src [demo_security]: demo_security
      PURITY: 100% pure
  [8] Src [__init__]: __init__
      PURITY: 100% pure
  [9] Src [_find_env_file]: _find_env_file
      PURITY: 100% pure
  [10] Src [_load_env]: _load_env
      PURITY: 100% pure
  [11] Src [_get_env_bool]: _get_env_bool
      PURITY: 100% pure
  [12] Src [_get_env_int]: _get_env_int
      PURITY: 100% pure
  [13] Src [_get_env_path]: _get_env_path
      PURITY: 100% pure
  [14] Src [_load_config]: _load_config
      PURITY: 100% pure
  [15] Src [reload]: reload
      PURITY: 100% pure
  [16] Src [init_config]: init_config
      PURITY: 100% pure
  [17] Src [reload_config]: reload_config
      PURITY: 100% pure
  [18] Src [get_openai_config]: get_openai_config → get_config
      PURITY: 100% pure
  [19] Src [get_grpc_config]: get_grpc_config → get_config
      PURITY: 100% pure
  [20] Src [get_websocket_config]: get_websocket_config → get_config
      PURITY: 100% pure
  [21] Src [is_debug]: is_debug → get_config
      PURITY: 100% pure
  [22] Src [is_test_mode]: is_test_mode → get_config
      PURITY: 100% pure
  [23] Src [cli]: cli
      PURITY: 100% pure
  [24] Src [main]: main → get_server_config → get_config
      PURITY: 100% pure
  [25] Src [convert]: convert
      PURITY: 100% pure
  [26] Src [file]: file
      PURITY: 100% pure
  [27] Src [string]: string
      PURITY: 100% pure
  [28] Src [formats]: formats
      PURITY: 100% pure
  [29] Src [universal]: universal
      PURITY: 100% pure
  [30] Src [send_email]: send_email
      PURITY: 100% pure
  [31] Src [batch]: batch
      PURITY: 100% pure
  [32] Src [import_browser_spec]: import_browser_spec
      PURITY: 100% pure
  [33] Src [is_llm_enhanced]: is_llm_enhanced
      PURITY: 100% pure
  [34] Src [extract_llm_descriptions]: extract_llm_descriptions
      PURITY: 100% pure
  [35] Src [__init__]: __init__
      PURITY: 100% pure
  [36] Src [_parse_md_table]: _parse_md_table
      PURITY: 100% pure
  [37] Src [_create_md_table]: _create_md_table
      PURITY: 100% pure
  [38] Src [__init__]: __init__
      PURITY: 100% pure
  [39] Src [to_markdown]: to_markdown
      PURITY: 100% pure
  [40] Src [from_markdown]: from_markdown
      PURITY: 100% pure
  [41] Src [_mock_sql_result]: _mock_sql_result
      PURITY: 100% pure
  [42] Src [to_markdown]: to_markdown
      PURITY: 100% pure
  [43] Src [from_markdown]: from_markdown
      PURITY: 100% pure
  [44] Src [_extract_structured_data]: _extract_structured_data
      PURITY: 100% pure
  [45] Src [_generate_github_query]: _generate_github_query
      PURITY: 100% pure
  [46] Src [to_markdown]: to_markdown
      PURITY: 100% pure
  [47] Src [from_markdown]: from_markdown
      PURITY: 100% pure
  [48] Src [_dict_to_markdown]: _dict_to_markdown
      PURITY: 100% pure
  [49] Src [_list_to_markdown]: _list_to_markdown
      PURITY: 100% pure
  [50] Src [_markdown_to_dict]: _markdown_to_dict
      PURITY: 100% pure

LAYERS:
  src/                            CC̄=3.8    ←in:0  →out:0
  │ !! dsl_converter              811L  8C   30m  CC=18     ←0
  │ !! uniconverter               759L  3C   17m  CC=23     ←0
  │ !! cli                        666L  0C   11m  CC=17     ←0
  │ matcher                    444L  2C   14m  CC=10     ←1
  │ !! enhanced                   416L  2C   16m  CC=18     ←0
  │ !! validation                 414L  4C   11m  CC=16     ←0
  │ converter                  375L  3C   15m  CC=13     ←0
  │ !! adapters                   366L  6C   17m  CC=16     ←1
  │ config                     364L  12C   19m  CC=3      ←3
  │ error_handler              361L  3C   15m  CC=14     ←0
  │ optimization               361L  3C   13m  CC=9      ←1
  │ llm_proxy                  278L  2C   10m  CC=8      ←1
  │ security                   263L  2C   10m  CC=13     ←1
  │ core                       236L  1C    8m  CC=13     ←0
  │ testing                    201L  1C    7m  CC=12     ←0
  │ query_gen                  201L  1C    8m  CC=2      ←0
  │ ws                         149L  3C    7m  CC=3      ←0
  │ rest                       127L  4C    6m  CC=4      ←0
  │ importer                   115L  1C    4m  CC=8      ←0
  │ mcp                        110L  2C    7m  CC=1      ←0
  │ parser                     100L  3C    5m  CC=4      ←0
  │ attachments                 93L  1C    7m  CC=6      ←0
  │ shell                       74L  1C    3m  CC=6      ←0
  │ constants                   62L  0C    0m  CC=0.0    ←0
  │ __init__                    29L  0C    0m  CC=0.0    ←0
  │ __init__                     8L  0C    0m  CC=0.0    ←0
  │
  examples/                       CC̄=0.8    ←in:0  →out:0
  │ run-all.sh                 371L  0C   11m  CC=0.0    ←0
  │ secure_handler             254L  2C    7m  CC=9      ←0
  │ Makefile                   203L  0C    0m  CC=0.0    ←0
  │ slack-openapi.json          78L  0C    0m  CC=0.0    ←0
  │ notion-openapi.json         78L  0C    0m  CC=0.0    ←0
  │ openapi.json                57L  0C    0m  CC=0.0    ←0
  │ run.sh                      51L  0C    0m  CC=0.0    ←0
  │ demo-public.sh              49L  0C    0m  CC=0.0    ←0
  │ run.sh                      47L  0C    1m  CC=0.0    ←0
  │ run.sh                      46L  0C    1m  CC=0.0    ←0
  │ run.sh                      46L  0C    1m  CC=0.0    ←0
  │ run.sh                      46L  0C    1m  CC=0.0    ←0
  │ run.sh                      46L  0C    1m  CC=0.0    ←0
  │ run.sh                      45L  0C    1m  CC=0.0    ←0
  │ run.sh                      42L  0C    1m  CC=0.0    ←0
  │ run.sh                      42L  0C    1m  CC=0.0    ←0
  │ run.sh                      42L  0C    1m  CC=0.0    ←0
  │ run-new-examples.sh         41L  0C    0m  CC=0.0    ←0
  │ run.sh                      40L  0C    0m  CC=0.0    ←0
  │ run.sh                      40L  0C    0m  CC=0.0    ←0
  │ run.sh                      40L  0C    0m  CC=0.0    ←0
  │ run.sh                      39L  0C    0m  CC=0.0    ←0
  │ ecommerce-api.json          39L  0C    0m  CC=0.0    ←0
  │ run.sh                      37L  0C    0m  CC=0.0    ←0
  │ run.sh                      37L  0C    0m  CC=0.0    ←0
  │ run.sh                      37L  0C    0m  CC=0.0    ←0
  │ run.sh                      36L  0C    0m  CC=0.0    ←0
  │
  ./                              CC̄=0.0    ←in:0  →out:0
  │ !! planfile.yaml              864L  0C    0m  CC=0.0    ←0
  │ !! goal.yaml                  512L  0C    0m  CC=0.0    ←0
  │ verify_examples.sh         116L  0C    1m  CC=0.0    ←0
  │ pyproject.toml             103L  0C    0m  CC=0.0    ←0
  │ test_examples_final.sh     100L  0C    1m  CC=0.0    ←0
  │ test_all_examples.sh        94L  0C    1m  CC=0.0    ←0
  │ Makefile                    85L  0C    0m  CC=0.0    ←0
  │ prefact.yaml                78L  0C    0m  CC=0.0    ←0
  │ project.sh                  50L  0C    0m  CC=0.0    ←0
  │ sample_data.json             5L  0C    0m  CC=0.0    ←0
  │

COUPLING:
                                  examples.05-security-hardening                     src.propact
  examples.05-security-hardening                              ──                               2
                     src.propact                              ←2                              ──
  CYCLES: none

EXTERNAL:
  validation: run `vallm batch .` → validation.toon
  duplication: run `redup scan .` → duplication.toon
```

### Duplication (`project/duplication.toon.yaml`)

```toon markpact:analysis path=project/duplication.toon.yaml
# redup/duplication | 4 groups | 26f 7436L | 2026-06-01

SUMMARY:
  files_scanned: 26
  total_lines:   7436
  dup_groups:    4
  dup_fragments: 14
  saved_lines:   41
  scan_ms:       2930

HOTSPOTS[4] (files with most duplication):
  src/propact/dsl_converter.py  dup=27L  groups=2  frags=3  (0.4%)
  src/propact/config.py  dup=24L  groups=1  frags=8  (0.3%)
  src/propact/uniconverter.py  dup=7L  groups=1  frags=1  (0.1%)
  src/propact/cli.py  dup=6L  groups=1  frags=2  (0.1%)

DUPLICATES[4] (ranked by impact):
  [ab5b16619a4fdd19]   STRU  get_openai_config  L=3 N=8 saved=21 sim=1.00
      src/propact/config.py:327-329  (get_openai_config)
      src/propact/config.py:332-334  (get_grpc_config)
      src/propact/config.py:337-339  (get_mqtt_config)
      src/propact/config.py:342-344  (get_smtp_config)
      src/propact/config.py:347-349  (get_websocket_config)
      src/propact/config.py:352-354  (get_server_config)
      src/propact/config.py:357-359  (is_debug)
      src/propact/config.py:362-364  (is_test_mode)
  [5dc94afc7b2e31b2]   EXAC  _markdown_to_dict  L=10 N=2 saved=10 sim=1.00
      src/propact/dsl_converter.py:529-538  (_markdown_to_dict)
      src/propact/dsl_converter.py:692-701  (_markdown_to_dict)
  [a0695bd2a771bfa7]   EXAC  __post_init__  L=7 N=2 saved=7 sim=1.00
      src/propact/dsl_converter.py:53-59  (__post_init__)
      src/propact/uniconverter.py:73-79  (__post_init__)
  [aaae754bdb04529d]   STRU  cli  L=3 N=2 saved=3 sim=1.00
      src/propact/cli.py:27-29  (cli)
      src/propact/cli.py:349-351  (convert)

REFACTOR[4] (ranked by priority):
  [1] ○ extract_function   → src/propact/utils/get_openai_config.py
      WHY: 8 occurrences of 3-line block across 1 files — saves 21 lines
      FILES: src/propact/config.py
  [2] ○ extract_function   → src/propact/utils/_markdown_to_dict.py
      WHY: 2 occurrences of 10-line block across 1 files — saves 10 lines
      FILES: src/propact/dsl_converter.py
  [3] ○ extract_class      → src/propact/utils/__post_init__.py
      WHY: 2 occurrences of 7-line block across 2 files — saves 7 lines
      FILES: src/propact/dsl_converter.py, src/propact/uniconverter.py
  [4] ○ extract_function   → src/propact/utils/cli.py
      WHY: 2 occurrences of 3-line block across 1 files — saves 3 lines
      FILES: src/propact/cli.py

QUICK_WINS[3] (low risk, high savings — do first):
  [1] extract_function   saved=21L  → src/propact/utils/get_openai_config.py
      FILES: config.py
  [2] extract_function   saved=10L  → src/propact/utils/_markdown_to_dict.py
      FILES: dsl_converter.py
  [3] extract_class      saved=7L  → src/propact/utils/__post_init__.py
      FILES: dsl_converter.py, uniconverter.py

EFFORT_ESTIMATE (total ≈ 1.4h):
  medium get_openai_config                   saved=21L  ~42min
  easy   _markdown_to_dict                   saved=10L  ~20min
  easy   __post_init__                       saved=7L  ~14min
  easy   cli                                 saved=3L  ~6min

METRICS-TARGET:
  dup_groups:  4 → 0
  saved_lines: 41 lines recoverable
```

### Evolution / Churn (`project/evolution.toon.yaml`)

```toon markpact:analysis path=project/evolution.toon.yaml
# code2llm/evolution | 263 func | 26f | 2026-06-01
# generated in 0.00s

NEXT[10] (ranked by impact):
  [1] !! SPLIT           src/propact/uniconverter.py
      WHY: 759L, 3 classes, max CC=23
      EFFORT: ~4h  IMPACT: 17457

  [2] !! SPLIT           src/propact/dsl_converter.py
      WHY: 811L, 8 classes, max CC=18
      EFFORT: ~4h  IMPACT: 14598

  [3] !  SPLIT-FUNC      UniConverter._md_to_docx  CC=23  fan=19
      WHY: CC=23 exceeds 15
      EFFORT: ~1h  IMPACT: 437

  [4] !  SPLIT-FUNC      EmailAdapter.send  CC=16  fan=22
      WHY: CC=16 exceeds 15
      EFFORT: ~1h  IMPACT: 352

  [5] !  SPLIT-FUNC      SQLConverter.from_markdown  CC=18  fan=16
      WHY: CC=18 exceeds 15
      EFFORT: ~1h  IMPACT: 288

  [6] !  SPLIT-FUNC      ValidationPipeline.validate  CC=16  fan=17
      WHY: CC=16 exceeds 15
      EFFORT: ~1h  IMPACT: 272

  [7] !  SPLIT-FUNC      Propact.send_to_endpoint  CC=18  fan=15
      WHY: CC=18 exceeds 15
      EFFORT: ~1h  IMPACT: 270

  [8] !  SPLIT-FUNC      Propact._send_rest  CC=17  fan=15
      WHY: CC=17 exceeds 15
      EFFORT: ~1h  IMPACT: 255

  [9] !  SPLIT-FUNC      universal  CC=17  fan=11
      WHY: CC=17 exceeds 15
      EFFORT: ~1h  IMPACT: 187

  [10] !  SPLIT-FUNC      file  CC=15  fan=12
      WHY: CC=15 exceeds 15
      EFFORT: ~1h  IMPACT: 180


RISKS[3]:
  ⚠ Splitting planfile.yaml may break 0 import paths
  ⚠ Splitting src/propact/dsl_converter.py may break 30 import paths
  ⚠ Splitting src/propact/uniconverter.py may break 17 import paths

METRICS-TARGET:
  CC̄:          3.8 → ≤2.7
  max-CC:      23 → ≤11
  god-modules: 5 → 0
  high-CC(≥15): 10 → ≤5
  hub-types:   0 → ≤0

PATTERNS (language parser shared logic):
  _extract_declarations() in base.py — unified extraction for:
    - TypeScript: interfaces, types, classes, functions, arrow funcs
    - PHP: namespaces, traits, classes, functions, includes
    - Ruby: modules, classes, methods, requires
    - C++: classes, structs, functions, #includes
    - C#: classes, interfaces, methods, usings
    - Java: classes, interfaces, methods, imports
    - Go: packages, functions, structs
    - Rust: modules, functions, traits, use statements

  Shared regex patterns per language:
    - import: language-specific import/require/using patterns
    - class: class/struct/trait declarations with inheritance
    - function: function/method signatures with visibility
    - brace_tracking: for C-family languages ({ })
    - end_keyword_tracking: for Ruby (module/class/def...end)

  Benefits:
    - Consistent extraction logic across all languages
    - Reduced code duplication (~70% reduction in parser LOC)
    - Easier maintenance: fix once, apply everywhere
    - Standardized FunctionInfo/ClassInfo models

HISTORY:
  prev CC̄=3.8 → now CC̄=3.8
```

### Validation (`project/validation.toon.yaml`)

```toon markpact:analysis path=project/validation.toon.yaml
# vallm batch | 167f | 0✓ 74⚠ 0✗ | 2026-06-01

SUMMARY:
  scanned: 167  passed: 0 (0.0%)  warnings: 74  errors: 0  unsupported: 0

WARNINGS[74]{path,score}:
  src/propact/cli.py,0.68
    issues[4]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
      complexity.lizard_cc,warning,main.run: CC=35 exceeds limit 15,139
      complexity.lizard_length,warning,main.run: 107 lines exceeds limit 100,139
      complexity.lizard_cc,warning,universal: CC=17 exceeds limit 15,512
  src/propact/enhanced.py,0.71
    issues[3]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
      complexity.lizard_cc,warning,send_to_endpoint: CC=18 exceeds limit 15,171
      complexity.lizard_cc,warning,_send_rest: CC=17 exceeds limit 15,261
  src/propact/adapters.py,0.74
    issues[2]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
      complexity.lizard_cc,warning,send: CC=16 exceeds limit 15,282
  src/propact/dsl_converter.py,0.74
    issues[2]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
      complexity.lizard_cc,warning,from_markdown: CC=18 exceeds limit 15,211
  src/propact/uniconverter.py,0.74
    issues[2]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
      complexity.lizard_cc,warning,_md_to_docx: CC=23 exceeds limit 15,537
  src/propact/validation.py,0.74
    issues[2]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
      complexity.lizard_cc,warning,validate: CC=16 exceeds limit 15,201
  examples/01-shell-upload/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/02-openapi-rest/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/03-mcp-tool/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/04-ws-chat/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/05-md-server/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/05-security-hardening/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/05-security-hardening/secure_handler.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  examples/06-openai-vision/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/07-ffmpeg-cli/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/08-grpc-inference/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/09-imgur/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/10-slack/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/10-slack/slack-openapi.json,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse JSON: Download error: Language 'JSON' not available for download. Available groups: [""all""]",
  examples/11-discord/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/12-openai-vision/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/13-github-gist/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/14-stripe/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/15-youtube/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/16-notion/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/17-twitter/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/18-todo-api/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/19-users-api/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/20-posts-api/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/21-albums-api/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/22-comments-api/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/23-photos-api/run.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/error-demo/ecommerce-api.json,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse JSON: Download error: Language 'JSON' not available for download. Available groups: [""all""]",
  examples/openapi-llm-demo/notion-openapi.json,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse JSON: Download error: Language 'JSON' not available for download. Available groups: [""all""]",
  examples/public-apis/demo-public.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/run-all.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/run-new-examples.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  examples/smart-test/openapi.json,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse JSON: Download error: Language 'JSON' not available for download. Available groups: [""all""]",
  examples/smart-test/test_matcher.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  goal.yaml,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse YAML: Download error: Language 'YAML' not available for download. Available groups: [""all""]",
  planfile.yaml,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse YAML: Download error: Language 'YAML' not available for download. Available groups: [""all""]",
  prefact.yaml,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse YAML: Download error: Language 'YAML' not available for download. Available groups: [""all""]",
  project.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  project/calls.yaml,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse YAML: Download error: Language 'YAML' not available for download. Available groups: [""all""]",
  project/planfile-tickets.yaml,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse YAML: Download error: Language 'YAML' not available for download. Available groups: [""all""]",
  pyproject.toml,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse TOML: Download error: Language 'TOML' not available for download. Available groups: [""all""]",
  sample_data.json,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse JSON: Download error: Language 'JSON' not available for download. Available groups: [""all""]",
  src/propact/__init__.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/attachments.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/config.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/constants.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/converter.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/core.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/error_handler.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/importer.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/llm_proxy.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/matcher.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/optimization.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/parser.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/protocols/__init__.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/protocols/mcp.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/protocols/rest.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/protocols/shell.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/protocols/ws.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/query_gen.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/security.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  src/propact/testing.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  test_all_examples.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  test_examples_final.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
  tests/__init__.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  tests/test_core.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  tests/test_error_handler.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  tests/test_protocols.py,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse PYTHON: Download error: Language 'PYTHON' not available for download. Available groups: [""all""]",
  verify_examples.sh,0.78
    issues[1]{rule,severity,message,line}:
      syntax.unsupported,warning,"Could not parse BASH: Download error: Language 'BASH' not available for download. Available groups: [""all""]",
```

## Intent


