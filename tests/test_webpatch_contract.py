"""Contract tests for optional webpatch integration boundaries."""

from __future__ import annotations

from pathlib import Path

from propact.webpatch import WebPatchArtifacts


def test_webpatch_artifacts_contract_shape() -> None:
    """Adapter result should keep a stable, explicit artifact contract."""
    artifacts = WebPatchArtifacts(
        sanitized_html="<html><body>ok</body></html>",
        visual_css="body { color: black; }",
        outline="<ol><li>body</li></ol>",
        diagnostics={"adapter": "repatch"},
    )

    assert isinstance(artifacts.sanitized_html, str)
    assert isinstance(artifacts.visual_css, str)
    assert isinstance(artifacts.outline, str)
    assert isinstance(artifacts.diagnostics, dict)
    assert set(vars(artifacts)) == {"sanitized_html", "visual_css", "outline", "diagnostics"}


def test_repatch_dependency_is_isolated_to_webpatch_module() -> None:
    """Only webpatch adapter may import repatch directly."""
    src_root = Path(__file__).resolve().parents[1] / "src" / "propact"
    offenders: list[str] = []

    for path in src_root.glob("*.py"):
        if path.name == "webpatch.py":
            continue
        text = path.read_text(encoding="utf-8")
        if "import repatch" in text or "from repatch" in text:
            offenders.append(path.name)

    assert offenders == []
