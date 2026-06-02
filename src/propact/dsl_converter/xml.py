"""XML converter for bidirectional XML ↔ Markdown conversion."""

import re
from typing import Dict, Any

from .base import BaseConverter, ConversionResult

# Try to import optional dependencies
try:
    import xmltodict
    HAS_XMLTODICT = True
except ImportError:
    HAS_XMLTODICT = False

try:
    import yaml
    HAS_YAML = True
except ImportError:
    HAS_YAML = False


class XMLConverter(BaseConverter):
    """Converter for XML ↔ Markdown."""
    
    def to_markdown(self, content: str, **kwargs) -> ConversionResult:
        """Convert XML to Markdown."""
        try:
            if not HAS_XMLTODICT:
                return ConversionResult(
                    success=False,
                    content="",
                    format="markdown",
                    errors=["xmltodict is required for XML conversion"]
                )
            
            # Parse XML
            data = xmltodict.parse(content)
            
            # Convert to YAML for readability, then wrap in code block
            if HAS_YAML:
                yaml_content = yaml.dump(data, indent=2)
                md_content = f"```xml\n{content}\n```\n\n**Parsed Structure:**\n```yaml\n{yaml_content}\n```"
            else:
                md_content = f"```xml\n{content}\n```"
            
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
        """Convert Markdown to XML."""
        try:
            if not HAS_XMLTODICT:
                return ConversionResult(
                    success=False,
                    content="",
                    format="xml",
                    errors=["xmltodict is required for XML conversion"]
                )
            
            # Extract XML from code blocks
            xml_blocks = re.findall(r'```xml\n(.*?)\n```', markdown, re.DOTALL)
            
            if xml_blocks:
                return ConversionResult(
                    success=True,
                    content=xml_blocks[0],
                    format="xml"
                )
            
            # Convert structured data to XML
            root_tag = kwargs.get('root_tag', 'root')
            data = self._markdown_to_dict(markdown)
            
            xml_content = xmltodict.unparse({root_tag: data}, pretty=True)
            
            return ConversionResult(
                success=True,
                content=xml_content,
                format="xml"
            )
        except Exception as e:
            return ConversionResult(
                success=False,
                content="",
                format="xml",
                errors=[str(e)]
            )
    
    def _markdown_to_dict(self, markdown: str) -> Dict[str, Any]:
        """Convert structured markdown to dictionary."""
        data = {}
        
        for line in markdown.split('\n'):
            if ':' in line and not line.strip().startswith('#') and not line.strip().startswith('```'):
                key, value = line.split(':', 1)
                data[key.strip()] = value.strip()
        
        return data
