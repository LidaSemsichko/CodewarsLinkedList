class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack) == 0

    def peek(self):
        if self.size() == 0:
            raise Exception("peek() called on empty stack.")
        return self.stack[-1]


class MyQueue:
    def __init__(self):
        self.s1 = Stack()
        self.s2 = Stack()

    def push(self, x):
        self.s1.push(x)

    def pop(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.pop()

    def peek(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())
        return self.s2.peek() if not self.s2.is_empty() else None

    def empty(self):
        return self.s1.is_empty() and self.s2.is_empty()
