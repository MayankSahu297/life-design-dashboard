# 🎨 Life Design Dashboard - Frontend

A stunning, modern web application for tracking personal growth, visualizing goal progress, and receiving AI-powered productivity insights.

## ✨ Features

### 📊 **Interactive Dashboard**
- Real-time goal progress visualization
- Activity breakdown with animated progress bars
- Comprehensive activity history timeline
- Consistency score tracking
- Wellness status monitoring

### 📝 **Activity Logging**
- Beautiful, intuitive form interface
- Visual activity type selection (Learning, Health, Fitness, Other)
- Real-time validation
- Instant success feedback

### 🧠 **AI-Powered Insights**
- Circular progress visualization for consistency scores
- Wellness status indicators
- Personalized recommendations based on activity patterns
- Balance detection and improvement suggestions

### 🎨 **Modern Design**
- **Glassmorphism** effects with backdrop blur
- **Gradient backgrounds** with smooth animations
- **Dark theme** optimized for extended use
- **Micro-animations** for enhanced user experience
- **Responsive design** for all devices
- **Premium aesthetics** with vibrant color palettes

## 🚀 Quick Start

### Prerequisites
- Python 3.7+ (for local development server)
- Modern web browser (Chrome, Firefox, Safari, Edge)
- Backend API running on `http://localhost:8000`

### Running Locally

1. **Navigate to frontend directory:**
   ```bash
   cd "c:\Users\VICTUS\Documents\Technical Assessment The Life Design Backend\frontend"
   ```

2. **Start local server:**
   ```bash
   python -m http.server 3000
   ```

3. **Open in browser:**
   ```
   http://localhost:3000
   ```

### Backend Connection

The frontend connects to the backend API at `http://localhost:8000`. Make sure your backend is running:

```bash
cd "c:\Users\VICTUS\Documents\Technical Assessment The Life Design Backend"
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## 📁 Project Structure

```
frontend/
├── index.html          # Main HTML structure
├── styles.css          # Complete styling with modern design
├── app.js             # JavaScript application logic
└── README.md          # This file
```

## 🎯 Usage Guide

### 1. **View Dashboard**
- Select a goal from the dropdown menu
- Click "Load Dashboard" to view progress
- See total activities, consistency score, and wellness status
- Review activity breakdown by type
- Browse recent activity history

### 2. **Log Activity**
- Click "Log Activity" in navigation
- Select your goal
- Choose activity type (Learning, Health, Fitness, Other)
- Enter time spent in minutes
- Select date and time
- Submit to log activity

### 3. **View Insights**
- Click "Insights" in navigation
- Click "Generate Insights" button
- View consistency score with circular progress
- Check wellness status indicator
- Read personalized recommendations

## 🎨 Design System

### Color Palette
- **Primary Gradient:** Purple to Blue (`#667eea` → `#764ba2`)
- **Learning:** Purple gradient
- **Health:** Pink gradient
- **Fitness:** Blue gradient
- **Other:** Green gradient

### Typography
- **Headings:** Outfit (Google Fonts)
- **Body:** Inter (Google Fonts)

### Effects
- Glassmorphism with backdrop blur
- Smooth transitions (0.3s ease)
- Hover animations
- Loading states
- Toast notifications

## 🌐 Deployment Options

### Option 1: Vercel (Recommended)

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Deploy:**
   ```bash
   cd frontend
   vercel
   ```

3. **Update API URL:**
   - Edit `app.js`
   - Change `API_BASE_URL` to your deployed backend URL

### Option 2: Netlify

1. **Install Netlify CLI:**
   ```bash
   npm install -g netlify-cli
   ```

2. **Deploy:**
   ```bash
   cd frontend
   netlify deploy
   ```

### Option 3: GitHub Pages

1. **Create repository and push code**
2. **Enable GitHub Pages in repository settings**
3. **Select branch and folder**
4. **Update API URL in `app.js`**

### Option 4: Render

1. **Create new Static Site on Render**
2. **Connect GitHub repository**
3. **Set publish directory to `frontend`**
4. **Deploy**

## 🔧 Configuration

### API Base URL

To change the backend API URL, edit `app.js`:

```javascript
const API_BASE_URL = 'https://your-backend-url.com';
```

### CORS Configuration

Ensure your backend allows requests from your frontend domain. In the backend `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://your-frontend-url.com"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## 📱 Responsive Design

The application is fully responsive and optimized for:
- **Desktop:** Full feature set with optimal layout
- **Tablet:** Adapted grid layouts
- **Mobile:** Stacked layouts with touch-friendly controls

## ✅ Browser Compatibility

- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Safari 14+
- ✅ Edge 90+

## 🎯 Key Features Implemented

### User Experience
- ✅ Smooth page transitions
- ✅ Loading states with spinner overlay
- ✅ Toast notifications for feedback
- ✅ Form validation
- ✅ Error handling
- ✅ Empty states

### Visual Design
- ✅ Glassmorphism effects
- ✅ Gradient backgrounds
- ✅ Animated progress bars
- ✅ Circular progress indicators
- ✅ Hover effects
- ✅ Micro-animations

### Functionality
- ✅ Real-time data fetching
- ✅ Dynamic content rendering
- ✅ Form submission
- ✅ Data visualization
- ✅ Multi-view navigation

## 🚀 Performance

- **Lightweight:** No heavy frameworks
- **Fast Loading:** Minimal dependencies
- **Optimized:** Efficient DOM manipulation
- **Smooth:** Hardware-accelerated animations

## 📄 License

This project is created as a technical assessment demonstration.

## 👤 Author

**Mayank Sahu**

Demonstrating frontend excellence with modern web technologies.

---

**Built with ❤️ using HTML, CSS, and Vanilla JavaScript**
