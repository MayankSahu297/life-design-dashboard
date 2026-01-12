# 🚀 Life Design Dashboard - Full Stack Application

**Growth Journal & Productivity Insights Platform**

A complete full-stack application featuring a production-ready Python FastAPI backend and a stunning modern frontend, enabling users to log daily efforts toward life goals, visualize progress, and receive AI-powered productivity insights.

---

## 📋 Table of Contents

- [Quick Start](#quick-start)
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Architecture](#architecture)
- [Setup Instructions](#setup-instructions)
- [Frontend](#frontend)
- [Deployment](#deployment)
- [API Documentation](#api-documentation)
- [Example Requests](#example-requests)
- [Technical Rationale](#technical-rationale)
- [Project Structure](#project-structure)

---

## ⚡ Quick Start

### Run the Complete Application

**1. Start the Backend:**
```bash
# Navigate to project directory
cd "c:\Users\VICTUS\Documents\Technical Assessment The Life Design Backend"

# Install dependencies (if not already done)
pip install -r requirements.txt

# Run the backend server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

**2. Start the Frontend:**
```bash
# Open a new terminal
cd "c:\Users\VICTUS\Documents\Technical Assessment The Life Design Backend\frontend"

# Start local server
python -m http.server 3000
```

**3. Access the Application:**
- **Frontend:** http://localhost:3000
- **Backend API Docs:** http://localhost:8000/docs

---

## 🎯 Overview

This backend microservice demonstrates:

✅ **Strong Backend Engineering**: Clean architecture, modular design, type safety  
✅ **Data Interpretation**: Transforming raw logs into meaningful insights  
✅ **Scalable Design**: Repository pattern for easy database swapping  
✅ **Production-Ready**: Comprehensive validation, error handling, documentation

---

## ✨ Features

### Core Functionality

- **📝 Activity Logging**: Track efforts across Learning, Health, Fitness, and Other categories
- **📊 Goal Dashboards**: Aggregated metrics, activity history, consistency scores
- **🧠 Smart Insights**: AI-generated recommendations based on behavioral patterns
- **⚠️ Wellness Monitoring**: Automated alerts for insufficient health activities

### Technical Highlights

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
| **Architecture** | Microservice, Modular Design |

### Frontend
| Component | Technology |
|-----------|-----------|
| **Languages** | HTML5, CSS3, JavaScript (ES6+) |
| **Styling** | Vanilla CSS with Modern Design |
| **Design** | Glassmorphism, Gradients, Animations |
| **Architecture** | Single Page Application (SPA) |
| **API Integration** | Fetch API |

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

## 🚀 Setup Instructions

### Prerequisites

- Python 3.10 or higher
- pip (Python package manager)

### Installation

1. **Clone/Navigate to Project Directory**

```bash
cd "c:\Users\VICTUS\Documents\Technical Assessment The Life Design Backend"
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

4. **Run the Server**

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

---

## 🎨 Frontend

### Modern Web Application

The Life Design Dashboard features a stunning, production-ready frontend with:

**🎯 Key Features:**
- ✨ **Glassmorphism Design** with backdrop blur effects
- 🌈 **Gradient Backgrounds** with smooth animations
- 🌙 **Dark Theme** optimized for extended use
- 📱 **Fully Responsive** for all devices
- ⚡ **Micro-animations** for enhanced UX
- 🎨 **Premium Aesthetics** with vibrant color palettes

**📊 Three Main Views:**

1. **Dashboard View**
   - Goal selection and progress tracking
   - Activity breakdown with animated progress bars
   - Recent activity timeline
   - Consistency score and wellness status

2. **Log Activity View**
   - Beautiful form interface
   - Visual activity type selection
   - Real-time validation
   - Success feedback animations

3. **Insights View**
   - Circular progress visualization
   - Wellness status indicators
   - AI-powered personalized recommendations

### Running the Frontend

```bash
# Navigate to frontend directory
cd frontend

# Start local server
python -m http.server 3000

# Access at http://localhost:3000
```

### Frontend Structure

```
frontend/
├── index.html          # Main HTML structure
├── styles.css          # Modern CSS with glassmorphism
├── app.js             # JavaScript application logic
├── README.md          # Frontend documentation
├── vercel.json        # Vercel deployment config
└── netlify.toml       # Netlify deployment config
```

### Design Highlights

- **Color Palette:** Purple-blue gradients with activity-specific colors
- **Typography:** Inter for body, Outfit for headings (Google Fonts)
- **Animations:** Smooth transitions, hover effects, loading states
- **Accessibility:** Semantic HTML, proper ARIA labels
- **Performance:** Vanilla JS, no heavy frameworks

For detailed frontend documentation, see [`frontend/README.md`](frontend/README.md)

---

## 📚 API Documentation

### Endpoints Overview

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check and service info |
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
curl -X POST "http://localhost:8000/activities" \
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
curl -X GET "http://localhost:8000/dashboard/fitness-2024"
```

**3. Get Insights**

```bash
curl -X GET "http://localhost:8000/insights/optimization"
```

### Using Python (httpx)

```python
import httpx

# Log activity
response = httpx.post(
    "http://localhost:8000/activities",
    json={
        "goal_id": "learning-2024",
        "activity_type": "Learning",
        "value": 90,
        "timestamp": "2024-01-15T19:00:00Z"
    }
)
print(response.json())

# Get dashboard
dashboard = httpx.get("http://localhost:8000/dashboard/learning-2024")
print(dashboard.json())

# Get insights
insights = httpx.get("http://localhost:8000/insights/optimization")
print(insights.json())
```

---

## 🧠 Technical Rationale

### 1. Data Interpretation Logic Design

**Consistency Score Algorithm:**

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

**Wellness Warning Logic:**

Checks if total `Health` activity in the last 7 days is below 150 minutes (WHO recommendation).

**Recommendation Engine:**

Rule-based system that detects:
1. Learning/Health imbalance (ratio > 3:1)
2. Low consistency (score < 0.3)
3. Missing activity categories
4. Wellness threshold violations

---

### 2. Performance & Scalability

**Current Implementation (In-Memory):**

| Operation | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Save Activity | O(1) | O(1) |
| Find by Goal | O(n log n) | O(k) |
| Consistency Calc | O(n log n) | O(n) |
| Aggregation | O(n) | O(1) |

Where:
- `n` = total activities
- `k` = matching activities for a goal

**Scalability Considerations:**

1. **Efficient Filtering**: Uses list comprehensions and generator expressions
2. **Sorted Storage**: Activities sorted by timestamp for fast range queries
3. **Lazy Evaluation**: Metrics computed on-demand, not pre-cached
4. **Database-Ready**: Repository pattern allows seamless migration to:
   - PostgreSQL (indexed queries, JSONB aggregation)
   - MongoDB (document-based storage, aggregation pipeline)
   - Redis (caching layer for hot data)

**Future Optimizations:**
- Add caching for frequently accessed dashboards
- Implement pagination for large activity histories
- Use database indexes on `goal_id` and `timestamp`
- Background jobs for weekly wellness reports

---

### 3. Service Layer + Repository Pattern

**Why This Architecture?**

✅ **Separation of Concerns**
- API layer handles HTTP
- Service layer contains business logic
- Repository layer manages data access

✅ **Testability**
- Mock repositories for unit testing
- Test services independently of storage
- Integration tests with real repositories

✅ **Flexibility**
- Swap storage backends without changing business logic
- Add new services (e.g., NotificationService) easily
- Extend functionality without modifying existing code

✅ **Maintainability**
- Clear boundaries between layers
- Single Responsibility Principle
- Easy to locate and fix bugs

**Example: Swapping to PostgreSQL**

```python
# Create new repository implementation
class PostgresActivityRepository(ActivityRepository):
    def save(self, activity: Activity) -> Activity:
        # Use SQLAlchemy or asyncpg
        pass

# Update main.py
repository = PostgresActivityRepository(db_connection)
# All services and APIs work unchanged!
```

---

## 📁 Project Structure

```
app/
│── main.py                          # FastAPI application entry point
│
│── api/                             # API layer (HTTP endpoints)
│   ├── activities.py                # POST /activities
│   ├── dashboard.py                 # GET /dashboard/{goal_id}
│   └── insights.py                  # GET /insights/optimization
│
│── models/                          # Domain models
│   └── activity.py                  # Activity entity
│
│── services/                        # Business logic layer
│   ├── analytics_service.py         # Metrics computation
│   └── recommendation_service.py    # Insight generation
│
│── repositories/                    # Data access layer
│   ├── activity_repository.py       # Repository interface (ABC)
│   └── in_memory_repository.py      # In-memory implementation
│
│── schemas/                         # Pydantic schemas
│   └── activity_schema.py           # Request/response models
│
│── utils/                           # Utility functions
│   └── date_helpers.py              # Date/time operations
│
requirements.txt                     # Python dependencies
README.md                            # This file
```

---

## 🎓 Key Learnings Demonstrated

| Skill Area | Implementation |
|------------|----------------|
| **Python Proficiency** | Type hints, list comprehensions, dataclasses |
| **API Design** | RESTful principles, proper HTTP status codes |
| **Business Logic** | Consistency algorithms, wellness detection |
| **System Design** | Modular architecture, repository pattern |
| **Data Interpretation** | Raw logs → actionable insights |
| **Code Quality** | Clean naming, documentation, error handling |

---

## 🌐 Deployment

### Quick Deployment Guide

**Frontend Options:**
- ✅ **Vercel** (Recommended) - `vercel --prod`
- ✅ **Netlify** - Drag & drop or CLI
- ✅ **GitHub Pages** - Free static hosting
- ✅ **Render** - Static site hosting

**Backend Options:**
- ✅ **Render** (Recommended) - Free Python hosting
- ✅ **Railway** - Easy deployment with CLI
- ✅ **Heroku** - Classic PaaS platform

### Deployment Files Included

- `frontend/vercel.json` - Vercel configuration
- `frontend/netlify.toml` - Netlify configuration
- `Procfile` - Heroku/Railway process file
- `runtime.txt` - Python version specification
- `render.yaml` - Render service configuration

### Complete Deployment Guide

For detailed step-by-step deployment instructions for all platforms, see:

📖 **[DEPLOYMENT.md](DEPLOYMENT.md)** - Comprehensive deployment guide

This guide includes:
- Platform-specific instructions
- Environment configuration
- CORS setup
- Post-deployment testing
- Troubleshooting tips

---

## 🚀 Next Steps

**Potential Enhancements:**

1. **Authentication**: Add JWT-based user authentication
2. **Database**: Migrate to PostgreSQL with Alembic migrations
3. **Caching**: Implement Redis for dashboard caching
4. **Testing**: Add comprehensive unit and integration tests
5. **Monitoring**: Integrate Prometheus metrics and logging
6. **Deployment**: Dockerize and deploy to AWS/GCP/Azure

---

## 📝 License

This project is created as a technical assessment demonstration.

---

## 👤 Author

**Mayank Sahu**

Demonstrating backend engineering excellence for SDE roles.

---

## 📞 Support

For questions or feedback, please refer to the interactive API documentation at `/docs` when the server is running.

---

**Built with ❤️ using FastAPI, Python, HTML, CSS, and JavaScript**

*A complete full-stack demonstration of modern web development and backend engineering excellence.*

