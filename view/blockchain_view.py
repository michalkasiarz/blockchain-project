class BlockchainView:
    def display(self, blockchain):
        print("Blockchain:")
        for block in blockchain.chain:
            print(block)
            print()
