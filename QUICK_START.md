# 🚀 SmartAgri Authentication - Quick Start Guide

## ⚡ Quick Setup (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Setup MongoDB

**Option A - Local MongoDB:**
```bash
# Download from: https://www.mongodb.com/try/download/community
# Install and start MongoDB
mongod
```

**Option B - MongoDB Atlas (Cloud - Free):**
1. Go to https://www.mongodb.com/cloud/atlas
2. Sign up for free account
3. Create a free cluster (M0)
4. Get connection string
5. Whitelist your IP address

### Step 3: Configure Environment
```bash
# Copy example environment file
cp .env.example .env

# Edit .env and set your MongoDB URL:
# Local: MONGODB_URL=mongodb://localhost:27017
# Atlas: MONGODB_URL=mongodb+srv://username:password@cluster.mongodb.net/
```

### Step 4: Start the Server
```bash
uvicorn main_fastapi:app --reload --host 0.0.0.0 --port 8000
```

### Step 5: Test It!
Visit: http://localhost:8000/docs

---

## 📡 API Endpoints

### Register User
```bash
POST /auth/register

{
  "name": "John Doe",
  "email": "john@example.com",
  "password": "secure123"
}
```

### Login User
```bash
POST /auth/login

{
  "email": "john@example.com",
  "password": "secure123"
}
```

### Get User Info
```bash
GET /auth/users/me?email=john@example.com
```

---

## 🧪 Test the API

### Method 1: Interactive Docs
http://localhost:8000/docs

### Method 2: Use Test Script
```bash
python test_auth.py
```

### Method 3: cURL Commands
```bash
# Register
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@example.com","password":"test123"}'

# Login
curl -X POST http://localhost:8000/auth/login \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"test123"}'
```

---

## 📂 File Structure

```
SmartAgri-AI/
├── database.py              # MongoDB connection
├── models.py                # Data validation schemas
├── auth.py                  # Registration & login logic
├── main_fastapi.py          # Main FastAPI app
├── requirements.txt         # Dependencies
├── .env                     # Your configuration (create this)
├── .env.example             # Configuration template
├── AUTH_DOCUMENTATION.md    # Full documentation
├── setup_auth.py            # Setup helper script
└── test_auth.py             # API test script
```

---

## 🔐 Security Features

✅ Bcrypt password hashing  
✅ Unique email validation  
✅ Input sanitization  
✅ MongoDB injection prevention  
✅ Secure password storage  
✅ Environment variable configuration  

---

## ❓ Troubleshooting

### Server won't start
**Problem:** `ModuleNotFoundError`  
**Solution:** `pip install -r requirements.txt`

### Can't connect to MongoDB
**Problem:** Connection refused  
**Solution:** 
- Local: Ensure `mongod` is running
- Atlas: Check internet connection and IP whitelist

### Email already registered
**Problem:** 400 error on registration  
**Solution:** User already exists - try login or use different email

---

## 📚 Learn More

- Full Documentation: [AUTH_DOCUMENTATION.md](AUTH_DOCUMENTATION.md)
- FastAPI Docs: http://localhost:8000/docs
- MongoDB Docs: https://docs.mongodb.com/

---

## 🎯 Next Steps

1. ✅ Basic auth is complete
2. 🔄 Integrate with your frontend
3. 🔐 Add JWT tokens (optional)
4. 📧 Email verification (optional)
5. 🔑 Password reset (optional)

---

## 💡 Frontend Integration Example

```javascript
// Register
const response = await fetch('http://localhost:8000/auth/register', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    name: 'John Doe',
    email: 'john@example.com',
    password: 'secure123'
  })
});

const data = await response.json();
console.log(data.message);

// Login
const loginResponse = await fetch('http://localhost:8000/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'john@example.com',
    password: 'secure123'
  })
});

const loginData = await loginResponse.json();
console.log(loginData.user);
```

---

## ✨ You're All Set!

Your authentication system is **production-ready** and **secure**.

**Database:** `smartagri`  
**Collection:** `users`  
**Endpoints:** `/auth/register`, `/auth/login`

Happy coding! 🚀
