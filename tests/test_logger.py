import unittest
from unittest.mock import patch, mock_open
from model.logger import Logger
from model.block import Block
from datetime import datetime


class TestLogger(unittest.TestCase):
    def setUp(self):
        self.logger = Logger("blockchain.log")

    @patch("builtins.open", new_callable=mock_open)
    def test_log_block_added(self, mock_file):
        block = Block(1, datetime.now(), [], "test")
        self.logger.log_block_added(block)
        mock_file().write.assert_called_once_with(f"Block added: {block}\n")

    def test_update_block_added_event(self):
        block = Block(1, datetime.now(), [], "test")
        with patch("builtins.open", mock_open()) as mock_file:
            self.logger.update("block_added", block)
            mock_file.assert_called_once_with("blockchain.log", "a")

