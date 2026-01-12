"""
Pydantic schemas for request/response validation and serialization.
"""
from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field, field_validator


class ActivityCreate(BaseModel):
    """Schema for creating a new activity entry."""
    
    goal_id: str = Field(..., min_length=1, description="Unique identifier for the goal")
    activity_type: Literal["Learning", "Health", "Fitness", "Other"] = Field(
        ..., description="Category of the activity"
    )
    value: float = Field(..., gt=0, description="Numeric value representing effort (e.g., minutes)")
    timestamp: str = Field(..., description="ISO-8601 formatted datetime string")
    
    @field_validator('timestamp')
    @classmethod
    def validate_timestamp(cls, v: str) -> str:
        """Validate that timestamp is a valid ISO-8601 datetime."""
        try:
            datetime.fromisoformat(v.replace('Z', '+00:00'))
        except ValueError:
            raise ValueError('timestamp must be a valid ISO-8601 datetime string')
        return v
    
    class Config:
        json_schema_extra = {
            "example": {
                "goal_id": "career-growth-2024",
                "activity_type": "Learning",
                "value": 120,
                "timestamp": "2024-01-15T14:30:00Z"
            }
        }


class ActivityResponse(BaseModel):
    """Schema for activity response."""
    
    activity_id: str
    goal_id: str
    activity_type: str
    value: float
    timestamp: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "activity_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
                "goal_id": "career-growth-2024",
                "activity_type": "Learning",
                "value": 120,
                "timestamp": "2024-01-15T14:30:00Z"
            }
        }


class DashboardResponse(BaseModel):
    """Schema for dashboard summary response."""
    
    goal_id: str
    total_activities: int
    aggregated_values: dict[str, float]
    activity_history: list[ActivityResponse]
    consistency_score: float = Field(..., ge=0.0, le=1.0)
    wellness_warning: bool
    
    class Config:
        json_schema_extra = {
            "example": {
                "goal_id": "career-growth-2024",
                "total_activities": 15,
                "aggregated_values": {
                    "Learning": 1800,
                    "Health": 300,
                    "Fitness": 450
                },
                "activity_history": [],
                "consistency_score": 0.82,
                "wellness_warning": False
            }
        }


class InsightsResponse(BaseModel):
    """Schema for optimization insights response."""
    
    consistency_score: float = Field(..., ge=0.0, le=1.0)
    wellness_warning: bool
    recommendation: str
    
    class Config:
        json_schema_extra = {
            "example": {
                "consistency_score": 0.82,
                "wellness_warning": True,
                "recommendation": "You are investing heavily in learning but neglecting physical wellness. Consider rebalancing your growth plan."
            }
        }
