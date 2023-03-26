import datetime

from model.block import Block
from model.statistics import Statistics


class TestStatistics:
    def setup_method(self):
        self.statistics = Statistics()

    def test_update_statistics_with_one_block(self):
        block = Block(1, datetime.datetime.now(), [], "test")
        self.statistics.update_statistics(block)
        assert self.statistics.blocks_count == 1
        assert self.statistics.total_time == datetime.timedelta(0)

    def test_update_statistics_with_multiple_blocks(self):
        block1 = Block(1, datetime.datetime.now(), [], "test")
        block2 = Block(2, datetime.datetime.now() + datetime.timedelta(seconds=30), [], "test")
        self.statistics.update_statistics(block1)
        self.statistics.update_statistics(block2)
        assert self.statistics.blocks_count == 2
        assert self.statistics.total_time.seconds == 30

    def test_display_statistics_with_not_enough_blocks(self, capsys):
        block = Block(1, datetime.datetime.now(), [], "test")
        self.statistics.update_statistics(block)
        self.statistics.display_statistics()
        captured_output = capsys.readouterr()
        assert captured_output.out.strip() == "Not enough blocks to calculate average time."

    def test_display_statistics_with_multiple_blocks(self, capsys):
        block1 = Block(1, datetime.datetime.now(), [], "test")
        block2 = Block(2, datetime.datetime.now() + datetime.timedelta(seconds=30), [], "test")
        self.statistics.update_statistics(block1)
        self.statistics.update_statistics(block2)
        self.statistics.display_statistics()
        captured_output = capsys.readouterr()
        assert captured_output.out.strip() == "Average time between blocks: 30"
