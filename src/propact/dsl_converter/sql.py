"""SQL converter for bidirectional SQL ↔ Markdown table conversion."""

import logging
from typing import TYPE_CHECKING

from .base import BaseConverter, ConversionResult

# Try to import optional dependencies
try:
    import pandas as pd
    HAS_PANDAS = True
except ImportError:
    HAS_PANDAS = False

try:
    import sqlglot
    HAS_SQLGLOT = True
except ImportError:
    HAS_SQLGLOT = False

try:
    from markdown_table_generator import table_from_dataframe
    HAS_MD_TABLE_GEN = True
except ImportError:
    HAS_MD_TABLE_GEN = False


class SQLConverter(BaseConverter):
    """Converter for SQL ↔ Markdown tables."""
    
    def __init__(self):
        super().__init__()
        self.supported_dialects = ["postgres", "mysql", "sqlite", "snowflake", "bigquery"]
    
    def to_markdown(self, content: str, **kwargs) -> ConversionResult:
        """Convert SQL query/result to Markdown table."""
        try:
            if not HAS_PANDAS:
                return ConversionResult(
                    success=False,
                    content="",
                    format="markdown",
                    errors=["pandas is required for SQL to Markdown conversion"]
                )
            
            # Check if content is a query or result
            db_connection = kwargs.get('db_connection')
            
            if db_connection:
                # Execute query and get results
                try:
                    df = pd.read_sql(content, db_connection)
                except Exception as e:
                    return ConversionResult(
                        success=False,
                        content="",
                        format="markdown",
                        errors=[f"Failed to execute SQL query: {str(e)}"]
                    )
            else:
                # Parse SQL to generate mock data (for demo)
                df = self._mock_sql_result(content)
            
            # Convert DataFrame to markdown
            if HAS_MD_TABLE_GEN:
                table_md = table_from_dataframe(df, align="center")
                content_md = table_md.to_markdown()
            else:
                # Simple markdown table generation
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
            self.logger.error(f"SQL to Markdown conversion failed: {e}")
            return ConversionResult(
                success=False,
                content="",
                format="markdown",
                errors=[str(e)]
            )
    
    def from_markdown(self, markdown: str, **kwargs) -> ConversionResult:
        """Convert Markdown table to SQL INSERT/UPDATE statements."""
        try:
            dialect = kwargs.get('dialect', 'postgres')
            table_name = kwargs.get('table_name', 'generated_table')
            operation = kwargs.get('operation', 'INSERT')  # INSERT or UPDATE
            
            if dialect not in self.supported_dialects:
                return ConversionResult(
                    success=False,
                    content="",
                    format="sql",
                    errors=[f"Unsupported SQL dialect: {dialect}"]
                )
            
            # Parse markdown table
            headers, rows = self._parse_md_table(markdown)
            
            if not headers or not rows:
                return ConversionResult(
                    success=False,
                    content="",
                    format="sql",
                    errors=["No data found in markdown table"]
                )
            
            # Generate SQL
            sql_statements = []
            
            # CREATE TABLE statement
            columns_def = ', '.join([f'"{col}" TEXT' for col in headers])
            sql_statements.append(f'CREATE TABLE IF NOT EXISTS "{table_name}" ({columns_def});')
            
            if operation == 'INSERT':
                # INSERT statements
                for row in rows:
                    values = ', '.join(['\'' + val.replace("'", "''") + '\'' for val in row])
                    cols = ', '.join([f'"{col}"' for col in headers])
                    sql_statements.append(f'INSERT INTO "{table_name}" ({cols}) VALUES ({values});')
            
            elif operation == 'UPDATE':
                # UPDATE statements (need a key column)
                key_column = kwargs.get('key_column', headers[0])
                if key_column not in headers:
                    return ConversionResult(
                        success=False,
                        content="",
                        format="sql",
                        errors=[f"Key column '{key_column}' not found in table"]
                    )
                
                key_idx = headers.index(key_column)
                for row in rows:
                    set_clauses = []
                    for i, (col, val) in enumerate(zip(headers, row)):
                        if i != key_idx:
                            set_clauses.append(f'"{col}" = \'{val.replace("\"", "\"\"")}\'')
                    
                    where_val = row[key_idx].replace("'", "''")
                    sql_statements.append(
                        f'UPDATE "{table_name}" SET {", ".join(set_clauses)} WHERE "{key_column}" = \'{where_val}\';'
                    )
            
            # Transpile to target dialect if sqlglot is available
            final_sql = '\n'.join(sql_statements)
            if HAS_SQLGLOT and dialect != 'postgres':
                try:
                    final_sql = sqlglot.transpile(final_sql, read='postgres', write=dialect)[0]
                except Exception as e:
                    self.logger.warning(f"SQL transpilation failed: {e}")
            
            return ConversionResult(
                success=True,
                content=final_sql,
                format="sql",
                metadata={"table": table_name, "rows": len(rows), "columns": len(headers)}
            )
            
        except Exception as e:
            self.logger.error(f"Markdown to SQL conversion failed: {e}")
            return ConversionResult(
                success=False,
                content="",
                format="sql",
                errors=[str(e)]
            )
    
    def _mock_sql_result(self, query: str) -> 'pd.DataFrame':
        """Generate mock data for SQL queries (for demo purposes)."""
        # Simple mock data based on query patterns
        if 'users' in query.lower():
            return pd.DataFrame({
                'id': [1, 2, 3],
                'name': ['Alice', 'Bob', 'Charlie'],
                'email': ['alice@example.com', 'bob@example.com', 'charlie@example.com']
            })
        elif 'products' in query.lower():
            return pd.DataFrame({
                'id': [101, 102],
                'name': ['Product A', 'Product B'],
                'price': [29.99, 49.99]
            })
        else:
            return pd.DataFrame({'result': ['mock_data']})
