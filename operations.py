"""
Operations module - Handles all ATM operations
"""

from data import update_account_transaction
from utils import display_header, format_currency

def check_balance(account):
    """
    Check and display current balance
    """
    display_header("CHECK BALANCE")
    print(f"Account Holder: {account['name']}")
    print(f"Current Balance: {format_currency(account['balance'])}")
    input("\nPress Enter to continue...")

def deposit(account):
    """
    Deposit money into account
    """
    display_header("DEPOSIT MONEY")
    
    try:
        amount = float(input("Enter amount to deposit: ₹"))
        
        if amount <= 0:
            print("❌ Deposit amount must be positive.")
            return
        
        account["balance"] += amount
        update_account_transaction(account, "Deposited", amount)
        
        print(f"✅ Successfully deposited {format_currency(amount)}")
        print(f"💰 New Balance: {format_currency(account['balance'])}")
        
    except ValueError:
        print("❌ Invalid amount! Please enter a valid number.")
    
    input("\nPress Enter to continue...")

def withdraw(account):
    """
    Withdraw money from account
    """
    display_header("WITHDRAW MONEY")
    
    try:
        amount = float(input("Enter amount to withdraw: ₹"))
        
        if amount <= 0:
            print("❌ Withdrawal amount must be positive.")
            return
        
        if amount > account["balance"]:
            print("❌ Insufficient balance!")
            print(f"💳 Current Balance: {format_currency(account['balance'])}")
            print(f"💸 Withdrawal Attempt: {format_currency(amount)}")
            return
        
        account["balance"] -= amount
        update_account_transaction(account, "Withdrew", amount)
        
        print(f"✅ Successfully withdrew {format_currency(amount)}")
        print(f"💰 New Balance: {format_currency(account['balance'])}")
        
    except ValueError:
        print("❌ Invalid amount! Please enter a valid number.")
    
    input("\nPress Enter to continue...")

def transaction_history(account):
    """
    Display transaction history
    """
    display_header("TRANSACTION HISTORY")
    print(f"Account Holder: {account['name']}")
    print(f"Current Balance: {format_currency(account['balance'])}")
    print("\nTransaction History:")
    print("-" * 30)
    
    if not account["transactions"]:
        print("No transactions yet.")
    else:
        for i, transaction in enumerate(account["transactions"], 1):
            print(f"{i}. {transaction}")
    
    input("\nPress Enter to continue...")