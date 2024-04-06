class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def push(head, data):
    next_node = Node(data)
    next_node.next = head
    return next_node

def sorted_insert(head, data):
    prev, cur = None, head
    while cur and cur.data < data:
        prev, cur = cur, cur.next
        
    if not prev:
        return push(cur, data)
    
    prev.next = push(cur, data)
    return head
