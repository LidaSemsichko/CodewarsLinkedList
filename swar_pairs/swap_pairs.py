class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swap_pairs(head):
    node = ListNode(0)
    node.next = head
    prev = node

    while prev.next and prev.next.next:
        first = prev.next
        second = prev.next.next

        prev.next = second
        first.next = second.next
        second.next = first
        prev = first
