from model.transaction import Transaction
from model.transaction_pool import TransactionPool
import unittest

class TestTransactionPool(unittest.TestCase):
    def setUp(self):
        self.pool = TransactionPool()

        self.sender_1 = "sender_1"
        self.sender_2 = "sender_2"
        self.sender_3 = "sender_3"

        self.sender_balances = {
            self.sender_1: 100,
            self.sender_2: 50,
            self.sender_3: 1000
        }

        self.transaction_1 = Transaction(self.sender_1, "recipient_1", 10)
        self.transaction_2 = Transaction(self.sender_2, "recipient_2", 20)
        self.transaction_3 = Transaction(self.sender_3, "recipient_3", 100)

    def test_add_transaction(self):
        self.pool.add_transaction(self.transaction_1)
        self.pool.add_transaction(self.transaction_2)
        self.pool.add_transaction(self.transaction_3)

        transactions = self.pool.get_transactions()
        self.assertEqual(len(transactions), 3)
        self.assertIn(self.transaction_1, transactions)
        self.assertIn(self.transaction_2, transactions)
        self.assertIn(self.transaction_3, transactions)

    def test_clear_transactions(self):
        self.pool.add_transaction(self.transaction_1)
        self.pool.add_transaction(self.transaction_2)
        self.pool.add_transaction(self.transaction_3)

        self.pool.clear_transactions()

        transactions = self.pool.get_transactions()
        self.assertEqual(len(transactions), 0)

    def test_get_transactions(self):
        self.pool.add_transaction(self.transaction_1)
        self.pool.add_transaction(self.transaction_2)

        transactions = self.pool.get_transactions()
        self.assertEqual(len(transactions), 2)
        self.assertIn(self.transaction_1, transactions)
        self.assertIn(self.transaction_2, transactions)

    def test_validate_transaction_pool(self):
        self.pool.add_transaction(self.transaction_1)
        self.pool.add_transaction(self.transaction_2)

        valid = self.pool.validate_transaction_pool(self.sender_balances)
        self.assertTrue(valid)

        self.pool.add_transaction(self.transaction_3)

        valid = self.pool.validate_transaction_pool(self.sender_balances)
        self.assertTrue(valid)
