from datetime import datetime
from model.transaction_pool import TransactionPool
from model.accounts import Accounts


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
        self.transaction_pool = TransactionPool()
        self.accounts = Accounts()

    def add_block(self):
        index = len(self.chain)
        previous_hash = self.chain[index - 1].hash
        transactions = self.transaction_pool.get_transactions()
        block = self.block_class(index, datetime.now(), transactions, previous_hash)
        sender_balances = self.get_sender_balances()
        if not self.validate_block_transactions(block, sender_balances):
            return False
        proof = self.proof_of_work(block)
        block.set_hash(proof)
        self.chain.append(block)
        self.notify_observers('block_added', block)
        self.transaction_pool.clear_transactions()

    def add_transaction_to_block(self, block, transaction_pool):
        sender_balances = self.get_sender_balances()
        valid_transactions = []
        for transaction in transaction_pool.get_transactions():
            if transaction.validate(sender_balances[transaction.sender], transaction.sender):
                valid_transactions.append(transaction)

        block.data = valid_transactions

    def get_sender_balances(self):
        sender_balances = self.accounts.accounts.copy()
        for block in self.chain:
            for transaction in block.transactions:
                sender = transaction.sender
                recipient = transaction.recipient
                amount = transaction.amount

                sender_balances[sender] -= amount
                sender_balances[recipient] += amount

        return sender_balances

    def validate_block_transactions(self, block, sender_balances):
        for transaction in block.transactions:
            if not transaction.validate(sender_balances[transaction.sender], transaction.sender):
                return False
        return True

    def proof_of_work(self, block, difficulty=2):
        proof = '0' * difficulty
        while not block.hash.startswith(proof):
            block.nonce += 1
            calculated_hash = block.calculate_hash()
            block.set_hash(calculated_hash)
        return block.hash
