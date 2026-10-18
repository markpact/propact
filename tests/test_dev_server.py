from http.server import ThreadingHTTPServer
import json
from pathlib import Path
import threading
import time
import urllib.request

import pytest

from propact.dev_server import (
    DevServerHandler,
    FileWatcher,
    SeedManager,
    get_openapi_spec,
    render_swagger_ui_html,
)


def test_seed_manager_initialization(tmp_path: Path) -> None:
    seed_file = tmp_path / "seeds.json"
    manager = SeedManager(seed_file=seed_file)
    summary = manager.get_summary()

    assert "users" in manager.data
    assert len(manager.data["users"]) >= 3
    assert summary["collections"]["users"] >= 3
    assert seed_file.exists()

    manager.reset()
    assert len(manager.data["users"]) >= 3


def test_openapi_spec_structure() -> None:
    spec = get_openapi_spec("127.0.0.1", 8000)
    assert spec["openapi"] == "3.0.3"
    assert "/docs" in spec["paths"]
    assert "/openapi.json" in spec["paths"]
    assert "/api/health" in spec["paths"]
    assert "/api/v1/seeds" in spec["paths"]
    assert "/api/v1/users" in spec["paths"]
    assert "/api/v1/pacts/execute" in spec["paths"]


def test_render_swagger_ui_html() -> None:
    html = render_swagger_ui_html()
    assert "SwaggerUIBundle" in html
    assert "/openapi.json" in html


def test_file_watcher_detects_changes(tmp_path: Path) -> None:
    watch_dir = tmp_path / "watch_me"
    watch_dir.mkdir()
    test_file = watch_dir / "sample.py"
    test_file.write_text("x = 1\n", encoding="utf-8")

    watcher = FileWatcher([str(watch_dir)])
    changed, _ = watcher.has_changed()
    assert not changed

    time.sleep(0.05)
    test_file.write_text("x = 2\n", encoding="utf-8")
    changed, reason = watcher.has_changed()
    assert changed
    assert "Modified" in reason


@pytest.fixture
def running_dev_server(tmp_path: Path) -> tuple[str, int]:
    DevServerHandler.server_host = "127.0.0.1"
    server = ThreadingHTTPServer(("127.0.0.1", 0), DevServerHandler)
    port = server.server_port
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    time.sleep(0.05)
    yield "127.0.0.1", port
    server.shutdown()
    server.server_close()


def test_dev_server_endpoints(running_dev_server: tuple[str, int]) -> None:
    host, port = running_dev_server
    base = f"http://{host}:{port}"

    # Test /docs HTML
    with urllib.request.urlopen(f"{base}/docs") as resp:
        assert resp.status == 200
        content = resp.read().decode("utf-8")
        assert "SwaggerUIBundle" in content

    # Test /openapi.json
    with urllib.request.urlopen(f"{base}/openapi.json") as resp:
        assert resp.status == 200
        data = json.loads(resp.read().decode("utf-8"))
        assert data["openapi"] == "3.0.3"

    # Test /api/health
    with urllib.request.urlopen(f"{base}/api/health") as resp:
        assert resp.status == 200
        data = json.loads(resp.read().decode("utf-8"))
        assert data["status"] == "healthy"

    # Test /api/v1/users
    with urllib.request.urlopen(f"{base}/api/v1/users") as resp:
        assert resp.status == 200
        users = json.loads(resp.read().decode("utf-8"))
        assert len(users) >= 3

    # Test /api/v1/pacts/execute
    req = urllib.request.Request(
        f"{base}/api/v1/pacts/execute",
        data=json.dumps({"pact": "# Test\n```propact:shell\necho 1\n```"}).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req) as resp:
        assert resp.status == 200
        result = json.loads(resp.read().decode("utf-8"))
        assert result["success"] is True
        assert len(result["detected_blocks"]) == 1
        assert result["detected_blocks"][0]["protocol"] == "shell"
