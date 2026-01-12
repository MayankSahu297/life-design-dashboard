"""
API endpoints for insights and recommendations.
"""
from fastapi import APIRouter, HTTPException, status
from app.schemas.activity_schema import InsightsResponse
from app.repositories.activity_repository import ActivityRepository
from app.services.analytics_service import AnalyticsService
from app.services.recommendation_service import RecommendationService


router = APIRouter(prefix="/insights", tags=["Insights"])


def create_insights_router(
    repository: ActivityRepository,
    analytics_service: AnalyticsService,
    recommendation_service: RecommendationService
) -> APIRouter:
    """
    Factory function to create insights router with dependency injection.
    
    Args:
        repository: ActivityRepository implementation
        analytics_service: AnalyticsService instance
        recommendation_service: RecommendationService instance
        
    Returns:
        Configured APIRouter instance
    """
    
    @router.get(
        "/optimization",
        response_model=InsightsResponse,
        summary="Get optimization insights",
        description="Retrieve AI-generated productivity recommendations based on activity patterns"
    )
    async def get_optimization_insights() -> InsightsResponse:
        """
        Get system-generated productivity recommendations.
        
        Analyzes all user activities to provide:
        - **consistency_score**: How consistently the user logs activities (0.0 - 1.0)
        - **wellness_warning**: Alert if health activities are below recommended threshold
        - **recommendation**: Personalized guidance for optimizing growth plan
        
        The recommendation engine detects patterns such as:
        - Imbalance between learning and physical wellness
        - Low consistency in activity logging
        - Missing activity categories
        - Opportunities for improvement
        """
        try:
            # Fetch all activities across all goals
            all_activities = repository.find_all()
            
            # Calculate global metrics
            consistency_score = analytics_service.calculate_consistency_score(all_activities)
            wellness_warning = analytics_service.check_wellness_warning(all_activities)
            
            # Generate personalized recommendation
            recommendation = recommendation_service.generate_recommendation(all_activities)
            
            return InsightsResponse(
                consistency_score=consistency_score,
                wellness_warning=wellness_warning,
                recommendation=recommendation
            )
            
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Failed to generate insights: {str(e)}"
            )
    
    return router
