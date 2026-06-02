"""Optional repatch-based HTML preprocessing adapter for propact."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence


class WebPatchDependencyError(RuntimeError):
    """Raised when optional webpatch dependencies are not installed."""


@dataclass
class WebPatchArtifacts:
    """Normalized outputs from HTML preprocessing for web patch workflows."""

    sanitized_html: str
    visual_css: str
    outline: str
    diagnostics: dict[str, Any]


def prepare_html_with_repatch(
    html: str,
    source_dir: Path,
    linked_css_paths: Sequence[str] | None = None,
) -> WebPatchArtifacts:
    """Prepare HTML artifacts using repatch web preprocess helpers."""
    try:
        from repatch.web_preprocess import (
            build_html_outline,
            extract_visual_css,
            sanitize_http_preview_html,
        )
    except ImportError as exc:
        raise WebPatchDependencyError(
            "repatch dependencies not installed. Install with: pip install propact[webpatch]"
        ) from exc

    css_paths = list(linked_css_paths or [])
    sanitized_html = sanitize_http_preview_html(html)
    visual_css = extract_visual_css(sanitized_html, css_paths, source_dir)
    outline = build_html_outline(sanitized_html)

    return WebPatchArtifacts(
        sanitized_html=sanitized_html,
        visual_css=visual_css,
        outline=outline,
        diagnostics={
            "adapter": "repatch",
            "source_dir": str(source_dir),
            "linked_css_count": len(css_paths),
        },
    )


def prepare_html_file_with_repatch(file_path: Path) -> WebPatchArtifacts:
    """Read an HTML file and return preprocessed artifacts."""
    html = file_path.read_text(encoding="utf-8")
    return prepare_html_with_repatch(html=html, source_dir=file_path.parent)
