from model.block import Block
from model.blockchain import Blockchain
from view.blockchain_view import BlockchainView
from controller.blockchain_controller import BlockchainController

if __name__ == '__main__':
    print("Starting Blockchain...")
    model = Blockchain(Block)
    view = BlockchainView(model)
    controller = BlockchainController(model, view)
    controller.add_block("Charlie's block, my dog is nice")
    controller.add_block("Peter's block: I like cats")
    controller.add_block("John's block: I have some money!")
    controller.add_block("Agnes' block: I like jazz")
    print("\n")
    view.display_blockchain()
