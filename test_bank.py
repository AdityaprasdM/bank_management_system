import unittest
from models.account import Account

class TestBank(unittest.TestCase):

    def test_deposit(self):
        acc = Account("101", "Test", "1234",1000)
        acc.deposit(500)
        self.assertEqual(acc.get_balance(), 1500)


    def test_withdraw(self):
        acc = Account("101", "Test","1234",1000)
        acc.withdraw(200)
        self.assertEqual(acc.get_balance(), 800)

if __name__ == "__main__":
    unittest.main()
