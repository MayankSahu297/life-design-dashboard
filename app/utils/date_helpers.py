"""
Utility functions for date and time operations.
"""
from datetime import datetime, timedelta
from typing import List


def parse_iso_datetime(iso_string: str) -> datetime:
    """
    Parse ISO-8601 datetime string to datetime object.
    
    Handles both with and without timezone information.
    """
    # Replace 'Z' with '+00:00' for UTC timezone
    normalized = iso_string.replace('Z', '+00:00')
    return datetime.fromisoformat(normalized)


def get_date_only(dt: datetime) -> datetime:
    """Extract date component, setting time to midnight."""
    return datetime(dt.year, dt.month, dt.day)


def calculate_consecutive_days(timestamps: List[datetime]) -> int:
    """
    Calculate the number of consecutive days with activity.
    
    Args:
        timestamps: List of datetime objects
        
    Returns:
        Number of consecutive days (from most recent backwards)
    """
    if not timestamps:
        return 0
    
    # Extract unique dates and sort in descending order
    unique_dates = sorted(set(get_date_only(ts) for ts in timestamps), reverse=True)
    
    if not unique_dates:
        return 0
    
    consecutive_count = 1
    current_date = unique_dates[0]
    
    for next_date in unique_dates[1:]:
        expected_previous = current_date - timedelta(days=1)
        if get_date_only(next_date) == expected_previous:
            consecutive_count += 1
            current_date = next_date
        else:
            break
    
    return consecutive_count


def get_week_start(dt: datetime) -> datetime:
    """Get the start of the week (Monday) for a given datetime."""
    days_since_monday = dt.weekday()
    week_start = dt - timedelta(days=days_since_monday)
    return get_date_only(week_start)


def filter_last_n_days(timestamps: List[datetime], days: int) -> List[datetime]:
    """
    Filter timestamps to only include those within the last N days.
    
    Args:
        timestamps: List of datetime objects
        days: Number of days to look back
        
    Returns:
        Filtered list of timestamps
    """
    if not timestamps:
        return []
    
    cutoff = datetime.now() - timedelta(days=days)
    return [ts for ts in timestamps if ts >= cutoff]
