class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    if not head:
        return None
    if not head.next:
        return head
    rev_head = reverse(head.next)
    head.next.next = head
    head.next = None
    return rev_head
