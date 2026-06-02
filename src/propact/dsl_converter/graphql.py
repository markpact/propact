"""GraphQL converter for bidirectional GraphQL ↔ Markdown conversion."""

from typing import Dict, Any

from .base import BaseConverter, ConversionResult


class GraphQLConverter(BaseConverter):
    """Converter for GraphQL ↔ Markdown."""
    
    def to_markdown(self, content: str, **kwargs) -> ConversionResult:
        """Convert GraphQL query/schema to Markdown."""
        try:
            # Format GraphQL as code block
            formatted = f"```graphql\n{content}\n```"
            
            return ConversionResult(
                success=True,
                content=formatted,
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
        """Convert Markdown to GraphQL query."""
        try:
            api_type = kwargs.get('api_type', 'generic')
            
            # Extract structured data from markdown
            structured_data = self._extract_structured_data(markdown)
            
            # Generate GraphQL query based on API type
            if api_type == 'github':
                query = self._generate_github_query(structured_data)
            elif api_type == 'stripe':
                query = self._generate_stripe_query(structured_data)
            else:
                query = self._generate_generic_query(structured_data)
            
            return ConversionResult(
                success=True,
                content=query,
                format="graphql",
                metadata={"api_type": api_type}
            )
        except Exception as e:
            return ConversionResult(
                success=False,
                content="",
                format="graphql",
                errors=[str(e)]
            )
    
    def _extract_structured_data(self, markdown: str) -> Dict[str, Any]:
        """Extract structured key-value data from markdown."""
        data = {}
        
        # Look for key: value patterns
        for line in markdown.split('\n'):
            if ':' in line and not line.strip().startswith('#') and not line.strip().startswith('```'):
                key, value = line.split(':', 1)
                data[key.strip()] = value.strip()
        
        return data
    
    def _generate_github_query(self, data: Dict[str, Any]) -> str:
        """Generate GitHub GraphQL query."""
        user = data.get('User', data.get('user', 'viewer'))
        status = data.get('Status', 'OPEN')
        limit = data.get('Limit', data.get('limit', '10'))
        
        query = f"""query {{
  user(login: "{user}") {{
    issues(states: [{status}], first: {limit}) {{
      nodes {{
        title
        body
        state
        createdAt
      }}
    }}
  }}
}}"""
        return query
    
    def _generate_stripe_query(self, data: Dict[str, Any]) -> str:
        """Generate Stripe GraphQL query."""
        query = """query {
  charges(first: 10) {
    edges {
      node {
        id
        amount
        currency
        status
        created
      }
    }
  }
}"""
        return query
    
    def _generate_generic_query(self, data: Dict[str, Any]) -> str:
        """Generate generic GraphQL query."""
        return """query {
  viewer {
    id
    name
  }
}"""
