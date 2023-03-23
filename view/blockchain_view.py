class BlockchainView:
    def __init__(self, model):
        self.model = model

    def display(self):
        print("Blockchain:")
        for block in self.model.chain:
            print(block)
        print("")
