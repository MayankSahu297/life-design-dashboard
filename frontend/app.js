// ===== CONFIGURATION =====
const API_BASE_URL = 'http://localhost:8000';

// ===== STATE MANAGEMENT =====
let currentView = 'dashboard';
let currentGoalId = '';

// ===== DOM ELEMENTS =====
const elements = {
    // Navigation
    navBtns: document.querySelectorAll('.nav-btn'),
    views: document.querySelectorAll('.view'),

    // Dashboard
    goalSelect: document.getElementById('goal-select'),
    loadDashboardBtn: document.getElementById('load-dashboard-btn'),
    dashboardContent: document.getElementById('dashboard-content'),
    dashboardEmpty: document.getElementById('dashboard-empty'),
    totalActivities: document.getElementById('total-activities'),
    consistencyScore: document.getElementById('consistency-score'),
    wellnessStatus: document.getElementById('wellness-status'),
    activityBreakdown: document.getElementById('activity-breakdown'),
    activityHistory: document.getElementById('activity-history'),

    // Log Activity
    activityForm: document.getElementById('activity-form'),
    activityGoalId: document.getElementById('activity-goal-id'),
    activityTimestamp: document.getElementById('activity-timestamp'),
    activitySuccess: document.getElementById('activity-success'),

    // Insights
    loadInsightsBtn: document.getElementById('load-insights-btn'),
    insightsContent: document.getElementById('insights-content'),
    consistencyPercentage: document.getElementById('consistency-percentage'),
    consistencyProgress: document.getElementById('consistency-progress'),
    wellnessIndicator: document.getElementById('wellness-indicator'),
    wellnessText: document.getElementById('wellness-text'),
    wellnessDescription: document.getElementById('wellness-description'),
    recommendationText: document.getElementById('recommendation-text'),

    // UI Elements
    toast: document.getElementById('toast'),
    toastMessage: document.getElementById('toast-message'),
    loadingOverlay: document.getElementById('loading-overlay')
};

// ===== INITIALIZATION =====
document.addEventListener('DOMContentLoaded', () => {
    initializeApp();
});

function initializeApp() {
    // Set default timestamp to now
    const now = new Date();
    now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
    elements.activityTimestamp.value = now.toISOString().slice(0, 16);

    // Event Listeners
    setupEventListeners();

    // Show initial view
    switchView('dashboard');
}

function setupEventListeners() {
    // Navigation
    elements.navBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const view = btn.dataset.view;
            switchView(view);
        });
    });

    // Dashboard
    elements.loadDashboardBtn.addEventListener('click', loadDashboard);

    // Log Activity
    elements.activityForm.addEventListener('submit', handleActivitySubmit);

    // Insights
    elements.loadInsightsBtn.addEventListener('click', loadInsights);
}

// ===== VIEW MANAGEMENT =====
function switchView(viewName) {
    currentView = viewName;

    // Update navigation
    elements.navBtns.forEach(btn => {
        if (btn.dataset.view === viewName) {
            btn.classList.add('active');
        } else {
            btn.classList.remove('active');
        }
    });

    // Update views
    elements.views.forEach(view => {
        if (view.id === `${viewName}-view`) {
            view.classList.add('active');
        } else {
            view.classList.remove('active');
        }
    });
}

// ===== API CALLS =====
async function apiCall(endpoint, options = {}) {
    showLoading();
    try {
        const response = await fetch(`${API_BASE_URL}${endpoint}`, {
            ...options,
            headers: {
                'Content-Type': 'application/json',
                ...options.headers
            }
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'API request failed');
        }

        const data = await response.json();
        hideLoading();
        return data;
    } catch (error) {
        hideLoading();
        showToast(error.message, 'error');
        throw error;
    }
}

// ===== DASHBOARD FUNCTIONS =====
async function loadDashboard() {
    const goalId = elements.goalSelect.value;

    if (!goalId) {
        showToast('Please select a goal', 'error');
        return;
    }

    currentGoalId = goalId;

    try {
        const data = await apiCall(`/dashboard/${goalId}`);
        displayDashboard(data);
    } catch (error) {
        console.error('Failed to load dashboard:', error);
    }
}

