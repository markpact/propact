"""Local development server for Propact with hot-reload, seeded test data, and OpenAPI /docs."""

import argparse
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import json
import logging
import os
from pathlib import Path
import re
import subprocess  # noqa: S404
import sys
import time
from typing import Any
from urllib.parse import parse_qs, urlparse

logger = logging.getLogger("propact.dev_server")

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
SEEDS_FILE_PATH = Path("seeds/test_data.json")


class SeedManager:
    """Manages seeded test data fixtures and in-memory mock store."""

    def __init__(self, seed_file: Path = SEEDS_FILE_PATH) -> None:
        self.seed_file = seed_file
        self.data: dict[str, Any] = {}
        self.load()

    def _default_seeds(self) -> dict[str, Any]:
        return {
            "users": [
                {
                    "id": "usr_001",
                    "name": "Alice Developer",
                    "email": "alice@propact.local",
                    "role": "admin",
                },
                {"id": "usr_002", "name": "Bob Tester", "email": "bob@propact.local", "role": "qa"},
                {
                    "id": "usr_003",
                    "name": "Charlie Guest",
                    "email": "charlie@propact.local",
                    "role": "viewer",
                },
            ],
            "pacts": [
                {
                    "id": "pact_rest_sample",
                    "name": "Sample REST Pact",
                    "protocol": "rest",
                    "content": (
                        "# Test REST Endpoint\n```propact:rest\nGET"
                        " http://localhost:8000/api/v1/users\n```"
                    ),
                },
                {
                    "id": "pact_shell_sample",
                    "name": "Sample Shell Pact",
                    "protocol": "shell",
                    "content": "# Test Shell Command\n```propact:shell\necho 'Propact Dev Ready'\n```",
                },
            ],
            "items": [
                {
                    "id": "item_1",
                    "title": "Protocol Pact Spec",
                    "category": "specification",
                    "active": True,
                },
                {"id": "item_2", "title": "DevX Hot-Reload", "category": "tooling", "active": True},
            ],
        }

    def load(self) -> None:
        if self.seed_file.exists():
            try:
                with open(self.seed_file, encoding="utf-8") as f:
                    self.data = json.load(f)
                return
            except Exception as err:
                logger.warning("Could not read seed file (%s). Falling back to defaults.", err)

        self.data = self._default_seeds()
        self.save()

    def save(self) -> None:
        self.seed_file.parent.mkdir(parents=True, exist_ok=True)
        with open(self.seed_file, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2)

    def reset(self) -> None:
        self.data = self._default_seeds()
        self.save()

    def get_summary(self) -> dict[str, Any]:
        return {
            "seed_file": str(self.seed_file),
            "collections": {k: len(v) if isinstance(v, list) else 1 for k, v in self.data.items()},
            "loaded_at": time.time(),
        }


SEEDS = SeedManager()
SERVER_START_TIME = time.time()


