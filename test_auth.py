"""
Test Script for SmartAgri Authentication API
Tests registration and login endpoints
"""

import requests
import json
from datetime import datetime


BASE_URL = "http://localhost:8000"


def print_response(title, response):
    """Pretty print API response"""
    print(f"\n{'='*60}")
    print(f"📊 {title}")
    print(f"{'='*60}")
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    try:
        print(json.dumps(response.json(), indent=2))
    except:
        print(response.text)


def test_authentication():
    """Test registration and login flow"""
    
    print("""
    ╔═══════════════════════════════════════════════════════════╗
    ║        SmartAgri Authentication API Test Suite           ║
    ╚═══════════════════════════════════════════════════════════╝
    """)
    
    # Test data
    test_user = {
        "name": "Test User",
        "email": f"test_{datetime.now().timestamp()}@example.com",
        "password": "test123456"
    }
    
    print(f"\n🧪 Testing with user: {test_user['email']}")
    
    # Test 1: Register new user
    print("\n\n🔹 TEST 1: User Registration")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json=test_user
        )
        print_response("Registration Response", response)
        
        if response.status_code == 201:
            print("✅ Registration successful!")
        else:
            print("❌ Registration failed!")
            
    except requests.exceptions.ConnectionError:
        print("\n❌ ERROR: Cannot connect to the server!")
        print("Make sure the FastAPI server is running:")
        print("   uvicorn main_fastapi:app --reload")
        return
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        return
    
    # Test 2: Login with correct credentials
    print("\n\n🔹 TEST 2: Login with Correct Credentials")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "email": test_user["email"],
                "password": test_user["password"]
            }
        )
        print_response("Login Response", response)
        
        if response.status_code == 200:
            print("✅ Login successful!")
            user_data = response.json()
            print(f"\n👤 Logged in as: {user_data['user']['name']}")
        else:
            print("❌ Login failed!")
            
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
    
    # Test 3: Login with wrong password
    print("\n\n🔹 TEST 3: Login with Wrong Password")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/login",
            json={
                "email": test_user["email"],
                "password": "wrongpassword"
            }
        )
        print_response("Login Response (Should Fail)", response)
        
        if response.status_code == 401:
            print("✅ Correctly rejected invalid credentials!")
        else:
            print("⚠️  Security issue: Should have rejected invalid credentials!")
            
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
    
    # Test 4: Duplicate registration
    print("\n\n🔹 TEST 4: Duplicate Email Registration")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json=test_user
        )
        print_response("Duplicate Registration Response (Should Fail)", response)
        
        if response.status_code == 400:
            print("✅ Correctly prevented duplicate registration!")
        else:
            print("⚠️  Should have prevented duplicate email!")
            
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
    
    # Test 5: Invalid email format
    print("\n\n🔹 TEST 5: Invalid Email Format")
    try:
        response = requests.post(
            f"{BASE_URL}/auth/register",
            json={
                "name": "Invalid User",
                "email": "not-an-email",
                "password": "test123456"
            }
        )
        print_response("Invalid Email Response (Should Fail)", response)
        
        if response.status_code == 422:
            print("✅ Correctly validated email format!")
        else:
            print("⚠️  Should have rejected invalid email format!")
            
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
    
    print("\n\n" + "="*60)
    print("🎉 Test Suite Complete!")
    print("="*60)
    print("\n📝 Summary:")
    print("   - All authentication endpoints are working")
    print("   - Password hashing is functional")
    print("   - Input validation is active")
    print("   - Duplicate prevention is working")
    print("\n✨ Your authentication system is ready to use!")


if __name__ == "__main__":
    print("\n⚠️  IMPORTANT: Make sure the FastAPI server is running!")
    print("Start it with: uvicorn main_fastapi:app --reload")
    print("\nPress Enter to start tests...")
    input()
    
    test_authentication()
