"""YAML converter for bidirectional YAML ↔ Markdown conversion."""

import re
from typing import Dict, Any, List

from .base import BaseConverter, ConversionResult

# Try to import optional dependency
try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class YAMLConverter(BaseConverter):
    """Converter for YAML ↔ Markdown."""
    
    def to_markdown(self, content: str, **kwargs) -> ConversionResult:
        """Convert YAML to Markdown."""
        try:
            if not HAS_YAML:
                return ConversionResult(
                    success=False,
                    content="",
                    format="markdown",
                    errors=["PyYAML is required for YAML conversion"]
                )
            
            # Parse YAML
            data = yaml.safe_load(content)
            
            # Convert to markdown
            if isinstance(data, dict):
                md_content = self._dict_to_markdown(data)
            elif isinstance(data, list):
                md_content = self._list_to_markdown(data)
            else:
                md_content = f"```\n{content}\n```"
            
            return ConversionResult(
                success=True,
                content=md_content,
                format="markdown"
            )
        except Exception as e:
            return ConversionResult(
                success=False,
                content="",
                format="markdown",
                errors=[str(e)]
            )
    
    def from_markdown(self, markdown: str, **kwargs) -> ConversionResult:
        """Convert Markdown to YAML."""
        try:
            if not HAS_YAML:
                return ConversionResult(
                    success=False,
                    content="",
                    format="yaml",
                    errors=["PyYAML is required for YAML conversion"]
                )
            
            # Extract code blocks or convert structured content
            yaml_blocks = re.findall(r'```yaml\n(.*?)\n```', markdown, re.DOTALL)
            
            if yaml_blocks:
                # Return first YAML block
                yaml_content = yaml_blocks[0]
            else:
                # Convert structured markdown to YAML
                data = self._markdown_to_dict(markdown)
                yaml_content = yaml.dump(data, indent=2)
            
            return ConversionResult(
                success=True,
                content=yaml_content,
                format="yaml"
            )
        except Exception as e:
            return ConversionResult(
                success=False,
                content="",
                format="yaml",
                errors=[str(e)]
            )
    
    def _dict_to_markdown(self, data: Dict[str, Any], level: int = 0) -> str:
        """Convert dictionary to markdown."""
        lines = []
        indent = "  " * level
        
        for key, value in data.items():
            if isinstance(value, dict):
                lines.append(f"{indent}- **{key}:**")
                lines.append(self._dict_to_markdown(value, level + 1))
            elif isinstance(value, list):
                lines.append(f"{indent}- **{key}:**")
                for item in value:
                    lines.append(f"{indent}  - {item}")
            else:
                lines.append(f"{indent}- **{key}:** {value}")
        
        return '\n'.join(lines)
    
    def _list_to_markdown(self, data: List[Any]) -> str:
        """Convert list to markdown."""
        lines = []
        for item in data:
            if isinstance(item, dict):
                lines.append(f"- {self._dict_to_markdown(item, 1)}")
            else:
                lines.append(f"- {item}")
        return '\n'.join(lines)
    
    def _markdown_to_dict(self, markdown: str) -> Dict[str, Any]:
        """Convert structured markdown to dictionary."""
        data = {}
        
        for line in markdown.split('\n'):
            if ':' in line and not line.strip().startswith('#') and not line.strip().startswith('```'):
                key, value = line.split(':', 1)
                data[key.strip()] = value.strip()
        
        return data
