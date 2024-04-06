class Node(object):
    """Node class for reference"""
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
def get_nth(node, index):
    for _ in range(index):
        node = node.next
    if index < 0 or node == None:
        raise IndexError
    return node
