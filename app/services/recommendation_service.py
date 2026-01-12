"""
Recommendation engine for generating personalized productivity insights.

This service analyzes activity patterns and provides actionable guidance.
"""
from typing import List, Dict
from app.models.activity import Activity
from app.services.analytics_service import AnalyticsService


class RecommendationService:
    """
    Service for generating intelligent recommendations based on activity patterns.
    
    Uses rule-based logic to detect imbalances and suggest improvements.
    """
    
    def __init__(self, analytics_service: AnalyticsService):
        self.analytics_service = analytics_service
    
    def generate_recommendation(self, activities: List[Activity]) -> str:
        """
        Generate a personalized recommendation based on activity patterns.
        
        Detection Rules:
        1. High Learning + Low Health/Fitness = Rebalancing needed
        2. Low consistency = Focus on building habits
        3. Wellness warning = Prioritize physical health
        4. Balanced activities = Maintain current approach
        
        Args:
            activities: List of all user activities
            
        Returns:
            Human-readable recommendation string
        """
        if not activities:
            return (
                "Start your growth journey by logging your first activity! "
                "Consistent small efforts compound into remarkable results."
            )
        
        aggregated = self.analytics_service.aggregate_by_type(activities)
        consistency_score = self.analytics_service.calculate_consistency_score(activities)
        wellness_warning = self.analytics_service.check_wellness_warning(activities)
        
        # Rule 1: Detect Learning/Health imbalance
        learning_total = aggregated.get("Learning", 0.0)
        health_total = aggregated.get("Health", 0.0)
        fitness_total = aggregated.get("Fitness", 0.0)
        physical_wellness = health_total + fitness_total
        
        if learning_total > 0 and physical_wellness > 0:
            ratio = learning_total / physical_wellness
            if ratio > 3.0:  # Learning is 3x more than physical wellness
                return (
                    "You are investing heavily in learning but neglecting physical wellness. "
                    "Consider rebalancing your growth plan. Research shows that physical "
                    "activity enhances cognitive performance and learning retention."
                )
        
        # Rule 2: Low consistency
        if consistency_score < 0.3:
            return (
                "Your consistency score is low. Focus on building a daily habit, "
                "even if it's just 15 minutes. Consistency beats intensity for "
                "long-term growth. Try the 2-minute rule: start so small you can't say no."
            )
        
        # Rule 3: Wellness warning
        if wellness_warning:
            return (
                "⚠️ Wellness Alert: You haven't met the recommended 150 minutes of "
                "health-related activity this week. Your body is the foundation of all "
                "growth. Schedule at least 30 minutes of movement daily."
            )
        
        # Rule 4: High learning, no physical activity at all
        if learning_total > 300 and physical_wellness == 0:
            return (
                "You're making great progress in learning! However, you have zero "
                "physical wellness activities logged. A healthy body fuels a sharp mind. "
                "Consider adding short movement breaks between study sessions."
            )
        
        # Rule 5: Excellent balance
        if consistency_score >= 0.7 and not wellness_warning:
            return (
                "Excellent work! You're maintaining strong consistency and a balanced "
                "approach to growth. Keep up this momentum. Consider setting a new "
                "stretch goal to continue challenging yourself."
            )
        
        # Default: Encourage balance
        return (
            "You're making progress! To optimize your growth, aim for balance across "
            "learning, health, and fitness. Track your consistency and adjust your "
            "plan based on what energizes you most."
        )
    
    def detect_activity_gaps(self, activities: List[Activity]) -> Dict[str, bool]:
        """
        Identify which activity types are missing or underrepresented.
        
        Returns:
            Dictionary mapping activity_type to whether it's missing (True = gap exists)
        """
        aggregated = self.analytics_service.aggregate_by_type(activities)
        
        activity_types = ["Learning", "Health", "Fitness", "Other"]
        gaps = {}
        
        for activity_type in activity_types:
            # Consider it a gap if total is 0 or very low (< 60 minutes total)
            total = aggregated.get(activity_type, 0.0)
            gaps[activity_type] = total < 60.0
        
        return gaps
