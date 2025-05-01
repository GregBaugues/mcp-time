from fastmcp import FastMCP
import datetime
import pytz


mcp = FastMCP("Time for MCP")

@mcp.tool()
def current_time(timezone: str = "America/New_York") -> str:
    """
    Returns the current time as a string.
    
    Args:
        timezone: Timezone name (e.g., 'UTC', 'US/Pacific', 'Europe/London').
                 Defaults to 'America/New_York'.
    """
    try:
        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz)
        return now.strftime("%H:%M:%S")
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Error: Unknown timezone '{timezone}'. Please use a valid timezone name."


@mcp.tool()
def current_date(timezone: str = "America/New_York") -> str:
    """
    Returns the current date as a string.
    
    Args:
        timezone: Timezone name (e.g., 'UTC', 'US/Pacific', 'Europe/London').
                 Defaults to 'America/New_York'.
    """
    try:
        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz)
        return now.strftime("%Y-%m-%d")
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Error: Unknown timezone '{timezone}'. Please use a valid timezone name."


@mcp.tool()
def current_datetime(timezone: str = "America/New_York") -> str:
    """
    Returns the current date and time as a string.
    
    Args:
        timezone: Timezone name (e.g., 'UTC', 'US/Pacific', 'Europe/London').
                 Defaults to 'America/New_York'.
    
    Returns:
        A formatted date and time string.
    """
    
    try:
        tz = pytz.timezone(timezone)
        now = datetime.datetime.now(tz)
        return now.strftime("%Y-%m-%d %H:%M:%S %Z")
    except pytz.exceptions.UnknownTimeZoneError:
        return f"Error: Unknown timezone '{timezone}'. Please use a valid timezone name."


if __name__ == "__main__":
    import asyncio
    asyncio.run(
        mcp.run_sse_async(
            host="127.0.0.1", 
            port=8000, 
            log_level="debug"
        )
    )
