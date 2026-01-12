# 🚀 Life Design Dashboard - Full Stack Application

**Growth Journal & Productivity Insights Platform**

A complete full-stack application featuring a production-ready Python FastAPI backend and a stunning modern frontend, enabling users to log daily efforts toward life goals, visualize progress, and receive AI-powered productivity insights.

---

## 🌐 Live Deployment

**🎨 Frontend Application:**  
👉 **https://life-design-dashboard-frontend.vercel.app**

**⚙️ Backend API:**  
👉 **https://life-design-dashboard.onrender.com**

**📚 API Documentation:**  
👉 **https://life-design-dashboard.onrender.com/docs**

---

## 📋 Table of Contents

- [Live Deployment](#live-deployment)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Local Development](#local-development)
- [API Documentation](#api-documentation)
- [Project Structure](#project-structure)
- [Deployment](#deployment)

---

## ✨ Features

### 🎯 Core Functionality

- **📝 Activity Logging**: Track efforts across Learning, Health, Fitness, and Other categories
- **📊 Goal Dashboards**: Aggregated metrics, activity history, consistency scores
- **🧠 Smart Insights**: AI-generated recommendations based on behavioral patterns
- **⚠️ Wellness Monitoring**: Automated alerts for insufficient health activities

### 🎨 Frontend Highlights

- ✨ **Glassmorphism Design** with backdrop blur effects
- 🌈 **Gradient Backgrounds** with smooth animations
- 🌙 **Dark Theme** optimized for extended use
- 📱 **Fully Responsive** for all devices
- ⚡ **Micro-animations** for enhanced UX
- 🎨 **Premium Aesthetics** with vibrant color palettes

### 🛠️ Technical Highlights

- **Type Safety**: Full Pydantic validation and Python 3.10+ type hints
- **Repository Pattern**: Interface-based storage abstraction
- **Service Layer**: Clean separation of business logic
- **RESTful Design**: HTTP-compliant endpoints with proper status codes
- **Auto-Generated Docs**: Interactive Swagger UI and ReDoc

---

## 🛠️ Tech Stack

### Backend
| Component | Technology |
|-----------|-----------|
| **Language** | Python 3.10+ |
| **Framework** | FastAPI |
| **Validation** | Pydantic v2 |
| **Server** | Uvicorn (ASGI) |
| **Storage** | In-Memory (Repository Pattern) |
| **Deployment** | Render |

### Frontend
| Component | Technology |
|-----------|-----------|
| **Languages** | HTML5, CSS3, JavaScript (ES6+) |
| **Styling** | Vanilla CSS with Modern Design |
| **Design** | Glassmorphism, Gradients, Animations |
| **Architecture** | Single Page Application (SPA) |
| **API Integration** | Fetch API |
| **Deployment** | Vercel |

---

## 🏗️ Architecture

### Design Principles

1. **Repository Pattern**: Abstraction layer for data access
   - Current: In-memory storage
   - Future: Swap to PostgreSQL/MongoDB without changing business logic

2. **Service Layer**: Business logic separated from API layer
   - `AnalyticsService`: Metric computation
   - `RecommendationService`: Insight generation

3. **Dependency Injection**: Services injected into routers for testability

### Data Flow

```
Client Request
    ↓
API Layer (FastAPI Router)
    ↓
Service Layer (Business Logic)
    ↓
Repository Layer (Data Access)
    ↓
In-Memory Storage
```

---

## 💻 Local Development

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Backend Setup

1. **Navigate to Project Directory**

```bash
cd life-design-dashboard
```

2. **Create Virtual Environment** (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate
```

3. **Install Dependencies**

```bash
pip install -r requirements.txt
```

4. **Run the Backend Server**

```bash
# Development mode (auto-reload)
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# Or use Python directly
python -m app.main
```

5. **Access the API**

- **API Base URL**: http://localhost:8000
- **Interactive Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

### Frontend Setup

1. **Navigate to Frontend Directory**

```bash
cd frontend
```

2. **Start Local Server**

```bash
python -m http.server 3000
```

3. **Access the Application**

- **Frontend**: http://localhost:3000

---

## 📚 API Documentation

### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check and service info |
| `GET` | `/health` | Health check endpoint |
| `POST` | `/activities` | Log a new activity |
| `GET` | `/dashboard/{goal_id}` | Get goal dashboard |
| `GET` | `/insights/optimization` | Get productivity recommendations |

---

### 1️⃣ POST /activities

**Log a new activity toward a goal**

**Request Body:**

```json
{
  "goal_id": "career-growth-2024",
  "activity_type": "Learning",
  "value": 120,
  "timestamp": "2024-01-15T14:30:00Z"
}
```

**Response (201 Created):**

```json
{
  "activity_id": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "goal_id": "career-growth-2024",
  "activity_type": "Learning",
  "value": 120,
  "timestamp": "2024-01-15T14:30:00Z"
}
```

**Validation Rules:**
- `goal_id`: Non-empty string
- `activity_type`: Must be one of: `Learning`, `Health`, `Fitness`, `Other`
- `value`: Must be greater than 0
- `timestamp`: Valid ISO-8601 datetime string

---

### 2️⃣ GET /dashboard/{goal_id}

**Get comprehensive dashboard for a specific goal**

**Response (200 OK):**

```json
{
  "goal_id": "career-growth-2024",
  "total_activities": 15,
  "aggregated_values": {
    "Learning": 1800,
    "Health": 300,
    "Fitness": 450
  },
  "activity_history": [
    {
      "activity_id": "...",
      "goal_id": "career-growth-2024",
      "activity_type": "Learning",
      "value": 120,
      "timestamp": "2024-01-15T14:30:00Z"
    }
  ],
  "consistency_score": 0.82,
  "wellness_warning": false
}
```

**Metrics Included:**
- **total_activities**: Count of all activities for this goal
- **aggregated_values**: Sum of values by activity type
- **activity_history**: Chronologically sorted activity list
- **consistency_score**: 0.0 - 1.0 (based on consecutive days)
- **wellness_warning**: `true` if health activities < 150 min/week

---

### 3️⃣ GET /insights/optimization

**Get AI-generated productivity recommendations**

**Response (200 OK):**

```json
{
  "consistency_score": 0.82,
  "wellness_warning": true,
  "recommendation": "You are investing heavily in learning but neglecting physical wellness. Consider rebalancing your growth plan. Research shows that physical activity enhances cognitive performance and learning retention."
}
```

**Recommendation Logic:**
- Detects imbalance between learning and physical wellness
- Identifies low consistency patterns
- Flags wellness concerns
- Suggests actionable improvements

---

## 🧪 Example Requests

### Using cURL

**1. Log an Activity**

```bash
curl -X POST "https://life-design-dashboard.onrender.com/activities" \
  -H "Content-Type: application/json" \
  -d '{
    "goal_id": "fitness-2024",
    "activity_type": "Health",
    "value": 45,
    "timestamp": "2024-01-15T08:00:00Z"
  }'
```

**2. Get Goal Dashboard**

```bash
curl -X GET "https://life-design-dashboard.onrender.com/dashboard/fitness-2024"
```

**3. Get Insights**

```bash
curl -X GET "https://life-design-dashboard.onrender.com/insights/optimization"
```

### Using Python (httpx)

```python
import httpx

BASE_URL = "https://life-design-dashboard.onrender.com"

# Log activity
response = httpx.post(
    f"{BASE_URL}/activities",
    json={
        "goal_id": "learning-2024",
        "activity_type": "Learning",
        "value": 90,
        "timestamp": "2024-01-15T19:00:00Z"
    }
)
print(response.json())

# Get dashboard
dashboard = httpx.get(f"{BASE_URL}/dashboard/learning-2024")
print(dashboard.json())

# Get insights
insights = httpx.get(f"{BASE_URL}/insights/optimization")
print(insights.json())
```

---

## 📁 Project Structure

```
life-design-dashboard/
│
├── app/                             # Backend application
│   ├── main.py                      # FastAPI application entry point
│   │
│   ├── api/                         # API layer (HTTP endpoints)
│   │   ├── activities.py            # POST /activities
│   │   ├── dashboard.py             # GET /dashboard/{goal_id}
│   │   └── insights.py              # GET /insights/optimization
│   │
│   ├── models/                      # Domain models
│   │   └── activity.py              # Activity entity
│   │
│   ├── services/                    # Business logic layer
│   │   ├── analytics_service.py     # Metrics computation
│   │   └── recommendation_service.py # Insight generation
│   │
│   ├── repositories/                # Data access layer
│   │   ├── activity_repository.py   # Repository interface (ABC)
│   │   └── in_memory_repository.py  # In-memory implementation
│   │
│   ├── schemas/                     # Pydantic schemas
│   │   └── activity_schema.py       # Request/response models
│   │
│   └── utils/                       # Utility functions
│       └── date_helpers.py          # Date/time operations
│
├── frontend/                        # Frontend application
│   ├── index.html                   # Main HTML structure
│   ├── styles.css                   # Modern CSS with glassmorphism
│   ├── app.js                       # JavaScript application logic
│   ├── vercel.json                  # Vercel deployment config
│   └── README.md                    # Frontend documentation
│
├── requirements.txt                 # Python dependencies
├── Procfile                         # Heroku/Railway process file
├── runtime.txt                      # Python version specification
├── render.yaml                      # Render service configuration
├── DEPLOYMENT.md                    # Deployment guide
├── TECHNICAL_DESIGN.md              # Technical design document
└── README.md                        # This file
```

---

## 🌐 Deployment

### Live Deployments

**Frontend (Vercel):**
- Production URL: https://life-design-dashboard-frontend.vercel.app
- Automatic deployment on push to `main` branch
- Global CDN distribution
- HTTPS enabled

**Backend (Render):**
- Production URL: https://life-design-dashboard.onrender.com
- Automatic deployment on push to `main` branch
- API Documentation: https://life-design-dashboard.onrender.com/docs
- Free tier hosting

### Deployment Configuration

**Frontend (`frontend/vercel.json`):**
```json
{
    "cleanUrls": true,
    "trailingSlash": false
}
```

**Backend (`render.yaml`):**
```yaml
services:
  - type: web
    name: life-design-backend
    env: python
    buildCommand: pip install -r requirements.txt
    startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

### CORS Configuration

The backend is configured to accept requests from:
- Production frontend: `https://life-design-dashboard-frontend.vercel.app`
- Preview deployments: `https://life-design-dashboard-frontend-*.vercel.app`
- Local development: `http://localhost:3000`

---

## 🧠 Technical Rationale

### Consistency Score Algorithm

The consistency score uses an asymptotic normalization formula:

```
score = consecutive_days / (consecutive_days + 7)
```

**Rationale:**
- **Rewards consistency**: More consecutive days = higher score
- **Diminishing returns**: Prevents score inflation for very long streaks
- **Interpretable scale**: 0.0 (no activity) to 1.0 (perfect consistency)
- **Balanced thresholds**:
  - 7 consecutive days = 0.50
  - 14 consecutive days = 0.67
  - 21 consecutive days = 0.75

### Wellness Warning Logic

Checks if total `Health` activity in the last 7 days is below 150 minutes (WHO recommendation).

### Recommendation Engine

Rule-based system that detects:
1. Learning/Health imbalance (ratio > 3:1)
2. Low consistency (score < 0.3)
3. Missing activity categories
4. Wellness threshold violations

---

## 🎓 Key Features Demonstrated

| Skill Area | Implementation |
|------------|----------------|
| **Python Proficiency** | Type hints, list comprehensions, dataclasses |
| **API Design** | RESTful principles, proper HTTP status codes |
| **Business Logic** | Consistency algorithms, wellness detection |
| **System Design** | Modular architecture, repository pattern |
| **Data Interpretation** | Raw logs → actionable insights |
| **Frontend Development** | Modern UI/UX, responsive design, animations |
| **Full-Stack Integration** | API integration, CORS, deployment |
| **Code Quality** | Clean naming, documentation, error handling |

---

## 🚀 Future Enhancements

**Potential Improvements:**

1. **Authentication**: Add JWT-based user authentication
2. **Database**: Migrate to PostgreSQL with Alembic migrations
3. **Caching**: Implement Redis for dashboard caching
4. **Testing**: Add comprehensive unit and integration tests
5. **Monitoring**: Integrate Prometheus metrics and logging
6. **Mobile App**: React Native or Flutter mobile application
7. **Social Features**: Share progress with friends
8. **Gamification**: Achievements, badges, and leaderboards

---

## 👤 Author

**Mayank Sahu**

Demonstrating full-stack engineering excellence.

---

## 📞 Support

For questions or feedback:
- **API Documentation**: https://life-design-dashboard.onrender.com/docs
- **GitHub Repository**: https://github.com/MayankSahu297/life-design-dashboard

---

**Built with ❤️ using FastAPI, Python, HTML, CSS, and JavaScript**

*A complete full-stack demonstration of modern web development and backend engineering excellence.*
