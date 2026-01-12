"""
Activity domain model representing user growth journal entries.
"""
from datetime import datetime
from typing import Literal
from uuid import uuid4


ActivityType = Literal["Learning", "Health", "Fitness", "Other"]


class Activity:
    """
    Domain model for a user activity log entry.
    
    Represents a single effort toward a life goal with associated metadata.
    """
    
    def __init__(
        self,
        goal_id: str,
        activity_type: ActivityType,
        value: float,
        timestamp: datetime,
        activity_id: str | None = None
    ):
        self.activity_id = activity_id or str(uuid4())
        self.goal_id = goal_id
        self.activity_type = activity_type
        self.value = value
        self.timestamp = timestamp
    
    def __repr__(self) -> str:
        return (
            f"Activity(id={self.activity_id}, goal={self.goal_id}, "
            f"type={self.activity_type}, value={self.value}, "
            f"timestamp={self.timestamp.isoformat()})"
        )
    
    def to_dict(self) -> dict:
        """Convert activity to dictionary representation."""
        return {
            "activity_id": self.activity_id,
            "goal_id": self.goal_id,
            "activity_type": self.activity_type,
            "value": self.value,
            "timestamp": self.timestamp.isoformat()
        }
