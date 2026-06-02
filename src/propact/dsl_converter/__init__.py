"""DSL Converter for bidirectional format conversions.

This package provides converters for various formats to/from Markdown:
- SQL ↔ Markdown tables
- GraphQL ↔ Markdown
- YAML ↔ Markdown
- CSV ↔ Markdown tables
- XML ↔ Markdown
"""

import logging
from typing import Dict, List

from .base import BaseConverter, ConversionResult
from .sql import SQLConverter
from .graphql import GraphQLConverter
from .yaml import YAMLConverter
from .csv import CSVConverter
from .xml import XMLConverter


class DSLConverter:
    """Main DSL converter using strategy pattern."""
    
    def __init__(self):
        """Initialize DSL converter with all format converters."""
        self.converters: Dict[str, BaseConverter] = {
            'sql': SQLConverter(),
            'graphql': GraphQLConverter(),
            'yaml': YAMLConverter(),
            'yml': YAMLConverter(),
            'csv': CSVConverter(),
            'xml': XMLConverter(),
        }
        self.logger = logging.getLogger(__name__)
    
    def convert(self, content: str, from_format: str, to_format: str, **kwargs) -> ConversionResult:
        """Convert content from one format to another.
        
        Args:
            content: Input content
            from_format: Source format (sql, graphql, yaml, csv, xml, markdown)
            to_format: Target format
            **kwargs: Additional options for conversion
            
        Returns:
            ConversionResult with converted content or errors
        """
        try:
            # Normalize formats
            from_format = from_format.lower()
            to_format = to_format.lower()
            
            # Direct conversion
            if from_format == 'markdown':
                # Markdown to target format
                if to_format not in self.converters:
                    return ConversionResult(
                        success=False,
                        content="",
                        format=to_format,
                        errors=[f"Unsupported target format: {to_format}"]
                    )
                
                converter = self.converters[to_format]
                return converter.from_markdown(content, **kwargs)
            
            elif to_format == 'markdown':
                # Source format to Markdown
                if from_format not in self.converters:
                    return ConversionResult(
                        success=False,
                        content="",
                        format="markdown",
                        errors=[f"Unsupported source format: {from_format}"]
                    )
                
                converter = self.converters[from_format]
                return converter.to_markdown(content, **kwargs)
            
            else:
                # Convert via Markdown as intermediate format
                # First convert to Markdown
                if from_format not in self.converters:
                    return ConversionResult(
                        success=False,
                        content="",
                        format=to_format,
                        errors=[f"Unsupported source format: {from_format}"]
                    )
                
                converter = self.converters[from_format]
                md_result = converter.to_markdown(content, **kwargs)
                
                if not md_result.success:
                    return md_result
                
                # Then convert Markdown to target
                if to_format not in self.converters:
                    return ConversionResult(
                        success=False,
                        content="",
                        format=to_format,
                        errors=[f"Unsupported target format: {to_format}"]
                    )
                
                target_converter = self.converters[to_format]
                return target_converter.from_markdown(md_result.content, **kwargs)
        
        except Exception as e:
            self.logger.error(f"Conversion failed: {e}")
            return ConversionResult(
                success=False,
                content="",
                format=to_format,
                errors=[str(e)]
            )
    
    def list_formats(self) -> List[str]:
        """List all supported formats."""
        return list(self.converters.keys()) + ['markdown']
    
    def register_converter(self, format_name: str, converter: BaseConverter):
        """Register a custom converter."""
        self.converters[format_name.lower()] = converter


# Default converter instance
default_converter = DSLConverter()


# Public API exports
__all__ = [
    "DSLConverter",
    "default_converter",
    "BaseConverter",
    "ConversionResult",
    "SQLConverter",
    "GraphQLConverter",
    "YAMLConverter",
    "CSVConverter",
    "XMLConverter",
]