def get_openapi_spec(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> dict[str, Any]:
    """Build the OpenAPI 3.0 specification for the dev server."""
    return {
        "openapi": "3.0.3",
        "info": {
            "title": "Propact Local Dev API",
            "version": "0.0.9",
            "description": (
                "Interactive local development API for Propact with hot-reload, seeded test data,"
                " and Markdown pact execution."
            ),
        },
        "servers": [{"url": f"http://{host}:{port}", "description": "Local Dev Server"}],
        "paths": {
            "/api/health": {
                "get": {
                    "summary": "Health check",
                    "responses": {"200": {"description": "Server is healthy and operational"}},
                }
            },
            "/api/v1/seeds": {
                "get": {
                    "summary": "List seed collections",
                    "responses": {"200": {"description": "Summary of active test seeds"}},
                }
            },
            "/api/v1/seeds/reset": {
                "post": {
                    "summary": "Reset seeds to initial fixtures",
                    "responses": {"200": {"description": "Seeds reset successfully"}},
                }
            },
            "/api/v1/users": {
                "get": {
                    "summary": "Get seeded users",
                    "responses": {"200": {"description": "List of test users"}},
                },
                "post": {
                    "summary": "Create new test user",
                    "responses": {"201": {"description": "User created"}},
                },
            },
            "/api/v1/echo": {
                "post": {
                    "summary": "Echo payload",
                    "description": "Echoes back the received JSON request body for pact testing",
                    "responses": {"200": {"description": "Echo response"}},
                }
            },
            "/api/v1/pacts/execute": {
                "post": {
                    "summary": "Execute Markdown pact",
                    "description": "Parses and dry-runs markdown pact content",
                    "responses": {"200": {"description": "Execution result"}},
                }
            },
            "/openapi.json": {
                "get": {
                    "summary": "OpenAPI specification JSON",
                    "responses": {"200": {"description": "OpenAPI 3.0 schema"}},
                }
            },
            "/docs": {
                "get": {
                    "summary": "Interactive Swagger UI documentation",
                    "responses": {"200": {"description": "Swagger UI HTML page"}},
                }
            },
        },
    }


def render_swagger_ui_html() -> str:
    """Render Swagger UI HTML page pointed at /openapi.json."""
    return """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Propact Dev API - OpenAPI Docs</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui.css" />
  <style>
    body { margin: 0; background: #fafafa; font-family: sans-serif; }
    .topbar { display: none; }
    .banner { background: #111827; color: #f9fafb; padding: 12px 24px; display: flex; justify-content: space-between; align-items: center; }
    .banner h1 { margin: 0; font-size: 1.1rem; }
    .banner a { color: #60a5fa; text-decoration: none; font-size: 0.9rem; }
  </style>
</head>
<body>
  <div class="banner">
    <h1>🚀 Propact Local Dev Server</h1>
    <div>
      <a href="/openapi.json" target="_blank">OpenAPI JSON</a> &bull;
      <a href="/api/health" target="_blank">Health</a>
    </div>
  </div>
  <div id="swagger-ui"></div>
  <script src="https://cdn.jsdelivr.net/npm/swagger-ui-dist@5/swagger-ui-bundle.js"></script>
  <script>
    window.onload = function() {
      SwaggerUIBundle({
        url: '/openapi.json',
        dom_id: '#swagger-ui',
        deepLinking: true,
        presets: [
          SwaggerUIBundle.presets.apis,
          SwaggerUIBundle.SwaggerUIStandalonePreset
        ]
      });
    };
  </script>
</body>
</html>"""


class DevServerHandler(BaseHTTPRequestHandler):
    """HTTP handler with OpenAPI /docs, Swagger UI, seed management, and pact runner."""

    server_host: str = DEFAULT_HOST
    server_port: int = DEFAULT_PORT

    def _send_json(self, status: int, data: Any) -> None:
        body = json.dumps(data, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_html(self, status: int, html_text: str) -> None:
        body = html_text.encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _read_json_body(self) -> dict[str, Any]:
        try:
            content_length = int(self.headers.get("Content-Length", "0"))
            if content_length > 0:
                raw = self.rfile.read(content_length).decode("utf-8")
                return json.loads(raw) if raw else {}
        except Exception as err:
            logger.warning("Error reading JSON body: %s", err)
        return {}

    def do_GET(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/") or "/"

        if path in ("/", "/docs"):
            self._send_html(200, render_swagger_ui_html())
            return

        if path == "/openapi.json":
            self._send_json(200, get_openapi_spec(self.server_host, self.server_port))
            return

        if path == "/api/health":
            self._send_json(
                200,
                {
                    "status": "healthy",
                    "uptime_seconds": round(time.time() - SERVER_START_TIME, 2),
                    "seeds": SEEDS.get_summary(),
                },
            )
            return

        if path == "/api/v1/seeds":
            self._send_json(200, SEEDS.get_summary())
            return

        if path == "/api/v1/users":
            self._send_json(200, SEEDS.data.get("users", []))
            return

        match = re.match(r"^/api/v1/users/([^/]+)$", path)
        if match:
            user_id = match.group(1)
            for user in SEEDS.data.get("users", []):
                if user.get("id") == user_id:
                    self._send_json(200, user)
                    return
            self._send_json(404, {"error": f"User {user_id} not found"})
            return

        self._send_json(404, {"error": "Endpoint not found", "docs": "/docs"})

    def do_POST(self) -> None:  # noqa: N802
        parsed = urlparse(self.path)
        path = parsed.path.rstrip("/")
        body = self._read_json_body()

        if path == "/api/v1/seeds/reset":
            SEEDS.reset()
            self._send_json(200, {"message": "Seeds reset successfully", "seeds": SEEDS.get_summary()})
            return

        if path == "/api/v1/echo":
            self._send_json(200, {"echo": body, "timestamp": time.time()})
            return

        if path == "/api/v1/users":
            users = SEEDS.data.setdefault("users", [])
            new_user = {
                "id": body.get("id") or f"usr_{len(users) + 1:03d}",
                "name": body.get("name", "Unnamed Test User"),
                "email": body.get("email", "user@propact.local"),
                "role": body.get("role", "tester"),
            }
            users.append(new_user)
            SEEDS.save()
            self._send_json(201, new_user)
            return

        if path == "/api/v1/pacts/execute":
            pact_text = body.get("pact", "")
            blocks = re.findall(r"```propact:(\w+)\s+(.*?)\s+```", pact_text, flags=re.DOTALL)
            self._send_json(
                200,
                {
                    "success": True,
                    "dry_run": bool(body.get("dry_run", True)),
                    "detected_blocks": [{"protocol": proto, "content": blk.strip()} for proto, blk in blocks],
                },
            )
            return

        self._send_json(404, {"error": "Endpoint not found", "docs": "/docs"})

    def log_message(self, format_str: str, *args: Any) -> None:
        logger.info("%s - - [%s] " + format_str, self.address_string(), self.log_date_time_string(), *args)


class FileWatcher:
    """Monitors repository directories for modifications to trigger hot-reload."""

    def __init__(self, watch_paths: list[str]) -> None:
        self.watch_paths = [Path(p) for p in watch_paths]
        self.snapshot = self._take_snapshot()

    def _take_snapshot(self) -> dict[str, float]:
        snapshot: dict[str, float] = {}
        extensions = {".py", ".md", ".json", ".yaml", ".yml"}
        for base in self.watch_paths:
            if not base.exists():
                continue
            for root, _, files in os.walk(base):
                for file in files:
                    p = Path(root) / file
                    if p.suffix.lower() in extensions:
                        try:
                            snapshot[str(p)] = p.stat().st_mtime
                        except OSError:
                            pass
        return snapshot

    def has_changed(self) -> tuple[bool, str]:
        current = self._take_snapshot()
        for file_path, mtime in current.items():
            if file_path not in self.snapshot:
                self.snapshot = current
                return True, f"New file: {file_path}"
            if mtime > self.snapshot[file_path]:
                self.snapshot = current
                return True, f"Modified: {file_path}"
        return False, ""


def run_hot_reload_supervisor(host: str, port: int) -> None:
    """Supervises the worker process and restarts it upon file modifications."""
    cmd = [sys.executable, "-m", "propact.dev_server", "--host", host, "--port", str(port), "--worker"]
    watcher = FileWatcher(["src", "seeds", "examples"])
    logger.info("Starting Propact dev supervisor with hot-reload watching src/, seeds/, examples/...")
    proc = subprocess.Popen(cmd)  # noqa: S603

    try:
        while True:
            time.sleep(0.5)
            changed, reason = watcher.has_changed()
            if changed:
                logger.info("Hot-reload triggered (%s). Restarting server...", reason)
                proc.terminate()
                proc.wait()
                proc = subprocess.Popen(cmd)  # noqa: S603
    except KeyboardInterrupt:
        proc.terminate()
        proc.wait()


def main() -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
    parser = argparse.ArgumentParser(description="Propact Local Dev Server")
    parser.add_argument("--host", default=DEFAULT_HOST, help="Host address (default: 127.0.0.1)")
    parser.add_argument("--port", type=int, default=DEFAULT_PORT, help="Port (default: 8000)")
    parser.add_argument("--reload", action="store_true", help="Enable hot-reload watcher")
    parser.add_argument("--worker", action="store_true", help="Internal worker mode")
    parser.add_argument("--seed-only", action="store_true", help="Initialize seeds and exit")
    args = parser.parse_args()

    if args.seed_only:
        SEEDS.load()
        logger.info("✅ Seeds loaded: %s", SEEDS.get_summary())
        return

    if args.reload and not args.worker:
        run_hot_reload_supervisor(args.host, args.port)
        return

    DevServerHandler.server_host = args.host
    DevServerHandler.server_port = args.port
    server = ThreadingHTTPServer((args.host, args.port), DevServerHandler)
    logger.info("🚀 Propact Dev Server running at http://%s:%d/docs", args.host, args.port)
    logger.info("🌱 Seeded items loaded from %s", SEEDS.seed_file)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        logger.info("Shutting down dev server...")
        server.server_close()


if __name__ == "__main__":
    main()
