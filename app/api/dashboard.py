"""
API endpoints for dashboard views and goal summaries.
"""
from fastapi import APIRouter, HTTPException, status
from app.schemas.activity_schema import DashboardResponse, ActivityResponse
from app.repositories.activity_repository import ActivityRepository
from app.services.analytics_service import AnalyticsService


router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


def create_dashboard_router(
    repository: ActivityRepository,
    analytics_service: AnalyticsService
) -> APIRouter:
    """
    Factory function to create dashboard router with dependency injection.
    
    Args:
        repository: ActivityRepository implementation
        analytics_service: AnalyticsService instance
        
    Returns:
        Configured APIRouter instance
    """
    
    @router.get(
        "/{goal_id}",
        response_model=DashboardResponse,
        summary="Get goal dashboard",
        description="Retrieve comprehensive dashboard view for a specific goal"
    )
    async def get_goal_dashboard(goal_id: str) -> DashboardResponse:
        """
        Get a summarized dashboard view for a specific goal.
        
        Returns:
        - Total number of activities
        - Aggregated values by activity type
        - Complete activity history (sorted by timestamp)
        - Consistency score (0.0 - 1.0)
        - Wellness warning flag
        
        **Path Parameters:**
        - **goal_id**: Unique identifier for the goal
        """
        try:
            # Fetch all activities for this goal
            activities = repository.find_by_goal_id(goal_id)
            
            if not activities:
                # Return empty dashboard for goals with no activities
                return DashboardResponse(
                    goal_id=goal_id,
                    total_activities=0,
                    aggregated_values={},
                    activity_history=[],
                    consistency_score=0.0,
                    wellness_warning=True
                )
            
            # Calculate metrics
            total_activities = len(activities)
            aggregated_values = analytics_service.aggregate_by_type(activities)
            consistency_score = analytics_service.calculate_consistency_score(activities)
            wellness_warning = analytics_service.check_wellness_warning(activities)
            
            # Convert activities to response schema
            activity_history = [
                ActivityResponse(
                    activity_id=activity.activity_id,
                    goal_id=activity.goal_id,
                    activity_type=activity.activity_type,
                    value=activity.value,
                    timestamp=activity.timestamp.isoformat()
                )
                for activity in activities
            ]
            
            return DashboardResponse(
                goal_id=goal_id,
                total_activities=total_activities,
                aggregated_values=aggregated_values,
                activity_history=activity_history,
                consistency_score=consistency_score,
                wellness_warning=wellness_warning
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to generate dashboard: {str(e)}"
            )
    
    return router
