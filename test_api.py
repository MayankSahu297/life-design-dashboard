"""
Test script to demonstrate the Life Design Backend Service API.

This script creates sample activities and tests all endpoints.
"""
import httpx
import json
from datetime import datetime, timedelta


BASE_URL = "http://localhost:8000"


def print_response(title: str, response):
    """Pretty print API response."""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2))


def main():
    """Run API tests."""
    
    print("\n🚀 Life Design Backend Service - API Test Suite")
    print("="*60)
    
    # Test 1: Health Check
    print("\n📍 Test 1: Health Check")
    response = httpx.get(f"{BASE_URL}/health")
    print_response("GET /health", response)
    
    # Test 2: Create Activities
    print("\n📍 Test 2: Creating Sample Activities")
    
    # Generate timestamps for the last 7 days
    now = datetime.now()
    activities_data = [
        # Learning activities (high volume)
        {
            "goal_id": "career-growth-2024",
            "activity_type": "Learning",
            "value": 120,
            "timestamp": (now - timedelta(days=0)).isoformat() + "Z"
        },
        {
            "goal_id": "career-growth-2024",
            "activity_type": "Learning",
            "value": 90,
            "timestamp": (now - timedelta(days=1)).isoformat() + "Z"
        },
        {
            "goal_id": "career-growth-2024",
            "activity_type": "Learning",
            "value": 150,
            "timestamp": (now - timedelta(days=2)).isoformat() + "Z"
        },
        {
            "goal_id": "career-growth-2024",
            "activity_type": "Learning",
            "value": 180,
            "timestamp": (now - timedelta(days=3)).isoformat() + "Z"
        },
        # Health activities (low volume - should trigger warning)
        {
            "goal_id": "career-growth-2024",
            "activity_type": "Health",
            "value": 30,
            "timestamp": (now - timedelta(days=1)).isoformat() + "Z"
        },
        {
            "goal_id": "career-growth-2024",
            "activity_type": "Health",
            "value": 45,
            "timestamp": (now - timedelta(days=3)).isoformat() + "Z"
        },
        # Fitness activities
        {
            "goal_id": "career-growth-2024",
            "activity_type": "Fitness",
            "value": 60,
            "timestamp": (now - timedelta(days=2)).isoformat() + "Z"
        },
    ]
    
    for i, activity in enumerate(activities_data, 1):
        response = httpx.post(f"{BASE_URL}/activities", json=activity)
        print(f"\n  Activity {i}: {activity['activity_type']} - {activity['value']} min")
        print(f"  Status: {response.status_code} - Activity ID: {response.json()['activity_id'][:8]}...")
    
    # Test 3: Get Dashboard
    print("\n\n📍 Test 3: Get Goal Dashboard")
    response = httpx.get(f"{BASE_URL}/dashboard/career-growth-2024")
    print_response("GET /dashboard/career-growth-2024", response)
    
    # Test 4: Get Insights
    print("\n\n📍 Test 4: Get Optimization Insights")
    response = httpx.get(f"{BASE_URL}/insights/optimization")
    print_response("GET /insights/optimization", response)
    
    # Test 5: Create more balanced activities
    print("\n\n📍 Test 5: Adding More Health Activities")
    
    balanced_activities = [
        {
            "goal_id": "wellness-2024",
            "activity_type": "Health",
            "value": 60,
            "timestamp": (now - timedelta(days=0)).isoformat() + "Z"
        },
        {
            "goal_id": "wellness-2024",
            "activity_type": "Health",
            "value": 45,
            "timestamp": (now - timedelta(days=1)).isoformat() + "Z"
        },
        {
            "goal_id": "wellness-2024",
            "activity_type": "Fitness",
            "value": 90,
            "timestamp": (now - timedelta(days=0)).isoformat() + "Z"
        },
        {
            "goal_id": "wellness-2024",
            "activity_type": "Learning",
            "value": 60,
            "timestamp": (now - timedelta(days=0)).isoformat() + "Z"
        },
    ]
    
    for activity in balanced_activities:
        response = httpx.post(f"{BASE_URL}/activities", json=activity)
        print(f"  ✓ Added {activity['activity_type']} activity")
    
    # Test 6: Get Wellness Dashboard
    print("\n\n📍 Test 6: Get Wellness Goal Dashboard")
    response = httpx.get(f"{BASE_URL}/dashboard/wellness-2024")
    print_response("GET /dashboard/wellness-2024", response)
    
    # Test 7: Get Updated Insights
    print("\n\n📍 Test 7: Get Updated Insights (After Adding More Activities)")
    response = httpx.get(f"{BASE_URL}/insights/optimization")
    print_response("GET /insights/optimization", response)
    
    print("\n\n✅ All tests completed successfully!")
    print("="*60)
    print("\n📚 Next Steps:")
    print("  • View interactive docs: http://localhost:8000/docs")
    print("  • Try the ReDoc version: http://localhost:8000/redoc")
    print("  • Explore the API with Postman or curl")
    print("\n")


if __name__ == "__main__":
    try:
        main()
    except httpx.ConnectError:
        print("\n❌ Error: Could not connect to the server.")
        print("   Make sure the server is running: uvicorn app.main:app --reload")
    except Exception as e:
        print(f"\n❌ Error: {e}")
