"""
API endpoints for activity management.
"""
from fastapi import APIRouter, HTTPException, status
from app.schemas.activity_schema import ActivityCreate, ActivityResponse
from app.models.activity import Activity
from app.repositories.activity_repository import ActivityRepository
from app.utils.date_helpers import parse_iso_datetime


router = APIRouter(prefix="/activities", tags=["Activities"])


def create_activities_router(repository: ActivityRepository) -> APIRouter:
    """
    Factory function to create activities router with dependency injection.
    
    Args:
        repository: ActivityRepository implementation
        
    Returns:
        Configured APIRouter instance
    """
    
    @router.post(
        "",
        response_model=ActivityResponse,
        status_code=status.HTTP_201_CREATED,
        summary="Log a new activity",
        description="Create a new activity entry for a specific goal"
    )
    async def create_activity(activity_data: ActivityCreate) -> ActivityResponse:
        """
        Log a new activity toward a life goal.
        
        - **goal_id**: Unique identifier for the goal
        - **activity_type**: Category (Learning, Health, Fitness, Other)
        - **value**: Numeric value representing effort (e.g., minutes spent)
        - **timestamp**: ISO-8601 formatted datetime
        """
        try:
            # Parse timestamp
            timestamp = parse_iso_datetime(activity_data.timestamp)
            
            # Create domain model
            activity = Activity(
                goal_id=activity_data.goal_id,
                activity_type=activity_data.activity_type,
                value=activity_data.value,
                timestamp=timestamp
            )
            
            # Persist to repository
            saved_activity = repository.save(activity)
            
            # Return response
            return ActivityResponse(
                activity_id=saved_activity.activity_id,
                goal_id=saved_activity.goal_id,
                activity_type=saved_activity.activity_type,
                value=saved_activity.value,
                timestamp=saved_activity.timestamp.isoformat()
            )
            
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid input: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to create activity: {str(e)}"
            )
    
    return router
