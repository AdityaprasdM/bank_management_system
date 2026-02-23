class Account:
    def __init__(self, acc_no, name, pin, balance=0, transactions=None):
        self.acc_no = acc_no
        self.name = name
        self.__pin = pin
        self._balance = balance
        self.transactions = transactions if transactions else []

    def verify_pin(self, pin):
        return self.__pin == pin

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self._balance += amount
        self.transactions.append(f"Deposited ₹{amount}")

    def withdraw(self, amount):
        if amount > self._balance:
            raise Exception("Insufficient balance")
        self._balance -= amount
        self.transactions.append(f"Withdrawn ₹{amount}")

    def get_balance(self):
        return self._balance

    def to_dict(self):
        return {
            "acc_no":self.acc_no,
            "name":self.name,
            "pin":self._Account__pin,
            "balance":self._balance,
            "transactions":self.transactions,
            "type":"base"
            }
