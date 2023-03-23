class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = None

    def set_hash(self, hash):
        self.hash = hash

    def __str__(self):
        return "Block {}: {} ({})".format(self.index, self.data, self.timestamp)
