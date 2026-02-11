# 🚢 Maritime Vessel Tracking System - Backend API

## 📋 Project Overview

A comprehensive Django REST API backend for real-time maritime vessel tracking, voyage management, and port analytics. This system enables operators to monitor vessel movements, manage cargo operations, and track voyages across global shipping routes.

### Key Features
- 🔐 **JWT Authentication** - Secure user registration and login
- 🚢 **Vessel Management** - Track ships with IMO numbers, positions, and speeds
- ⚓ **Port Operations** - Manage global port database with coordinates
- 🗺️ **Voyage Tracking** - Monitor departure, arrival, and voyage status
- 👥 **Role-Based Access** - Operator, Analyst, and Admin roles
- 📊 **RESTful API** - Clean, documented endpoints
- 🔄 **Real-time Updates** - Live position and status tracking

---

## 🛠️ Technology Stack

| Component | Technology |
|-----------|-----------|
| **Framework** | Django 6.0.2 |
| **API** | Django REST Framework 3.16.1 |
| **Authentication** | JWT (djangorestframework-simplejwt 5.5.1) |
| **Database** | SQLite (Dev) / PostgreSQL (Production) |
| **CORS Handling** | django-cors-headers 4.9.0 |
| **Python Version** | 3.11+ |

---

## 📁 Project Structure
```
backend/
├── maritime_backend/          # Django project configuration
│   ├── __init__.py
│   ├── settings.py           # Project settings & configurations
│   ├── urls.py               # Root URL routing
│   ├── wsgi.py               # WSGI application
│   └── asgi.py               # ASGI application
│
├── vessels/                   # Main application
│   ├── migrations/           # Database migrations
│   ├── __init__.py
│   ├── models.py             # Data models (User, Vessel, Port, Voyage, Notification)
│   ├── serializers.py        # DRF serializers for API responses
│   ├── views.py              # API view logic
│   ├── urls.py               # App-specific URL routing
│   ├── admin.py              # Django admin configurations
│   ├── apps.py               # App configuration
│   └── tests.py              # Unit tests
│
├── manage.py                  # Django management script
├── requirements.txt           # Python dependencies
├── .gitignore                # Git ignore rules
└── README.md                 # This file
```

---

## 🚀 Getting Started

### Prerequisites

