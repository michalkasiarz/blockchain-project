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
