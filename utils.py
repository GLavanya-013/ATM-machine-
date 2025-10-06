"""
Utilities module - Helper functions for display and formatting
"""

import os

def clear_screen():
    """
    Clear the terminal screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header(title):
    """
    Display a formatted header
    """
    clear_screen()
    print("="*50)
    print(f"           {title}")
    print("="*50)

def format_currency(amount):
    """
    Format amount as currency
    """
    return f"₹{amount:,.2f}"

def display_menu():
    """
    Display the main ATM menu
    """
    display_header("ATM MACHINE")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transaction History")
    print("5. Exit")
    print("="*50)

def get_user_choice():
    """
    Get and validate user menu choice
    """
    try:
        choice = int(input("Enter your choice (1-5): "))
        return choice
    except ValueError:
        print("❌ Invalid choice! Please enter a number between 1-5.")
        return -1