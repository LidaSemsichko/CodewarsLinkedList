class Node:
  '''
  class with simple Node
  '''
    def __init__(self, data, next=None): 
        self.data = data
        self.next = next


def linked_list_from_string(s):
  '''
  function to make linked list from str with ->
  '''
    if s.lower() in ["null", "nil", "nullptr", "null()"]:
        return None
    else:
        elements = s.split(" -> ")
        if len(elements) == 1 and elements[0].lower() in ["none"]:
            return None
        head = Node(int(elements[0]))
        current = head
        for element in elements[1:-1]:
            current.next = Node(int(element))
            current = current.next
        return head
