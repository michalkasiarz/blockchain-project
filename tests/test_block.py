import hashlib
import unittest
from datetime import datetime
from model.block import Block


class TestBlock(unittest.TestCase):
    def setUp(self):
        self.index = 1
        self.timestamp = datetime.now()
        self.transactions = ["transaction1", "transaction2"]
        self.previous_hash = "previous_hash"
        self.nonce = 0
        self.block = Block(self.index, self.timestamp, self.transactions, self.previous_hash, self.nonce)

    def test_init(self):
        self.assertEqual(self.block.index, self.index)
        self.assertEqual(self.block.timestamp, self.timestamp)
        self.assertEqual(self.block.transactions, self.transactions)
        self.assertEqual(self.block.previous_hash, self.previous_hash)
        self.assertEqual(self.block.nonce, self.nonce)
        self.assertEqual(self.block.hash, self.block.calculate_hash())
        self.assertIsNone(self.block.block_id)
        self.assertEqual(self.block.data, self.transactions)

    def test_set_hash(self):
        hash = "hash"
        self.block.set_hash(hash)
        self.assertEqual(self.block.hash, hash)
        self.assertEqual(self.block.block_id, f"{self.index}-{hash}")

    def test_calculate_hash(self):
        sha = hashlib.sha256()
        string = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(self.nonce)
        sha.update(string.encode('utf-8'))
        expected_hash = sha.hexdigest()
        self.assertEqual(self.block.calculate_hash(), expected_hash)

    def test_create_genesis_block(self):
        genesis_block = Block.create_genesis_block()
        self.assertEqual(genesis_block.index, 0)
        self.assertEqual(len(genesis_block.transactions), 0)
        self.assertEqual(genesis_block.previous_hash, "Genesis Block")
        self.assertEqual(genesis_block.nonce, 0)
        self.assertEqual(genesis_block.hash, genesis_block.calculate_hash())
        self.assertIsNone(genesis_block.block_id)
        self.assertEqual(genesis_block.data, [])
