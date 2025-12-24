# SmartAgri Authentication System Documentation

## 🎯 Overview
This document explains the secure authentication system implemented for SmartAgri using MongoDB, FastAPI, and bcrypt password hashing.

---

## 📁 Project Structure

```
SmartAgri-AI/
├── database.py           # MongoDB connection and configuration
├── models.py             # Pydantic data validation schemas
├── auth.py               # Authentication routes (register/login)
├── main_fastapi.py       # Main FastAPI application
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variables template
└── .env                  # Your actual configuration (create this)
```

---

## 🗄️ Database Schema

**Database:** `smartagri`  
**Collection:** `users`

### User Document Structure:
```javascript
{
  "_id": ObjectId("..."),              // MongoDB auto-generated ID
  "name": "John Doe",                  // User's full name
  "email": "john@example.com",         // Unique email address
  "hashed_password": "$2b$12$...",     // Bcrypt hashed password
  "role": "user",                      // User role (default: "user")
  "created_at": ISODate("..."),        // Account creation timestamp
  "last_login": ISODate("...")         // Last login timestamp (nullable)
}
```

**Indexes:**
- `email` field has a unique index to prevent duplicate registrations

---

## 🔐 Authentication Flow

### Registration Flow:
```
1. User submits: name, email, password
   ↓
2. Backend validates email format and password length
   ↓
3. Check if email already exists in database
   ↓
4. Hash password using bcrypt
   ↓
5. Store user document in MongoDB
   ↓
6. Return success message
```

### Login Flow:
```
1. User submits: email, password
   ↓
2. Find user by email in database
   ↓
3. Verify password using bcrypt comparison
   ↓
4. Update last_login timestamp
   ↓
5. Return success message with user info (excluding password)
```

---

## 🛠️ API Endpoints

### 1. Register New User
**Endpoint:** `POST /auth/register`

**Request Body:**
```json
{
  "name": "John Doe",
  "email": "john.doe@example.com",
  "password": "securePassword123"
}
```

**Success Response (201):**
```json
{
  "message": "User 'John Doe' registered successfully! Please login to continue."
}
```

**Error Responses:**
- `400 Bad Request`: Email already registered
- `422 Unprocessable Entity`: Invalid email format or password too short
- `500 Internal Server Error`: Database error

---

### 2. Login User
**Endpoint:** `POST /auth/login`

**Request Body:**
```json
{
  "email": "john.doe@example.com",
  "password": "securePassword123"
}
```

**Success Response (200):**
```json
{
  "message": "Login successful",
  "user": {
    "id": "507f1f77bcf86cd799439011",
    "name": "John Doe",
    "email": "john.doe@example.com",
    "role": "user"
  }
}
```

**Error Responses:**
- `401 Unauthorized`: Invalid email or password
- `422 Unprocessable Entity`: Invalid request format

---

### 3. Get Current User (Optional)
**Endpoint:** `GET /auth/users/me?email=user@example.com`

**Success Response (200):**
```json
{
  "id": "507f1f77bcf86cd799439011",
  "name": "John Doe",
  "email": "john.doe@example.com",
  "role": "user",
  "created_at": "2024-01-01T00:00:00",
  "last_login": "2024-01-15T10:30:00"
}
```

---

## 🔧 Setup Instructions

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Install and Start MongoDB

**Option A: Local MongoDB**
```bash
# Download and install from: https://www.mongodb.com/try/download/community
# Start MongoDB service
mongod
```

**Option B: MongoDB Atlas (Cloud)**
- Sign up at: https://www.mongodb.com/cloud/atlas
- Create a free cluster
- Get your connection string

### 3. Configure Environment Variables
```bash
# Copy example environment file
cp .env.example .env

# Edit .env with your MongoDB connection string
# For local: MONGODB_URL=mongodb://localhost:27017
# For Atlas: MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/
```

### 4. Run the Application
```bash
uvicorn main_fastapi:app --reload --host 0.0.0.0 --port 8000
```

### 5. Test the API
Visit: http://localhost:8000/docs (Interactive API documentation)

---

## 🔒 Security Features

### Password Hashing
- **Algorithm:** Bcrypt (industry-standard)
- **Rounds:** 12 (default, provides good balance of security and performance)
- **Salt:** Automatically generated per password

### Security Best Practices Implemented:
✅ Passwords are hashed before storage (never stored in plain text)  
✅ Bcrypt automatically handles salt generation  
✅ Email uniqueness enforced at database level  
✅ Input validation using Pydantic models  
✅ Sensitive data excluded from API responses  
✅ Environment variables for configuration  
✅ Proper error handling without leaking information  

---

## 🧪 Testing the API

### Using cURL:

**Register:**
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test User",
    "email": "test@example.com",
    "password": "test123456"
  }'
```

**Login:**
```bash
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "test123456"
  }'
```

### Using Python Requests:
```python
import requests

# Register
response = requests.post(
    "http://localhost:8000/auth/register",
    json={
        "name": "Test User",
        "email": "test@example.com",
        "password": "test123456"
    }
)
print(response.json())

# Login
response = requests.post(
    "http://localhost:8000/auth/login",
    json={
        "email": "test@example.com",
        "password": "test123456"
    }
)
print(response.json())
```

---

## 🚀 Next Steps (Optional Enhancements)

### JWT Token Authentication
For production-grade authentication, implement JWT tokens:
```python
# Add to requirements.txt
python-jose[cryptography]

# Implementation
from jose import JWTError, jwt
from datetime import datetime, timedelta

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
```

### Email Verification
Add email verification for new registrations

### Password Reset
Implement forgot password functionality

### Rate Limiting
Add rate limiting to prevent brute-force attacks

### Two-Factor Authentication (2FA)
Implement TOTP-based 2FA for enhanced security

---

## 📊 Code Quality

### Features:
- **Type Hints:** Full Python type annotations
- **Documentation:** Comprehensive docstrings
- **Validation:** Pydantic models for request/response validation
- **Error Handling:** Proper HTTP status codes and error messages
- **Async/Await:** Asynchronous operations for better performance
- **Separation of Concerns:** Modular code structure

---

## 🐛 Troubleshooting

### MongoDB Connection Error
**Problem:** `Failed to connect to MongoDB`  
**Solution:** 
- Ensure MongoDB is running: `mongod`
- Check MONGODB_URL in .env file
- Verify network connectivity (for MongoDB Atlas)

### Import Errors
**Problem:** `ModuleNotFoundError`  
**Solution:** 
```bash
pip install -r requirements.txt
```

### Email Already Registered
**Problem:** `400 Bad Request: Email already registered`  
**Solution:** Use a different email or login with existing credentials

### Password Validation
**Problem:** `422 Unprocessable Entity`  
**Solution:** Ensure password is at least 6 characters long

---

## 📞 Support

For issues or questions:
1. Check the FastAPI docs at `/docs` endpoint
2. Review MongoDB logs
3. Check environment variables in `.env`

---

## ✨ Summary

You now have a **production-ready authentication system** with:
- ✅ Secure password hashing (bcrypt)
- ✅ MongoDB integration
- ✅ Clean API design
- ✅ Input validation
- ✅ Proper error handling
- ✅ Modular code structure
- ✅ Interview-ready implementation

**Database:** `smartagri`  
**Collection:** `users`  
**Endpoints:** `/auth/register`, `/auth/login`, `/auth/users/me`
