import datetime


class Statistics:
    def __init__(self):
        self.previous_block_timestamp = None
        self.total_time = datetime.timedelta()
        self.blocks_count = 0

    def update(self, event, data=None):
        if event == "block_added":
            self.update_statistics(data)

    def update_statistics(self, block):
        if self.blocks_count > 0:
            time_difference = block.timestamp - self.previous_block_timestamp
            self.total_time += time_difference
        self.previous_block_timestamp = block.timestamp
        self.blocks_count += 1

    def display_statistics(self):
        if self.blocks_count > 1:
            average_time = self.total_time / (self.blocks_count - 1)
            print(f"Average time between blocks: {average_time.seconds}")
        else:
            print("Not enough blocks to calculate average time.")
