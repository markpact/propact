"""CSV converter for bidirectional CSV ↔ Markdown table conversion."""

import csv
from io import StringIO

from .base import BaseConverter, ConversionResult

# Try to import optional dependencies
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    from markdown_table_generator import table_from_dataframe
    HAS_MD_TABLE_GEN = True
except ImportError:
    HAS_MD_TABLE_GEN = False


class CSVConverter(BaseConverter):
    """Converter for CSV ↔ Markdown tables."""
    
    def to_markdown(self, content: str, **kwargs) -> ConversionResult:
        """Convert CSV to Markdown table."""
        try:
            if not HAS_PANDAS:
                return ConversionResult(
                    success=False,
                    content="",
                    format="markdown",
                    errors=["pandas is required for CSV conversion"]
                )
            
            # Parse CSV
            df = pd.read_csv(StringIO(content))
            
            # Convert to markdown table
            if HAS_MD_TABLE_GEN:
                table_md = table_from_dataframe(df, align="center")
                content_md = table_md.to_markdown()
            else:
                content_md = self._create_md_table(
                    df.columns.tolist(),
                    df.values.astype(str).tolist()
                )
            
            return ConversionResult(
                success=True,
                content=content_md,
                format="markdown",
                metadata={"rows": len(df), "columns": len(df.columns)}
            )
        except Exception as e:
            return ConversionResult(
                success=False,
                content="",
                format="markdown",
                errors=[str(e)]
            )
    
    def from_markdown(self, markdown: str, **kwargs) -> ConversionResult:
        """Convert Markdown table to CSV."""
        try:
            # Parse markdown table
            headers, rows = self._parse_md_table(markdown)
            
            # Generate CSV
            output = StringIO()
            writer = csv.writer(output)
            writer.writerow(headers)
            writer.writerows(rows)
            
            csv_content = output.getvalue()
            
            return ConversionResult(
                success=True,
                content=csv_content,
                format="csv",
                metadata={"rows": len(rows), "columns": len(headers)}
            )
        except Exception as e:
            return ConversionResult(
                success=False,
                content="",
                format="csv",
                errors=[str(e)]
            )
