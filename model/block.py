import hashlib
from datetime import datetime


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = ""
        self.nonce = 0

    def set_hash(self, hash):
        self.hash = hash

    def calculate_hash(self):
        # SHA256 hash
        sha = hashlib.sha256()

        # block data
        string = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)

        # UTF-8 coding and hash update
        sha.update(string.encode('utf-8'))

        # returns hash in hexadecimal format
        return sha.hexdigest()

    @staticmethod
    def create_genesis_block():
        return Block(0, datetime.now(), "Genesis Block", "0")
