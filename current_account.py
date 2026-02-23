from models.account import Account

class CurrentAccount(Account):
    OVERDRAFT_LIMIT = 5000

    def withdraw(self, amount):
        if self._balance + self.OVERDRAFT_LIMIT >= amount:
            self._balance -= amount
            self.transactions.append(f"withdrawn ₹{amount}")
        else:
            raise Exception("Overdraft limit exceeded")


    def to_dict(self):
        data = super().to_dict()
        data["type"] = "current"
        return data
