class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head):
    if head is None or head.next is None:
        raise ValueError("List must have at least two nodes for splitting.")
    
    first_head = head
    second_head = head.next
    
    first_current = first_head
    second_current = second_head
    
    while first_current.next and second_current.next:
        first_current.next = second_current.next
        first_current = first_current.next
        
        second_current.next = first_current.next
        second_current = second_current.next
        
    first_current.next = None
    
    return Context(first_head, second_head)
