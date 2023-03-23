class BlockchainView:
    def __init__(self, model):
        self.model = model

    def display_blockchain(self):
        print("Blockchain:")
        for block in self.model.chain:
            print(f"Index: {block.index}")
            print(f"Date: {block.timestamp}")
            print(f"Data: {block.data}")
            print(f"Hash: {block.hash}")
            print("-" * 20)