function displayDashboard(data) {
    // Show dashboard content
    elements.dashboardContent.classList.remove('hidden');
    elements.dashboardEmpty.classList.add('hidden');

    // Update stats
    elements.totalActivities.textContent = data.total_activities;
    elements.consistencyScore.textContent = `${Math.round(data.consistency_score * 100)}%`;
    elements.wellnessStatus.textContent = data.wellness_warning ? 'Needs Attention' : 'Good';
    elements.wellnessStatus.style.color = data.wellness_warning ? '#fa709a' : '#4facfe';

    // Display activity breakdown
    displayActivityBreakdown(data.aggregated_values);

    // Display activity history
    displayActivityHistory(data.activity_history);

    showToast('Dashboard loaded successfully', 'success');
}

function displayActivityBreakdown(aggregatedValues) {
    const total = Object.values(aggregatedValues).reduce((sum, val) => sum + val, 0);

    if (total === 0) {
        elements.activityBreakdown.innerHTML = '<p style="color: var(--text-secondary); text-align: center;">No activities logged yet</p>';
        return;
    }

    const activityTypes = ['Learning', 'Health', 'Fitness', 'Other'];
    const icons = {
        Learning: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>',
        Health: '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>',
        Fitness: '<path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>',
        Other: '<circle cx="12" cy="12" r="3"></circle><path d="M12 1v6m0 6v6m-6-6h6m6 0h6"></path>'
    };

    const html = activityTypes.map(type => {
        const value = aggregatedValues[type] || 0;
        const percentage = total > 0 ? (value / total * 100) : 0;

        if (value === 0) return '';

        return `
            <div class="activity-bar">
                <div class="activity-bar-header">
                    <div class="activity-bar-label">
                        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                            ${icons[type]}
                        </svg>
                        ${type}
                    </div>
                    <div class="activity-bar-value">${value} min</div>
                </div>
                <div class="activity-bar-track">
                    <div class="activity-bar-fill ${type.toLowerCase()}" style="width: ${percentage}%"></div>
                </div>
            </div>
        `;
    }).join('');

    elements.activityBreakdown.innerHTML = html;
}

function displayActivityHistory(activities) {
    if (activities.length === 0) {
        elements.activityHistory.innerHTML = '<p style="color: var(--text-secondary); text-align: center;">No activities logged yet</p>';
        return;
    }

    const icons = {
        Learning: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"></path><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"></path>',
        Health: '<path d="M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 0 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z"></path>',
        Fitness: '<path d="M22 12h-4l-3 9L9 3l-3 9H2"></path>',
        Other: '<circle cx="12" cy="12" r="3"></circle><path d="M12 1v6m0 6v6m-6-6h6m6 0h6"></path>'
    };

    const html = activities.slice().reverse().map(activity => {
        const date = new Date(activity.timestamp);
        const formattedDate = date.toLocaleDateString('en-US', {
            month: 'short',
            day: 'numeric',
            year: 'numeric'
        });
        const formattedTime = date.toLocaleTimeString('en-US', {
            hour: '2-digit',
            minute: '2-digit'
        });

        return `
            <div class="activity-item">
                <div class="activity-item-icon ${activity.activity_type.toLowerCase()}">
                    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                        ${icons[activity.activity_type]}
                    </svg>
                </div>
                <div class="activity-item-info">
                    <div class="activity-item-type">${activity.activity_type}</div>
                    <div class="activity-item-time">${formattedDate} at ${formattedTime}</div>
                </div>
                <div class="activity-item-value">${activity.value} min</div>
            </div>
        `;
    }).join('');

    elements.activityHistory.innerHTML = html;
}

// ===== LOG ACTIVITY FUNCTIONS =====
async function handleActivitySubmit(e) {
    e.preventDefault();

    const formData = new FormData(elements.activityForm);
    const activityType = formData.get('activity-type');
    const goalId = elements.activityGoalId.value;
    const value = parseInt(document.getElementById('activity-value').value);
    const timestamp = new Date(elements.activityTimestamp.value).toISOString();

    const activityData = {
        goal_id: goalId,
        activity_type: activityType,
        value: value,
        timestamp: timestamp
    };

    try {
        await apiCall('/activities', {
            method: 'POST',
            body: JSON.stringify(activityData)
        });

        // Show success message
        elements.activityForm.classList.add('hidden');
        elements.activitySuccess.classList.remove('hidden');

        // Reset form after 3 seconds
        setTimeout(() => {
            elements.activityForm.reset();
            elements.activityForm.classList.remove('hidden');
            elements.activitySuccess.classList.add('hidden');

            // Reset timestamp to now
            const now = new Date();
            now.setMinutes(now.getMinutes() - now.getTimezoneOffset());
            elements.activityTimestamp.value = now.toISOString().slice(0, 16);
        }, 3000);

        showToast('Activity logged successfully!', 'success');
    } catch (error) {
        console.error('Failed to log activity:', error);
    }
}

