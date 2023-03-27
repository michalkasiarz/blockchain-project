import unittest
from model.accounts import Accounts


class TestAccounts(unittest.TestCase):
    def setUp(self):
        self.accounts = Accounts()

    def test_get_balance(self):
        self.assertEqual(self.accounts.get_balance("Alice"), 100)
        self.assertEqual(self.accounts.get_balance("Bob"), 50)
        self.assertEqual(self.accounts.get_balance("Charlie"), 200)

    def test_get_balance_invalid_account(self):
        with self.assertRaises(ValueError):
            self.accounts.get_balance("Eve")

    def test_add_account(self):
        accounts = Accounts()
        account_name = "David"
        balance = 300
        accounts.add_account(account_name, balance)
        self.assertEqual(accounts.get_balance(account_name), balance)

    def test_add_existing_account(self):
        accounts = Accounts()
        account_name = "Alice"
        balance = 300
        with self.assertRaises(ValueError):
            accounts.add_account(account_name, balance)