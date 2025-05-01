# MCP Time Service

A FastMCP service that provides current time, date, and datetime information in various timezones.

## Available Tools

- `current_time`: Returns the current time in the specified timezone
- `current_date`: Returns the current date in the specified timezone
- `current_datetime`: Returns the current date and time in the specified timezone

All tools accept an optional `timezone` parameter (defaults to 'America/New_York').

## Development

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the server:
```bash
python server.py
```

The server will start on `http://127.0.0.1:8000`.

## Deployment

This service is configured for deployment on Render. The `render.yaml` file contains the necessary configuration 