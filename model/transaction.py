from Cryptodome.PublicKey import RSA
from Cryptodome.Signature import pkcs1_15
from Cryptodome.Hash import SHA256


class Transaction:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.signature = None
        self.public_key = None

    def validate(self, sender_balance, sender, executed_transactions = {}):
        print(f"Sender: {sender}")
        if self.sender != "MINING":
            if sender_balance < self.amount:
                return False

            if self.sender != sender:
                return False

            sender_tx_amounts = [tx.amount for tx in executed_transactions if tx.sender == self.sender]
            recipient_tx_amounts = [tx.amount for tx in executed_transactions if tx.recipient == self.sender]
            sender_total_tx_amount = sum(sender_tx_amounts) - sum(recipient_tx_amounts)
            if sender_balance < sender_total_tx_amount + self.amount:
                return False

            if self.public_key is None:
                return False

            try:
                message = str(self).encode()
                message_hash = SHA256.new(message)
                pkcs1_15.new(self.public_key).verify(message_hash, bytes.fromhex(self.signature.decode()))
            except (ValueError, TypeError):
                return False

        return True

    def sign(self, private_key):
        private_key = RSA.import_key(bytes.fromhex(private_key))
        message = str(self).encode()
        message_hash = SHA256.new(message)
        self.signature = pkcs1_15.new(private_key).sign(message_hash)
        self.public_key = private_key.publickey()

    def __str__(self):
        return f"{self.sender}{self.recipient}{self.amount}"
