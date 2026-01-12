# 🚀 Deployment Guide - Life Design Dashboard

Complete guide to deploy both the frontend and backend of the Life Design Dashboard application.

## 📋 Table of Contents

- [Overview](#overview)
- [Frontend Deployment](#frontend-deployment)
  - [Vercel (Recommended)](#vercel-recommended)
  - [Netlify](#netlify)
  - [GitHub Pages](#github-pages)
  - [Render](#render)
- [Backend Deployment](#backend-deployment)
  - [Render (Recommended)](#render-backend)
  - [Railway](#railway)
  - [Heroku](#heroku)
- [Environment Configuration](#environment-configuration)
- [Post-Deployment Steps](#post-deployment-steps)

---

## 🎯 Overview

The Life Design Dashboard consists of two parts:
1. **Frontend:** Static HTML/CSS/JavaScript application
2. **Backend:** FastAPI Python application

Both need to be deployed separately and then connected.

---

## 🎨 Frontend Deployment

### Vercel (Recommended)

**Why Vercel?**
- ✅ Free tier available
- ✅ Automatic HTTPS
- ✅ Global CDN
- ✅ Easy deployment
- ✅ Custom domains

**Steps:**

1. **Install Vercel CLI:**
   ```bash
   npm install -g vercel
   ```

2. **Navigate to frontend directory:**
   ```bash
   cd "c:\Users\VICTUS\Documents\Technical Assessment The Life Design Backend\frontend"
   ```

3. **Login to Vercel:**
   ```bash
   vercel login
   ```

4. **Deploy:**
   ```bash
   vercel
   ```

5. **Follow prompts:**
   - Set up and deploy? `Y`
   - Which scope? (Select your account)
   - Link to existing project? `N`
   - Project name? `life-design-dashboard`
   - Directory? `./`
   - Override settings? `N`

6. **Production deployment:**
   ```bash
   vercel --prod
   ```

**Your frontend will be live at:** `https://life-design-dashboard.vercel.app`

---

### Netlify

**Steps:**

1. **Install Netlify CLI:**
   ```bash
   npm install -g netlify-cli
   ```

2. **Navigate to frontend:**
   ```bash
   cd "c:\Users\VICTUS\Documents\Technical Assessment The Life Design Backend\frontend"
   ```

3. **Login:**
   ```bash
   netlify login
   ```

4. **Deploy:**
   ```bash
   netlify deploy
   ```

5. **For production:**
   ```bash
   netlify deploy --prod
   ```

**Alternative: Drag & Drop**
1. Go to [Netlify Drop](https://app.netlify.com/drop)
2. Drag the `frontend` folder
3. Get instant deployment

---

### GitHub Pages

**Steps:**

1. **Create GitHub repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/life-design-dashboard.git
   git push -u origin main
   ```

2. **Enable GitHub Pages:**
   - Go to repository Settings
   - Navigate to Pages section
   - Source: Deploy from branch
   - Branch: `main`, Folder: `/frontend`
   - Save

3. **Access your site:**
   ```
   https://YOUR_USERNAME.github.io/life-design-dashboard/
   ```

---

### Render

**Steps:**

1. **Create account:** [render.com](https://render.com)

2. **Create New Static Site:**
   - Click "New +"
   - Select "Static Site"
   - Connect GitHub repository (or use manual deploy)

3. **Configure:**
   - Name: `life-design-dashboard`
   - Root Directory: `frontend`
   - Build Command: (leave empty)
   - Publish Directory: `.`

4. **Deploy:**
   - Click "Create Static Site"

---

## ⚙️ Backend Deployment

### Render (Backend)

**Why Render?**
- ✅ Free tier for web services
- ✅ Automatic HTTPS
- ✅ Easy Python deployment
- ✅ Environment variables support

**Steps:**

1. **Create `requirements.txt`** (already exists in your project)

2. **Create `render.yaml`:**
   ```yaml
   services:
     - type: web
       name: life-design-backend
       env: python
       buildCommand: pip install -r requirements.txt
       startCommand: uvicorn app.main:app --host 0.0.0.0 --port $PORT
       envVars:
         - key: PYTHON_VERSION
           value: 3.10.0
   ```

3. **Deploy on Render:**
   - Go to [render.com](https://render.com)
   - Click "New +"
   - Select "Web Service"
   - Connect GitHub repository
   - Configure:
     - Name: `life-design-backend`
     - Environment: `Python 3`
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
   - Click "Create Web Service"

**Your backend will be live at:** `https://life-design-backend.onrender.com`

---

### Railway

**Steps:**

1. **Install Railway CLI:**
   ```bash
   npm install -g @railway/cli
   ```

2. **Login:**
   ```bash
   railway login
   ```

3. **Initialize project:**
   ```bash
   cd "c:\Users\VICTUS\Documents\Technical Assessment The Life Design Backend"
   railway init
   ```

4. **Deploy:**
   ```bash
   railway up
   ```

5. **Add domain:**
   ```bash
   railway domain
   ```

---

### Heroku

**Steps:**

1. **Install Heroku CLI**

2. **Create `Procfile`:**
   ```
   web: uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

3. **Create `runtime.txt`:**
   ```
   python-3.10.0
   ```

4. **Deploy:**
   ```bash
   heroku login
   heroku create life-design-backend
   git push heroku main
   ```

---

## 🔧 Environment Configuration

### Update Frontend API URL

After deploying the backend, update the frontend to connect to it:

1. **Edit `frontend/app.js`:**
   ```javascript
   // Change this line:
   const API_BASE_URL = 'http://localhost:8000';
   
   // To your deployed backend URL:
   const API_BASE_URL = 'https://life-design-backend.onrender.com';
   ```

2. **Redeploy frontend:**
   ```bash
   cd frontend
   vercel --prod
   ```

### Update Backend CORS

Update `app/main.py` to allow your frontend domain:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://life-design-dashboard.vercel.app",  # Your frontend URL
        "http://localhost:3000"  # Keep for local development
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## ✅ Post-Deployment Steps

### 1. Test the Application

**Frontend:**
- ✅ Navigate to your frontend URL
- ✅ Check all three views (Dashboard, Log Activity, Insights)
- ✅ Verify navigation works

**Backend:**
- ✅ Visit `https://your-backend-url.com/docs`
- ✅ Test API endpoints in Swagger UI
- ✅ Verify CORS is configured correctly

### 2. Test Integration

1. **Log an Activity:**
   - Go to "Log Activity"
   - Fill out the form
   - Submit
   - Check for success message

2. **View Dashboard:**
   - Select a goal
   - Click "Load Dashboard"
   - Verify data displays correctly

3. **Generate Insights:**
   - Click "Insights"
   - Click "Generate Insights"
   - Verify recommendations appear

### 3. Monitor Performance

**Frontend:**
- Check loading times
- Test on different devices
- Verify responsive design

**Backend:**
- Monitor API response times
- Check logs for errors
- Verify all endpoints work

---

## 🎯 Quick Deployment Checklist

### Before Deployment:
- [ ] Backend runs locally without errors
- [ ] Frontend connects to local backend successfully
- [ ] All features tested locally
- [ ] CORS configured properly

### Frontend Deployment:
- [ ] Choose hosting platform (Vercel recommended)
- [ ] Deploy frontend
- [ ] Get frontend URL
- [ ] Test frontend loads correctly

### Backend Deployment:
- [ ] Choose hosting platform (Render recommended)
- [ ] Deploy backend
- [ ] Get backend URL
- [ ] Test `/docs` endpoint works

### Integration:
- [ ] Update `API_BASE_URL` in frontend
- [ ] Update CORS in backend
- [ ] Redeploy both
- [ ] Test full application flow
- [ ] Verify all features work

---

## 🚨 Troubleshooting

### Frontend Issues

**Problem:** Blank page after deployment
- **Solution:** Check browser console for errors
- **Solution:** Verify all file paths are correct
- **Solution:** Check if API URL is correct

**Problem:** API calls failing
- **Solution:** Check CORS configuration
- **Solution:** Verify backend is running
- **Solution:** Check API_BASE_URL in app.js

### Backend Issues

**Problem:** 500 Internal Server Error
- **Solution:** Check backend logs
- **Solution:** Verify all dependencies installed
- **Solution:** Check Python version compatibility

**Problem:** CORS errors
- **Solution:** Add frontend domain to allow_origins
- **Solution:** Ensure credentials are allowed
- **Solution:** Check HTTP vs HTTPS

---

## 📞 Support Resources

- **Vercel Docs:** https://vercel.com/docs
- **Netlify Docs:** https://docs.netlify.com
- **Render Docs:** https://render.com/docs
- **FastAPI Docs:** https://fastapi.tiangolo.com
- **Railway Docs:** https://docs.railway.app

---

## 🎉 Success!

Once deployed, you'll have:
- ✅ Live frontend accessible worldwide
- ✅ Live backend API with documentation
- ✅ Fully functional Life Design Dashboard
- ✅ HTTPS security
- ✅ Professional deployment

**Share your deployment:**
- Frontend: `https://your-app.vercel.app`
- Backend API: `https://your-api.onrender.com`
- API Docs: `https://your-api.onrender.com/docs`

---

**Built with ❤️ by Mayank Sahu**
