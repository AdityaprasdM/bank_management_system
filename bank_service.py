from database.db_json import load_data, save_data
from models.savings_account import SavingsAccount
from models.current_account import CurrentAccount

class BankService:

    def __init__(self):
        self.accounts = {}
        self.load_accounts()


    def load_accounts(self):
        data = load_data()
        for acc_no, details in data.items():
            if details['type'] == 'savings':
                acc = SavingsAccount(
                    acc_no, details["name"], details["pin"],
                    details['balance'],details['transactions']
                    )
            else:
                acc = CurrentAccount(
                    acc_no, details['name'], details['pin'],
                    details['balance'],details['transactions']
                    )
            self.accounts[acc_no] = acc

    def save_accounts(self):
        data = {acc_no:acc.to_dict() for acc_no, acc in self.accounts.items()}
        save_data(data)

    def create_account(self, acc_no, name, pin, acc_type):
        if acc_no in self.accounts:
            raise Exception("Account already exists")

        if acc_type == "savings":
            acc = SavingsAccount(acc_no, name, pin)

        else:
            acc = CurrentAccount(acc_no, name, pin)

        self.accounts[acc_no] = acc
        self.save_accounts()

    def get_account(self, acc_no):
        return self.accounts.get(acc_no)

    def transfer(self, sender, receiver, amount):
        sender.withdraw(amount)
        receiver.deposit(amount)
        sender.transactions.append(f"Transferred ₹{amount} to {receiver.acc_no}")
        receiver.transactions.append(f"Received ₹{amount} from {sender.acc_no}")
        self.save_accounts()
        
