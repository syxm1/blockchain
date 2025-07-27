class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(previous_hash='0')

    def create_block(self, data):
        index = len(self.chain) + 1
        timestamp = self.get_timestamp()
        previous_hash = self.chain[-1].hash if self.chain else '0'
        hash = self.hash_block(index, previous_hash, timestamp, data)
        block = Block(index, previous_hash, timestamp, data, hash)
        self.chain.append(block)
        return block

    def hash_block(self, index, previous_hash, timestamp, data):
        import hashlib
        value = f"{index}{previous_hash}{timestamp}{data}".encode()
        return hashlib.sha256(value).hexdigest()

    def get_timestamp(self):
        import time
        return time.time()

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != self.hash_block(current.index, current.previous_hash, current.timestamp, current.data):
                return False

            if current.previous_hash != previous.hash:
                return False

        return True

    def get_chain(self):
        return [(block.index, block.previous_hash, block.timestamp, block.data, block.hash) for block in self.chain]