Before you begin, ensure you have the following installed:
- **Python 3.8+** ([Download here](https://www.python.org/downloads/))
- **pip** (comes with Python)
- **Git** ([Download here](https://git-scm.com/downloads))
- **Code Editor** (VS Code recommended)

### Installation & Setup

Follow these steps carefully:

#### **1. Clone the Repository**
```bash
# Clone the project
git clone https://github.com/springboardmentor0018/Maritime-Vessel-Tracking_Feb-26_Team-A.git

# Navigate to the project
cd Maritime-Vessel-Tracking_Feb-26_Team-A

# Switch to the backend branch
git checkout Milestone-1

# Navigate to backend folder
cd backend
```

#### **2. Create Virtual Environment**

**Windows:**
```bash
python -m venv env
env\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv env
source env/bin/activate
```

**✅ You'll know it's activated when you see `(env)` at the start of your terminal line**

#### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

#### **4. Configure Database**
```bash
# Create database tables
python manage.py makemigrations
python manage.py migrate
```

#### **5. Create Admin User (Optional)**
```bash
python manage.py createsuperuser
```
Follow the prompts to create your admin account.

#### **6. Run Development Server**
```bash
python manage.py runserver
```

**✅ Success! Your server is running at:** `http://127.0.0.1:8000/`

---

## 🔗 API Endpoints

### Base URL
```
http://localhost:8000/api/
```

### Authentication Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/api/auth/register/` | Register new user | ❌ |
| `POST` | `/api/auth/login/` | Login & get JWT tokens | ❌ |
| `POST` | `/api/auth/token/refresh/` | Refresh access token | ❌ |
| `GET` | `/api/auth/profile/` | Get user profile | ✅ |
| `PUT` | `/api/auth/profile/` | Update user profile | ✅ |

### Vessel Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/vessels/` | List all vessels | ❌ |
| `POST` | `/api/vessels/` | Create new vessel | ✅ |
| `GET` | `/api/vessels/{id}/` | Get vessel details | ❌ |
| `PUT` | `/api/vessels/{id}/` | Update vessel | ✅ |
| `DELETE` | `/api/vessels/{id}/` | Delete vessel | ✅ |

### Port Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/ports/` | List all ports | ❌ |
| `POST` | `/api/ports/` | Create new port | ✅ |
| `GET` | `/api/ports/{id}/` | Get port details | ❌ |
| `PUT` | `/api/ports/{id}/` | Update port | ✅ |
| `DELETE` | `/api/ports/{id}/` | Delete port | ✅ |

### Voyage Endpoints

| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/voyages/` | List all voyages | ❌ |
| `POST` | `/api/voyages/` | Create new voyage | ✅ |
| `GET` | `/api/voyages/{id}/` | Get voyage details | ❌ |
| `PUT` | `/api/voyages/{id}/` | Update voyage | ✅ |
| `DELETE` | `/api/voyages/{id}/` | Delete voyage | ✅ |

---

## 📊 Data Models

### User Model
```python
- username (unique)
- email
- role (operator/analyst/admin)
- company
- phone
```

### Vessel Model
```python
- imo_number (unique)
- name
- vessel_type (cargo/tanker/passenger/fishing)
- cargo_type (container/bulk/liquid/general)
- flag
- operator
- current_latitude
- current_longitude
- current_speed
- destination
- eta
```

### Port Model
```python
- code (unique)
- name
- country
- latitude
- longitude
```

### Voyage Model
```python
- vessel (ForeignKey)
- origin_port (ForeignKey)
- destination_port (ForeignKey)
- departure_time
- arrival_time
- status (scheduled/in_progress/completed/delayed)
```

### Notification Model
```python
- user (ForeignKey)
- title
- message
- notification_type (alert/info/warning)
- is_read
- created_at
```

---

## 🧪 Testing the API

### Using Django Admin Panel
1. Navigate to `http://127.0.0.1:8000/admin/`
2. Login with your superuser credentials
3. Add test data for Vessels, Ports, and Voyages

### Using Postman or Thunder Client

**Example: Register a User**
```http
POST http://localhost:8000/api/auth/register/
Content-Type: application/json

{
  "username": "johndoe",
  "email": "john@example.com",
  "password": "securepass123",
  "password_confirm": "securepass123",
  "role": "operator",
  "company": "Ocean Shipping Co",
  "phone": "+1234567890"
}
```

**Example: Login**
```http
POST http://localhost:8000/api/auth/login/
Content-Type: application/json

{
  "username": "johndoe",
  "password": "securepass123"
}
```

**Example: Create a Vessel (Requires Authentication)**
```http
POST http://localhost:8000/api/vessels/
Authorization: Bearer YOUR_ACCESS_TOKEN
Content-Type: application/json

{
  "imo_number": "IMO9876543",
  "name": "Ocean Pioneer",
  "vessel_type": "cargo",
  "cargo_type": "container",
  "flag": "USA",
  "operator": "Global Shipping Inc",
  "current_latitude": 40.7128,
  "current_longitude": -74.0060,
  "current_speed": 15.5,
  "destination": "Port of Rotterdam",
  "eta": "2026-02-20T14:30:00Z"
}
```

---

## 🔒 Security Configuration

### Important Settings (for Production)

**⚠️ Before deploying to production:**

1. **Change SECRET_KEY** in `settings.py`
2. **Set DEBUG = False**
3. **Configure ALLOWED_HOSTS**
4. **Use PostgreSQL instead of SQLite**
5. **Set up HTTPS**
6. **Configure proper CORS origins**

---

## 🤝 Team Collaboration Guide

### Before Starting Work
```bash
# Always pull latest changes first
git checkout Milestone-1
git pull origin Milestone-1
```

### After Making Changes
```bash
# Check what files changed
git status

# Stage your changes
git add .

# Commit with a clear message
git commit -m "Add: Feature description"

# Push to GitHub
git push origin Milestone-1
```

### Commit Message Conventions
- `Add:` - New features
- `Fix:` - Bug fixes
- `Update:` - Modifications to existing features
- `Remove:` - Deleted files/features
- `Docs:` - Documentation changes

---

## 🐛 Troubleshooting

### Common Issues & Solutions

**❌ Problem:** `Module not found` errors
```bash
✅ Solution: 
# Ensure virtual environment is activated
# You should see (env) in your terminal

# Reinstall dependencies
pip install -r requirements.txt
```

**❌ Problem:** Database errors
```bash
✅ Solution:
# Delete db.sqlite3 (if it exists)
# Run migrations again
python manage.py makemigrations
python manage.py migrate
```

**❌ Problem:** Port already in use
```bash
✅ Solution:
# Run on a different port
python manage.py runserver 8001
```

**❌ Problem:** CORS errors from frontend
```bash
✅ Solution:
# Check settings.py - ensure your frontend URL is in:
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]
```

**❌ Problem:** JWT token expired
```bash
✅ Solution:
# Use the refresh token to get a new access token
POST /api/auth/token/refresh/
{
  "refresh": "YOUR_REFRESH_TOKEN"
}
```

---

## 📚 Additional Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [JWT Authentication](https://django-rest-framework-simplejwt.readthedocs.io/)
- [Git Basics](https://git-scm.com/doc)

---

## 👥 Team Members

**Team A(Anindita dutta) - Infosys Springboard Internship Program**

---

## 📄 License

This project is licensed under the MIT License.

---

## 📞 Support

For questions or issues:
- Open an issue on GitHub
- Contact team lead
- Check documentation

---

**Happy Coding! 🚀**