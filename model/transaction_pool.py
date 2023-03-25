class TransactionPool:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def clear_transactions(self):
        self.transactions = []

    def get_transactions(self):
        return self.transactions

    def validate_transaction_pool(self, sender_balances):
        for transaction in self.transactions:
            if not transaction.validate(sender_balances[transaction.sender], transaction.sender):
                return False
        return True



