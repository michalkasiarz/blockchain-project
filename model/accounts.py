class Accounts:
    def __init__(self):
        self.accounts = {
            "Alice": 100,
            "Bob": 50,
            "Charlie": 200
        }

    def get_balance(self, account):
        if account not in self.accounts:
            raise ValueError(f"Account {account} does not exist.")
        return self.accounts[account]

    def add_account(self, account, balance):
        if account in self.accounts:
            raise ValueError(f"Account {account} already exists.")
        self.accounts[account] = balance