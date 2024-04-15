class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.items.pop(0)

    def size(self):
        return len(self.items)


class MyStack:
    def __init__(self):
        self.queue = Queue()

    def push(self, val):
        self.queue.enqueue(val)
        for _ in range(self.queue.size() - 1):
            self.queue.enqueue(self.queue.dequeue())

    def pop(self):
        return self.queue.dequeue()

    def top(self):
        return self.queue.items[0] if not self.queue.is_empty() else None

    def empty(self):
        return self.queue.is_empty()
