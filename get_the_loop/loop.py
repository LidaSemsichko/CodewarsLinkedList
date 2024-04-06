class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def loop_size(node):
    visited = set()
    current = node
    while current not in visited:
        visited.add(current)
        current = current.next
    start_of_loop = current
    current = current.next
    loop_size = 1
    while current != start_of_loop:
        current = current.next
        loop_size += 1
    return loop_size

def create_chain(length, loop_size):
    nodes = [Node() for _ in range(length)]
    for i in range(length - 1):
        nodes[i].next = nodes[i + 1]
    loop_start = length - loop_size
    nodes[-1].next = nodes[loop_start]
    return nodes[0]
