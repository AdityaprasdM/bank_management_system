from models.account import Account

class SavingsAccount(Account):
    INTEREST_RATE = 0.04

    def add_interest(self):
        interest = self._balance * self.INTEREST_RATE
        self._balance += interest
        self.transactions.append(f"Interest added ₹{interest}")

    def to_dict(self):
        data = super().to_dict()
        data["type"] = "savings"
        return data
