from services.bank_service import BankService
from services.auth_service import Authservice
from models.savings_account import SavingsAccount

bank = BankService()
auth = Authservice()

def account_menu(account):

    while True:
        print("\n1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Transaction History")
        print("5. Add Interest (Savings only)")
        print("6. Logout")

        choice = input("Enter choice: ")

        try:

            if choice == '1':
                amount = float(input("Enter Amount: "))
                account.deposit(amount)
                bank.save_accounts()

            elif choice == '2':
                amount = float(input("Enter Amount: "))
                account.withdraw(amount)
                bank.save_accounts()

            elif choice == '3':
                print("Balance:",account.get_balance())

            elif choice == '4':
                for t in account.transactions:
                    print(t)

            elif choice == '5':
                if isinstance(account, SavingsAccount):
                    account.add_interest()
                    bank.save_accounts()

                else:
                    print("Only for savings account")

            elif choice == '6':
                break
        except Exception as e:
            print(e)


while True:
    print("\n====== BANK SYSTEM ======")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        acc_no = input("Account number: ")
        name = input("Name: ")
        pin = input("Set PIN: ")
        acc_type = input("Account type (savings/current): ")

        try:
            bank.create_account(acc_no, name, pin, acc_type)
            print("Account created successfully")

        except Exception as e:
            print(e)

    elif choice == '2':
        acc_no = input("Account number: ")
        pin = input("Enter PIN: ")

        account = bank.get_account(acc_no)
        if account:
            try:
                auth.login(account,pin)
                print("Login successful")
                account_menu(account)
            except Exception as e:
                print(e)

        else:
            print("Account not found")

    elif  choice == '3':
        break
                    
            























    