// ===== INSIGHTS FUNCTIONS =====
async function loadInsights() {
    try {
        const data = await apiCall('/insights/optimization');
        displayInsights(data);
    } catch (error) {
        console.error('Failed to load insights:', error);
    }
}

function displayInsights(data) {
    // Show insights content
    elements.insightsContent.classList.remove('hidden');

    // Update consistency score
    const consistencyPercent = Math.round(data.consistency_score * 100);
    elements.consistencyPercentage.textContent = `${consistencyPercent}%`;

    // Animate circular progress
    const circumference = 2 * Math.PI * 50; // radius = 50
    const offset = circumference - (consistencyPercent / 100) * circumference;
    elements.consistencyProgress.style.strokeDashoffset = offset;

    // Add gradient definition if not exists
    if (!document.querySelector('#progressGradient')) {
        const svg = elements.consistencyProgress.closest('svg');
        const defs = document.createElementNS('http://www.w3.org/2000/svg', 'defs');
        defs.innerHTML = `
            <linearGradient id="progressGradient" x1="0%" y1="0%" x2="100%" y2="100%">
                <stop offset="0%" style="stop-color:#667eea;stop-opacity:1" />
                <stop offset="100%" style="stop-color:#764ba2;stop-opacity:1" />
            </linearGradient>
        `;
        svg.insertBefore(defs, svg.firstChild);
    }

    // Update wellness status
    if (data.wellness_warning) {
        elements.wellnessIndicator.classList.remove('good');
        elements.wellnessIndicator.classList.add('warning');
        elements.wellnessText.textContent = 'Needs Attention';
        elements.wellnessDescription.textContent = 'Health activities below recommended threshold';
        elements.wellnessIndicator.querySelector('svg').innerHTML = `
            <circle cx="12" cy="12" r="10"></circle>
            <line x1="12" y1="8" x2="12" y2="12"></line>
            <line x1="12" y1="16" x2="12.01" y2="16"></line>
        `;
    } else {
        elements.wellnessIndicator.classList.remove('warning');
        elements.wellnessIndicator.classList.add('good');
        elements.wellnessText.textContent = 'Good';
        elements.wellnessDescription.textContent = 'Meeting recommended health activity levels';
        elements.wellnessIndicator.querySelector('svg').innerHTML = `
            <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
            <polyline points="22 4 12 14.01 9 11.01"></polyline>
        `;
    }

    // Update recommendation
    elements.recommendationText.textContent = data.recommendation;

    showToast('Insights generated successfully', 'success');
}

// ===== UI HELPER FUNCTIONS =====
function showLoading() {
    elements.loadingOverlay.classList.remove('hidden');
}

function hideLoading() {
    elements.loadingOverlay.classList.add('hidden');
}

function showToast(message, type = 'success') {
    elements.toastMessage.textContent = message;
    elements.toast.classList.remove('hidden', 'error', 'success');
    elements.toast.classList.add(type);

    setTimeout(() => {
        elements.toast.classList.add('hidden');
    }, 3000);
}

// ===== UTILITY FUNCTIONS =====
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

function formatMinutes(minutes) {
    if (minutes < 60) {
        return `${minutes} min`;
    }
    const hours = Math.floor(minutes / 60);
    const mins = minutes % 60;
    return mins > 0 ? `${hours}h ${mins}m` : `${hours}h`;
}

// ===== ERROR HANDLING =====
window.addEventListener('error', (event) => {
    console.error('Global error:', event.error);
    showToast('An unexpected error occurred', 'error');
});

window.addEventListener('unhandledrejection', (event) => {
    console.error('Unhandled promise rejection:', event.reason);
    showToast('An unexpected error occurred', 'error');
});
