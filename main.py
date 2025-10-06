"""
Main module - ATM Machine CLI Application
"""

from auth import require_authentication
from operations import check_balance, deposit, withdraw, transaction_history
from utils import display_menu, get_user_choice, clear_screen

def main():
    """
    Main function to run the ATM Machine
    """
    print("🚀 Starting ATM Machine...")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == 1:
            # Check Balance
            @require_authentication()
            def authenticated_check_balance(account):
                check_balance(account)
            authenticated_check_balance()
            
        elif choice == 2:
            # Deposit Money
            @require_authentication()
            def authenticated_deposit(account):
                deposit(account)
            authenticated_deposit()
            
        elif choice == 3:
            # Withdraw Money
            @require_authentication()
            def authenticated_withdraw(account):
                withdraw(account)
            authenticated_withdraw()
            
        elif choice == 4:
            # Transaction History
            @require_authentication()
            def authenticated_transaction_history(account):
                transaction_history(account)
            authenticated_transaction_history()
            
        elif choice == 5:
            # Exit
            clear_screen()
            print("="*50)
            print("        Thank you for using ATM Machine!")
            print("                 Goodbye! 👋")
            print("="*50)
            break
            
        else:
            print("❌ Invalid choice! Please select between 1-5.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()