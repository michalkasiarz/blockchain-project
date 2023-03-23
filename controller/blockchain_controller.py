class BlockchainController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_block(self, data):
        self.model.add_block(data)
        print("Block added")

    def validate_chain(self):
        if self.model.is_valid():
            print("Chain is valid")
        else:
            print("Chain is not valid")

    def display_blockchain(self):
        self.view.display_blockchain(self.model)
