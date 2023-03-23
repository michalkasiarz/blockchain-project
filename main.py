from model.block import Block
from model.blockchain import Blockchain
from view.blockchain_view import BlockchainView
from controller.blockchain_controller import BlockchainController

if __name__ == '__main__':
    model = Blockchain(Block)
    view = BlockchainView()
    controller = BlockchainController(model, view)
    controller.add_block("Block 1")
    controller.add_block("Block 2")
    controller.add_block("Block 3")
