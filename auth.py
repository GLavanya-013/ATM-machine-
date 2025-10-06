"""
Authentication module - Handles user authentication
"""

from data import get_account_by_name_and_pin

def authenticate_user():
    """
    Authenticate user by name and PIN
    Returns authenticated account dictionary if successful, None otherwise
    """
    print("\n" + "="*40)
    print("          USER AUTHENTICATION")
    print("="*40)
    
    name = input("Enter your name: ").strip()
    
    try:
        pin = int(input("Enter your PIN: "))
    except ValueError:
        print("❌ Invalid PIN! PIN must be a number.")
        return None
    
    account = get_account_by_name_and_pin(name, pin)
    
    if account:
        print(f"✅ Welcome, {account['name']}!")
        return account
    else:
        print("❌ Invalid name or PIN. Please try again.")
        return None

def require_authentication():
    """
    Decorator to require authentication for operations
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            account = authenticate_user()
            if account:
                return func(account, *args, **kwargs)
            return None
        return wrapper
    return decorator