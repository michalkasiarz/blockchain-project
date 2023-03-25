class BlockchainView:
    def __init__(self, model):
        self.model = model

    def update(self, event, data=None):
        if event == "block_added":
            self.display_block(data)

    def display_block(self, block):
        print(f"Block {block.index}: {block.block_id}")

    def display_blockchain(self):
        print("Displaying the entire blockchain:")
        for block in self.model.chain:
            print(f"Block {block.index} (ID: {block.block_id}):")
            print(f"    Timestamp: {block.timestamp}")
            print(f"    Data: {block.data}")
            print(f"    Previous Hash: {block.previous_hash}")
            print(f"    Hash: {block.hash}")
            print(f"    Nonce: {block.nonce}")
