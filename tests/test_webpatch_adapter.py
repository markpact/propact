"""Tests for optional repatch web preprocess adapter."""

from __future__ import annotations

import builtins
import sys
import types
from pathlib import Path

import pytest

from propact.webpatch import (
    WebPatchDependencyError,
    prepare_html_file_with_repatch,
    prepare_html_with_repatch,
)


def test_prepare_html_with_repatch_requires_optional_dependency(monkeypatch: pytest.MonkeyPatch) -> None:
    """Adapter should raise a clear error when repatch is missing."""
    original_import = builtins.__import__

    def _fake_import(name, globals=None, locals=None, fromlist=(), level=0):
        if name.startswith("repatch"):
            raise ImportError("No module named 'repatch'")
        return original_import(name, globals, locals, fromlist, level)

    monkeypatch.setattr(builtins, "__import__", _fake_import)

    with pytest.raises(WebPatchDependencyError, match=r"propact\[webpatch\]"):
        prepare_html_with_repatch("<html></html>", Path("."))


def test_prepare_html_with_repatch_returns_contract(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """Adapter should return normalized artifacts when repatch helpers are available."""
    repatch_module = types.ModuleType("repatch")
    web_preprocess_module = types.ModuleType("repatch.web_preprocess")

    def _sanitize_http_preview_html(html: str) -> str:
        return html.replace("<script>", "").replace("</script>", "")

    def _extract_visual_css(html: str, linked_css_paths: list[str], source_dir: Path) -> str:
        _ = html
        _ = linked_css_paths
        _ = source_dir
        return "body { color: red; }"

    def _build_html_outline(html: str) -> str:
        _ = html
        return "<ol><li>body</li></ol>"

    web_preprocess_module.sanitize_http_preview_html = _sanitize_http_preview_html
    web_preprocess_module.extract_visual_css = _extract_visual_css
    web_preprocess_module.build_html_outline = _build_html_outline

    monkeypatch.setitem(sys.modules, "repatch", repatch_module)
    monkeypatch.setitem(sys.modules, "repatch.web_preprocess", web_preprocess_module)

    artifacts = prepare_html_with_repatch(
        html="<html><body><script>alert(1)</script><h1>Hello</h1></body></html>",
        source_dir=tmp_path,
    )

    assert "<script>" not in artifacts.sanitized_html
    assert artifacts.visual_css == "body { color: red; }"
    assert artifacts.outline == "<ol><li>body</li></ol>"
    assert artifacts.diagnostics["adapter"] == "repatch"
    assert artifacts.diagnostics["source_dir"] == str(tmp_path)


def test_prepare_html_file_with_repatch_reads_file(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    """File helper should read HTML and delegate to adapter function."""
    html_file = tmp_path / "page.html"
    html_file.write_text("<html><body><h1>Hello</h1></body></html>", encoding="utf-8")

    repatch_module = types.ModuleType("repatch")
    web_preprocess_module = types.ModuleType("repatch.web_preprocess")
    web_preprocess_module.sanitize_http_preview_html = lambda html: html
    web_preprocess_module.extract_visual_css = lambda html, linked_css_paths, source_dir: ""
    web_preprocess_module.build_html_outline = lambda html: "outline"

    monkeypatch.setitem(sys.modules, "repatch", repatch_module)
    monkeypatch.setitem(sys.modules, "repatch.web_preprocess", web_preprocess_module)

    artifacts = prepare_html_file_with_repatch(html_file)
    assert artifacts.sanitized_html.startswith("<html>")
    assert artifacts.outline == "outline"
