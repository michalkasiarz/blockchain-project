from model.accounts import Accounts
from model.block import Block
from model.blockchain import Blockchain
from model.logger import Logger
from model.statistics import Statistics
from view.blockchain_view import BlockchainView
from controller.blockchain_controller import BlockchainController
from model.transaction import Transaction

if __name__ == '__main__':
    print("Starting Blockchain...")
    model = Blockchain.get_instance(block_class=Block)
    logger = Logger()
    model.register_observer(logger)
    statistics = Statistics()
    model.register_observer(statistics)
    view = BlockchainView(model)
    model.register_observer(view)
    controller = BlockchainController(model, view)

    transaction1 = Transaction('Alice', 'Bob', 50)
    transaction2 = Transaction('Charlie', 'Alice', 10)
    transaction3 = Transaction('Bob', 'Charlie', 30)

    controller.add_transaction_to_pool(transaction1)
    controller.add_transaction_to_pool(transaction2)
    controller.add_transaction_to_pool(transaction3)

    controller.add_block()
    view.display_blockchain()
    statistics.display_statistics()


