"""Base classes and shared infrastructure for DSL converters."""

import re
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, List, Union, Tuple
from dataclasses import dataclass


@dataclass
class ConversionResult:
    """Result of a conversion operation."""
    success: bool
    content: str
    format: str
    errors: List[str] = None
    warnings: List[str] = None
    metadata: Dict[str, Any] = None
    
    def __post_init__(self):
        if self.errors is None:
            self.errors = []
        if self.warnings is None:
            self.warnings = []
        if self.metadata is None:
            self.metadata = {}


class BaseConverter(ABC):
    """Base class for format converters."""
    
    def __init__(self):
        self.logger = logging.getLogger(self.__class__.__name__)
    
    @abstractmethod
    def to_markdown(self, content: str, **kwargs) -> ConversionResult:
        """Convert content to Markdown format."""
        pass
    
    @abstractmethod
    def from_markdown(self, markdown: str, **kwargs) -> ConversionResult:
        """Convert Markdown content to target format."""
        pass
    
    def _parse_md_table(self, markdown: str) -> Tuple[List[str], List[List[str]]]:
        """Parse a markdown table into headers and rows."""
        lines = [line.strip() for line in markdown.strip().split('\n') if line.strip()]
        
        # Find table start
        table_start = -1
        for i, line in enumerate(lines):
            if '|' in line and i + 1 < len(lines) and '-' in lines[i + 1]:
                table_start = i
                break
        
        if table_start == -1:
            raise ValueError("No valid markdown table found")
        
        # Parse header
        header_line = lines[table_start]
        headers = [h.strip() for h in header_line.split('|') if h.strip()]
        
        # Parse rows (skip separator line)
        rows = []
        for line in lines[table_start + 2:]:
            if '|' in line:
                row = [cell.strip() for cell in line.split('|') if cell.strip()]
                if row:
                    rows.append(row)
        
        return headers, rows
    
    def _create_md_table(self, headers: List[str], rows: List[List[str]], 
                        align: str = "left") -> str:
        """Create a markdown table from headers and rows."""
        if not headers:
            return ""
        
        # Calculate column widths
        col_widths = [len(h) for h in headers]
        for row in rows:
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    col_widths[i] = max(col_widths[i], len(cell))
        
        # Build table
        lines = []
        
        # Header row
        header_cells = [h.ljust(w) for h, w in zip(headers, col_widths)]
        lines.append(f"| {' | '.join(header_cells)} |")
        
        # Separator row
        if align == "center":
            sep_cells = [':' + '-' * (w - 2) + ':' for w in col_widths]
        elif align == "right":
            sep_cells = ['-' * (w - 1) + ':' for w in col_widths]
        else:  # left
            sep_cells = ['-' * w for w in col_widths]
        lines.append(f"| {' | '.join(sep_cells)} |")
        
        # Data rows
        for row in rows:
            row_cells = []
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    row_cells.append(cell.ljust(col_widths[i]))
                else:
                    row_cells.append(cell)
            lines.append(f"| {' | '.join(row_cells)} |")
        
        return '\n'.join(lines)
