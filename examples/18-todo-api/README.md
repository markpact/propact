# Todo API Example

This example demonstrates CRUD operations with the JSONPlaceholder REST API using propact.

## Overview

JSONPlaceholder is a free fake REST API for testing and prototyping. This example shows how to:
- Fetch todos using GET requests
- Handle JSON responses
- Save formatted responses to markdown

## API Endpoint

Base URL: `https://jsonplaceholder.typicode.com`

## Usage

### Quick Run
```bash
./run.sh
```

### Manual Commands

Get a single todo:
```bash
poetry run propact run README.md \
    --endpoint "https://jsonplaceholder.typicode.com/todos/1" \
    --method GET
```

List todos for a user:
```bash
poetry run propact run README.md \
    --endpoint "https://jsonplaceholder.typicode.com/todos?userId=1&_limit=5" \
    --method GET
```

## Expected Response Format

Response is saved to `README.response.md` with markdown formatting:

```markdown
