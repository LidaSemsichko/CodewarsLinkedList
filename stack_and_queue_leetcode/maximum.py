from collections import deque

class FreqStack:
    def __init__(self):
        self.freq_map = {}
        self.stack = deque()

    def push(self, val):
        if val not in self.freq_map:
            self.freq_map[val] = 0
        self.freq_map[val] += 1
        freq = self.freq_map[val]
        if freq > len(self.stack):
            self.stack.append(deque())
        self.stack[freq - 1].append(val)

    def pop(self):
        if not self.stack:
            return None
        val = self.stack[-1].pop()
        if not self.stack[-1]:
            self.stack.pop()
        self.freq_map[val] -= 1
        if self.freq_map[val] == 0:
            del self.freq_map[val]
        return val
