"""
Repository interface for activity data access.

This abstraction allows easy replacement of storage backends
(in-memory, PostgreSQL, MongoDB, etc.) without changing business logic.
"""
from abc import ABC, abstractmethod
from typing import List
from app.models.activity import Activity


class ActivityRepository(ABC):
    """Abstract base class defining the contract for activity storage."""
    
    @abstractmethod
    def save(self, activity: Activity) -> Activity:
        """
        Persist an activity to storage.
        
        Args:
            activity: Activity instance to save
            
        Returns:
            The saved activity instance
        """
        pass
    
    @abstractmethod
    def find_by_goal_id(self, goal_id: str) -> List[Activity]:
        """
        Retrieve all activities associated with a specific goal.
        
        Args:
            goal_id: Unique identifier for the goal
            
        Returns:
            List of activities for the specified goal, sorted by timestamp
        """
        pass
    
    @abstractmethod
    def find_all(self) -> List[Activity]:
        """
        Retrieve all activities across all goals.
        
        Returns:
            List of all activities in storage
        """
        pass
    
    @abstractmethod
    def count_by_goal_id(self, goal_id: str) -> int:
        """
        Count total activities for a specific goal.
        
        Args:
            goal_id: Unique identifier for the goal
            
        Returns:
            Number of activities logged for the goal
        """
        pass
    
    @abstractmethod
    def clear(self) -> None:
        """Clear all activities from storage (useful for testing)."""
        pass
