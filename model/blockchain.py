import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.generate_hash()

    def generate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode('utf-8') + str(self.timestamp).encode('utf-8') +
                   str(self.data).encode('utf-8') + str(self.previous_hash).encode('utf-8'))
        return sha.hexdigest()

class BlockchainModel:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, datetime.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        index = len(self.chain)
        timestamp = datetime.datetime.now()
        previous_hash = self.get_latest_block().hash
        new_block = Block(index, timestamp, data, previous_hash)
        self.chain.append(new_block)
