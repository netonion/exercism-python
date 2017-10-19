class BufferFullException(Exception):
    pass


class BufferEmptyException(Exception):
    pass


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0

    def read(self):
        if self.head >= self.tail: raise BufferEmptyException
        val = self.buffer[self.head % self.capacity]
        self.head += 1
        return val

    def write(self, data):
        if self.tail >= self.head + self.capacity:
            raise BufferFullException
        self.buffer[self.tail % self.capacity] = data
        self.tail += 1

    def clear(self):
        self.head = 0
        self.tail = 0

    def overwrite(self, data):
        self.buffer[self.tail % self.capacity] = data
        while self.tail >= self.head + self.capacity: self.head += 1
        self.tail += 1
