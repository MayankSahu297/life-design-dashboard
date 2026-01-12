"""
Analytics service for computing metrics and insights from activity data.

This service transforms raw activity logs into meaningful business metrics.
"""
from datetime import datetime, timedelta
from typing import List, Dict
from app.models.activity import Activity
from app.utils.date_helpers import (
    calculate_consecutive_days,
    get_week_start,
    filter_last_n_days
)


class AnalyticsService:
    """
    Service layer for activity analytics and metric computation.
    
    Responsibilities:
    - Calculate consistency scores
    - Detect wellness warnings
    - Aggregate activity data by type
    """
    
    WELLNESS_THRESHOLD_MINUTES = 150  # WHO recommendation: 150 min/week
    
    def calculate_consistency_score(self, activities: List[Activity]) -> float:
        """
        Compute consistency index based on consecutive days of activity.
        
        Algorithm:
        1. Extract all unique activity dates
        2. Count consecutive days from most recent backwards
        3. Normalize score: consecutive_days / (consecutive_days + 7)
           - This creates a 0-1 scale where:
             - 0 days = 0.0
             - 7 consecutive days = 0.5
             - 14 consecutive days = 0.67
             - 21 consecutive days = 0.75
             - Asymptotically approaches 1.0
        
        Time complexity: O(n log n) due to sorting
        Space complexity: O(n) for unique dates
        
        Args:
            activities: List of Activity objects
            
        Returns:
            Consistency score between 0.0 and 1.0
        """
        if not activities:
            return 0.0
        
        timestamps = [activity.timestamp for activity in activities]
        consecutive_days = calculate_consecutive_days(timestamps)
        
        # Normalize using asymptotic formula
        # This rewards consistency but has diminishing returns
        score = consecutive_days / (consecutive_days + 7)
        
        return round(score, 2)
    
    def check_wellness_warning(self, activities: List[Activity]) -> bool:
        """
        Determine if user has insufficient health-related activity.
        
        Checks if total Health activity in the past 7 days is below
        the WHO recommended 150 minutes per week.
        
        Args:
            activities: List of Activity objects
            
        Returns:
            True if wellness warning should be triggered
        """
        if not activities:
            return True  # No activity is a warning
        
        # Calculate cutoff date (7 days ago)
        from datetime import datetime, timedelta, timezone
        cutoff = datetime.now(timezone.utc) - timedelta(days=7)
        
        # Filter activities from last 7 days and calculate Health minutes
        recent_health_minutes = sum(
            activity.value
            for activity in activities
            if (activity.timestamp if activity.timestamp.tzinfo else activity.timestamp.replace(tzinfo=timezone.utc)) >= cutoff
            and activity.activity_type == "Health"
        )
        
        return recent_health_minutes < self.WELLNESS_THRESHOLD_MINUTES
    
    def aggregate_by_type(self, activities: List[Activity]) -> Dict[str, float]:
        """
        Aggregate total values by activity type.
        
        Args:
            activities: List of Activity objects
            
        Returns:
            Dictionary mapping activity_type to total value
        """
        aggregated: Dict[str, float] = {}
        
        for activity in activities:
            activity_type = activity.activity_type
            aggregated[activity_type] = aggregated.get(activity_type, 0.0) + activity.value
        
        return aggregated
    
    def get_weekly_totals(self, activities: List[Activity]) -> Dict[str, Dict[str, float]]:
        """
        Group activities by week and calculate totals per activity type.
        
        Returns:
            Dictionary mapping week_start_date to {activity_type: total_value}
        """
        weekly_data: Dict[str, Dict[str, float]] = {}
        
        for activity in activities:
            week_start = get_week_start(activity.timestamp)
            week_key = week_start.strftime("%Y-%m-%d")
            
            if week_key not in weekly_data:
                weekly_data[week_key] = {}
            
            activity_type = activity.activity_type
            weekly_data[week_key][activity_type] = (
                weekly_data[week_key].get(activity_type, 0.0) + activity.value
            )
        
        return weekly_data
