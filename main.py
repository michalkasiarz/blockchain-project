from model.block import Block
from model.blockchain import Blockchain
from model.logger import Logger
from model.statistics import Statistics
from view.blockchain_view import BlockchainView
from controller.blockchain_controller import BlockchainController

if __name__ == '__main__':
    print("Starting Blockchain...")
    model = Blockchain.get_instance(block_class=Block)
    logger = Logger()
    model.register_observer(logger)
    statistics = Statistics()
    model.register_observer(statistics)
    view = BlockchainView(model)
    controller = BlockchainController(model, view)
    controller.add_block("Charlie's block, my dog is nice")
    controller.add_block("Peter's block: I like cats")
    controller.add_block("John's block: I have some money!")
    controller.add_block("Agnes' block: I like jazz")
    print("\n")
    view.display_blockchain()
    print("\n")
    statistics.display_statistics()
