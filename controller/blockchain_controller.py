from model.accounts import Accounts


class BlockchainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.accounts = Accounts()

    def add_block(self):
        self.model.add_block()
        print("Block added")

    def validate_chain(self):
        if self.model.is_valid():
            print("Chain is valid")
        else:
            print("Chain is not valid")

    def display_blockchain(self):
        self.view.display_blockchain(self.model)

    def add_transaction_to_pool(self, transaction):
        # Get current balances of all unique senders in the transaction pool
        unique_senders = {tx.sender for tx in self.model.transaction_pool.get_transactions()}
        sender_balances = {sender: self.accounts.get_balance(sender) for sender in unique_senders}

        # Add the balance of the sender of the current transaction if it's not already in the dictionary
        if transaction.sender not in sender_balances:
            sender_balances[transaction.sender] = self.accounts.get_balance(transaction.sender)

        # Validate the transaction using the sender's current balance
        if transaction.validate(sender_balances[transaction.sender], transaction.sender):
            self.model.transaction_pool.add_transaction(transaction)






