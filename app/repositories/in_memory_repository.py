"""
In-memory implementation of the ActivityRepository interface.

This implementation uses Python data structures for storage.
Thread-safe operations can be added using threading.Lock if needed.
"""
from typing import List
from app.models.activity import Activity
from app.repositories.activity_repository import ActivityRepository


class InMemoryActivityRepository(ActivityRepository):
    """
    In-memory storage implementation using a dictionary.
    
    Data structure: {activity_id: Activity}
    Optimized for fast lookups and filtering operations.
    """
    
    def __init__(self):
        self._storage: dict[str, Activity] = {}
    
    def save(self, activity: Activity) -> Activity:
        """Store activity in memory using activity_id as key."""
        self._storage[activity.activity_id] = activity
        return activity
    
    def find_by_goal_id(self, goal_id: str) -> List[Activity]:
        """
        Filter activities by goal_id and sort by timestamp.
        
        Time complexity: O(n log n) where n is total activities
        Space complexity: O(k) where k is matching activities
        """
        matching_activities = [
            activity for activity in self._storage.values()
            if activity.goal_id == goal_id
        ]
        # Sort by timestamp (oldest first)
        return sorted(matching_activities, key=lambda a: a.timestamp)
    
    def find_all(self) -> List[Activity]:
        """Return all activities sorted by timestamp."""
        return sorted(self._storage.values(), key=lambda a: a.timestamp)
    
    def count_by_goal_id(self, goal_id: str) -> int:
        """
        Count activities for a specific goal.
        
        Time complexity: O(n) where n is total activities
        """
        return sum(1 for activity in self._storage.values() if activity.goal_id == goal_id)
    
    def clear(self) -> None:
        """Clear all stored activities."""
        self._storage.clear()
    
    def __len__(self) -> int:
        """Return total number of stored activities."""
        return len(self._storage)
