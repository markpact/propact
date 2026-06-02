# Photos API Example

This example demonstrates fetching photos from the JSONPlaceholder REST API using propact.

## Overview

JSONPlaceholder provides fake photo data for testing. This example shows how to:
- Fetch photo metadata using GET requests
- Work with thumbnail and full-size URLs
- Filter photos by album

## API Endpoint

Base URL: `https://jsonplaceholder.typicode.com`

## Photo Structure

Each photo has the following fields:
- `albumId`: The parent album ID
- `id`: Unique photo identifier
- `title`: Photo title/description
- `url`: Full-size image URL (150x150 placeholder)
- `thumbnailUrl`: Thumbnail image URL (150x150 placeholder)

## Usage

### Quick Run
```bash
./run.sh
```

### Manual Commands

Get a single photo:
```bash
poetry run propact run README.md \
    --endpoint "https://jsonplaceholder.typicode.com/photos/1" \
    --method GET
```

Get photos from an album:
```bash
poetry run propact run README.md \
    --endpoint "https://jsonplaceholder.typicode.com/albums/1/photos?_limit=5" \
    --method GET
```

## Expected Response Format

Response is saved to `README.response.md` with markdown formatting:

```markdown
