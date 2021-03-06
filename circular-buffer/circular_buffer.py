class BufferFullException(Exception):
    pass

class BufferEmptyException(Exception):
    pass

class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = []

    def read(self):
        if not self.buffer: raise BufferEmptyException
        return self.buffer.pop(0)

    def write(self, data):
        if len(self.buffer) >= self.capacity:
            raise BufferFullException
        self.buffer.append(data)

    def clear(self):
        self.buffer.clear()

    def overwrite(self, data):
        while len(self.buffer) >= self.capacity:
            self.read()
        self.write(data)
