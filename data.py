"""
Data module - Contains account data and data management functions
"""

# Predefined accounts data
accounts = [
    {"name": "Ravi", "balance": 5000, "pin": 1234, "transactions": []},
    {"name": "Priya", "balance": 7000, "pin": 2345, "transactions": []},
    {"name": "Suresh", "balance": 10000, "pin": 3456, "transactions": []},
    {"name": "Anita", "balance": 3000, "pin": 4567, "transactions": []},
    {"name": "Kiran", "balance": 8500, "pin": 5678, "transactions": []},
    {"name": "Meena", "balance": 12000, "pin": 6789, "transactions": []},
    {"name": "Vamsi", "balance": 4500, "pin": 7890, "transactions": []},
    {"name": "Rohit", "balance": 6000, "pin": 8901, "transactions": []},
    {"name": "Sonia", "balance": 9000, "pin": 9012, "transactions": []},
    {"name": "Neha", "balance": 11000, "pin": 1122, "transactions": []}
]

def get_account_by_name_and_pin(name, pin):
    """
    Find account by name and PIN
    Returns account dictionary if found, None otherwise
    """
    for account in accounts:
        if account["name"].lower() == name.lower() and account["pin"] == pin:
            return account
    return None

def update_account_transaction(account, transaction_type, amount):
    """
    Update account transaction history
    """
    transaction_record = f"{transaction_type} ₹{amount}"
    account["transactions"].append(transaction_record)