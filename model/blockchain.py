from datetime import datetime

class Observable:
    def __init__(self):
        self._observers = []

    def register_observer(self, observer):
        self._observers.append(observer)

    def unregister_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self, event, data=None):
        for observer in self._observers:
            observer.update(event, data)

class Blockchain(Observable):
    _instance = None

    @classmethod
    def get_instance(cls, block_class=None):
        if cls._instance is None:
            if block_class is None:
                raise ValueError("block_class is required when creating a new instance")
            cls._instance = cls(block_class)
        return cls._instance

    def __init__(self, block_class):
        if self._instance is not None:
            raise ValueError("An instance of the Blockchain class already exists!")
        super().__init__()
        self.block_class = block_class
        self.chain = [self.block_class.create_genesis_block()]

    def add_block(self, data):
        index = len(self.chain)
        previous_hash = self.chain[index-1].hash
        block = self.block_class(index, datetime.now(), data, previous_hash)
        proof = self.proof_of_work(block)
        block.set_hash(proof)
        self.chain.append(block)
        self.notify_observers('block_added', block)

    def proof_of_work(self, block, difficulty=2):
        proof = '0' * difficulty
        while not block.hash.startswith(proof):
            block.nonce += 1
            calculated_hash = block.calculate_hash()
            block.set_hash(calculated_hash)
        return block.hash
