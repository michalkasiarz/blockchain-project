import hashlib
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, transactions, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()
        self.block_id = None
        self.data = transactions

    def set_hash(self, hash):
        self.hash = hash
        self.block_id = f"{self.index}-{self.hash}"

    def calculate_hash(self):
        # SHA256 hash
        sha = hashlib.sha256()

        # block data
        string = str(self.index) + str(self.timestamp) + str(self.transactions) + str(self.previous_hash) + str(
            self.nonce)

        # UTF-8 coding and hash update
        sha.update(string.encode('utf-8'))

        # returns hash in hexadecimal format
        return sha.hexdigest()

    @staticmethod
    def create_genesis_block():
        return Block(0, datetime.now(), [], "Genesis Block", 0)
