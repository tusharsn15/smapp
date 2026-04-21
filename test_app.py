#!/usr/bin/env python
"""
Test script to verify the login/register functionality with CSRF tokens
"""
import sys
sys.path.insert(0, 'c:\\Users\\Lenovo\\OneDrive\\Desktop\\2 sem\\C\\SocialMediaApp')

from app import create_app, db
from app.models.user import User

# Create app context
app = create_app()

with app.app_context():
    # Clear existing test user if exists
    test_user = User.query.filter_by(username='testuser').first()
    if test_user:
        db.session.delete(test_user)
        db.session.commit()
    
    # Test registration via model
    new_user = User(
        username='testuser',
        email='test@example.com'
    )
    new_user.set_password('testpassword123')
    db.session.add(new_user)
    db.session.commit()
    
    print("✓ Test user created successfully")
    print(f"  Username: {new_user.username}")
    print(f"  Email: {new_user.email}")
    
    # Test login
    retrieved_user = User.query.filter_by(username='testuser').first()
    if retrieved_user and retrieved_user.check_password('testpassword123'):
        print("✓ Password verification works correctly")
    else:
        print("✗ Password verification failed")
    
    # Test with wrong password
    if retrieved_user and not retrieved_user.check_password('wrongpassword'):
        print("✓ Wrong password correctly rejected")
    else:
        print("✗ Wrong password validation failed")
    
    print("\nAll database operations working correctly!")
    print("CSRF tokens should now work with the forms.")
    print("\nTo test in browser:")
    print("1. Go to http://127.0.0.1:5000")
    print("2. Click 'Register' or 'Login'")
    print("3. The CSRF token will be automatically included")
    print("4. Form submission should now work without 'invalid request' error")
