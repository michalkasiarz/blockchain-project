from unittest import TestCase
from model.block import Block
from model.blockchain import Blockchain
from model.transaction import Transaction


class TestBlockchain(TestCase):
    def test_add_block(self):
        blockchain = Blockchain(block_class=Block)
        blockchain.add_block()
        self.assertEqual(len(blockchain.chain), 2)

    def test_validate_transaction_pool_failed(self):
        blockchain = Blockchain(block_class=Block)
        transaction1 = Transaction("Charlie", "Peter", 1000)
        transaction2 = Transaction("Charlie", "Agnes", 700)
        blockchain.transaction_pool.add_transaction(transaction1)
        blockchain.transaction_pool.add_transaction(transaction2)
        sender_balances = {"Charlie": 500}
        self.assertFalse(blockchain.transaction_pool.validate_transaction_pool(sender_balances))

    def test_validate_transaction_pool_successful(self):
        blockchain = Blockchain(block_class=Block)
        transaction1 = Transaction("Charlie", "Peter", 500)
        blockchain.transaction_pool.add_transaction(transaction1)
        sender_balances = {"Charlie": 1000}
        self.assertTrue(blockchain.transaction_pool.validate_transaction_pool(sender_balances))
