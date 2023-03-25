class Logger:
    def __init__(self, filename="blockchain.log"):
        self.filename = filename

    def update(self, event, data=None):
        if event == "block_added":
            self.log_block_added(data)

    def log_block_added(self, block):
        log_entry = f"Block added: {block}\n"
        with open(self.filename, "a") as log_file:
            log_file.write(log_entry)
