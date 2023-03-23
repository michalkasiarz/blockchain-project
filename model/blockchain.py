from datetime import datetime


class Blockchain:
    def __init__(self, block_class):
        self.block_class = block_class
        self.chain = [self.block_class.create_genesis_block()]

    def add_block(self, data):
        index = len(self.chain)
        previous_hash = self.chain[index-1].hash
        block = self.block_class(index, datetime.now(), data, previous_hash)
        proof = self.proof_of_work(block)
        block.set_hash(proof)
        self.chain.append(block)

    def proof_of_work(self, block, difficulty=2):
        proof = '0' * difficulty
        while not block.hash.startswith(proof):
            block.nonce += 1
            calculated_hash = block.calculate_hash()
            block.set_hash(calculated_hash)
        return block.hash
