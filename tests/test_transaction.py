import unittest
import base64
from Cryptodome.PublicKey import RSA
from Cryptodome.Hash import SHA256
from Cryptodome.Signature import PKCS1_v1_5

from model.transaction import Transaction


class TestTransaction(unittest.TestCase):
    def setUp(self):
        self.sender_public_key = "sender_public_key"
        self.recipient_public_key = "recipient_public_key"
        self.transaction = Transaction(self.sender_public_key, self.recipient_public_key, 20)

    def test_validate_valid_transaction(self):
        sender_balance = 100
        executed_transactions = [Transaction(self.sender_public_key, self.recipient_public_key, 10)]

        result = self.transaction.validate(sender_balance, self.sender_public_key, executed_transactions)
        self.assertTrue(result)

    def test_validate_sender_balance_insufficient(self):
        sender_balance = 10
        executed_transactions = []

        result = self.transaction.validate(sender_balance, self.sender_public_key, executed_transactions)
        self.assertFalse(result)

    def test_validate_sender_and_public_key_do_not_match(self):
        sender_balance = 100
        executed_transactions = []

        result = self.transaction.validate(sender_balance, "other_public_key", executed_transactions)
        self.assertFalse(result)

    def test_validate_sender_total_tx_amount_insufficient(self):
        sender_balance = 100
        executed_transactions = [Transaction(self.sender_public_key, self.recipient_public_key, 10),
                                 Transaction("other_sender_public_key", self.sender_public_key, 90)]

        result = self.transaction.validate(sender_balance, self.sender_public_key, executed_transactions)
        self.assertTrue(result)

    def test_validate_invalid_signature(self):
        sender_balance = 100
        executed_transactions = []
        self.transaction.signature = "invalid_signature"

        result = self.transaction.validate(sender_balance, self.sender_public_key, executed_transactions)
        self.assertTrue(result)

    def test_sign(self):
        private_key = RSA.generate(1024).export_key()
        private_key_b64 = base64.b64encode(private_key).decode('utf-8').replace('\n', '')
        self.transaction.sign(private_key_b64)

        message = str(self.transaction).encode()
        message_hash = SHA256.new(message)
        public_key = RSA.import_key(base64.b64decode(private_key_b64)).publickey()
        verifier = PKCS1_v1_5.new(public_key)
        self.assertTrue(verifier.verify(message_hash, base64.b64decode(self.transaction.signature)))

