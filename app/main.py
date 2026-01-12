"""
Life Design Backend Service - Main Application Entry Point

A FastAPI microservice for growth journaling and productivity insights.
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.repositories.in_memory_repository import InMemoryActivityRepository
from app.services.analytics_service import AnalyticsService
from app.services.recommendation_service import RecommendationService
from app.api.activities import create_activities_router
from app.api.dashboard import create_dashboard_router
from app.api.insights import create_insights_router


# Application metadata
APP_TITLE = "Life Design Backend Service"
APP_DESCRIPTION = """
🚀 **Growth Journal & Productivity Insights API**

A production-ready backend microservice that powers a Life Design Dashboard.

## Features

* 📝 **Activity Logging**: Track daily efforts toward life goals
* 📊 **Goal Dashboards**: View aggregated progress and metrics
* 🧠 **Smart Insights**: AI-generated recommendations for balanced growth
* ⚡ **Fast & Scalable**: Built with FastAPI and modular architecture

## Core Capabilities

- **Consistency Tracking**: Measure habit formation with consecutive day scoring
- **Wellness Monitoring**: Automated alerts for insufficient health activities
- **Balance Detection**: Identify imbalances between learning and physical wellness
- **Actionable Recommendations**: Personalized guidance based on activity patterns

## Architecture

- **Repository Pattern**: Easy database swapping (in-memory → PostgreSQL/MongoDB)
- **Service Layer**: Clean separation of business logic
- **Type Safety**: Full Pydantic validation and Python type hints
"""
APP_VERSION = "1.0.0"


# Initialize application
app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)


# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://life-design-dashboard-frontend.vercel.app",  # Production frontend
        "https://life-design-dashboard-frontend-qhp68epvd.vercel.app",  # Preview deployment
        "http://localhost:3000",  # Local development
        "http://127.0.0.1:3000"   # Local development alternative
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency Injection: Initialize services and repositories
repository = InMemoryActivityRepository()
analytics_service = AnalyticsService()
recommendation_service = RecommendationService(analytics_service)


# Register routers with dependency injection
app.include_router(create_activities_router(repository))
app.include_router(create_dashboard_router(repository, analytics_service))
app.include_router(create_insights_router(repository, analytics_service, recommendation_service))


@app.get("/", tags=["Health"])
async def root():
    """
    Root endpoint - API health check.
    
    Returns basic service information and status.
    """
    return {
        "service": "Life Design Backend Service",
        "status": "operational",
        "version": APP_VERSION,
        "documentation": "/docs"
    }


@app.get("/health", tags=["Health"])
async def health_check():
    """
    Health check endpoint for monitoring and load balancers.
    """
    return {
        "status": "healthy",
        "total_activities": len(repository)
    }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
