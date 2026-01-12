# Quick Start Guide
## Life Design Backend Service

Get up and running in 5 minutes! 🚀

---

## Prerequisites

- Python 3.10 or higher
- pip (Python package manager)
- Terminal/Command Prompt

---

## Installation Steps

### 1. Navigate to Project Directory

```bash
cd "c:\Users\VICTUS\Documents\Technical Assessment The Life Design Backend"
```

### 2. (Optional) Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

Expected packages:
- fastapi
- uvicorn[standard]
- pydantic
- python-multipart

### 4. Start the Server

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

You should see:
```
INFO:     Uvicorn running on http://0.0.0.0:8000
INFO:     Application startup complete.
```

---

## Verify Installation

### Option 1: Browser

Open your browser and navigate to:
- **API Docs**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc
- **Health Check**: http://localhost:8000/health

### Option 2: Command Line

```bash
# Health check
curl http://localhost:8000/health

# Create an activity
curl -X POST "http://localhost:8000/activities" \
  -H "Content-Type: application/json" \
  -d '{
    "goal_id": "test-goal",
    "activity_type": "Learning",
    "value": 60,
    "timestamp": "2024-01-15T14:30:00Z"
  }'
```

### Option 3: Run Test Script

```bash
python test_api.py
```

This will:
- Create sample activities
- Test all endpoints
- Display formatted responses

---

## Quick API Reference

### 1. Create Activity

**Endpoint**: `POST /activities`

**Example**:
```json
{
  "goal_id": "career-2024",
  "activity_type": "Learning",
  "value": 120,
  "timestamp": "2024-01-15T14:30:00Z"
}
```

**Activity Types**: `Learning`, `Health`, `Fitness`, `Other`

### 2. Get Dashboard

**Endpoint**: `GET /dashboard/{goal_id}`

**Example**: `GET /dashboard/career-2024`

**Returns**:
- Total activities
- Aggregated values by type
- Activity history
- Consistency score
- Wellness warning

### 3. Get Insights

**Endpoint**: `GET /insights/optimization`

**Returns**:
- Consistency score (0.0 - 1.0)
- Wellness warning (true/false)
- Personalized recommendation

---

## Common Issues

### Issue: "Module not found"

**Solution**: Make sure you're in the project directory and dependencies are installed
```bash
pip install -r requirements.txt
```

### Issue: "Port 8000 already in use"

**Solution**: Use a different port
```bash
uvicorn app.main:app --reload --port 8001
```

### Issue: "Import error"

**Solution**: Ensure you're running from the project root directory where `app/` folder exists

---

## Next Steps

1. **Explore the API**: Open http://localhost:8000/docs
2. **Read the README**: See `README.md` for detailed documentation
3. **Review Technical Design**: Check `TECHNICAL_DESIGN.md` for architecture details
4. **Import Postman Collection**: Use `Life_Design_API.postman_collection.json`

---

## Project Structure

```
app/
├── main.py                    # FastAPI application
├── api/                       # API endpoints
│   ├── activities.py
│   ├── dashboard.py
│   └── insights.py
├── models/                    # Domain models
│   └── activity.py
├── services/                  # Business logic
│   ├── analytics_service.py
│   └── recommendation_service.py
├── repositories/              # Data access
│   ├── activity_repository.py
│   └── in_memory_repository.py
├── schemas/                   # Pydantic schemas
│   └── activity_schema.py
└── utils/                     # Utilities
    └── date_helpers.py
```

---

## Development Tips

### Auto-reload

The `--reload` flag watches for file changes and automatically restarts the server.

### Interactive Docs

FastAPI automatically generates interactive API documentation at `/docs`.
You can test endpoints directly from the browser!

### Type Checking

Run mypy for type checking:
```bash
pip install mypy
mypy app/
```

### Code Formatting

Use black for consistent formatting:
```bash
pip install black
black app/
```

---

## Support

For questions or issues:
1. Check the README.md
2. Review TECHNICAL_DESIGN.md
3. Explore the interactive docs at /docs

---

**Happy Coding! 🎉**
