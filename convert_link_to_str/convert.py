class Node():
  '''
  class with simple Node
  '''
    def __init__(self, data, next = None):
        self.data = data
        self.next = next

def stringify(node):
  '''
  function to make string with ->
  '''
    if node is None:
        return "None"
    else:
        current = node
        result = ""
        while current is not None:
            result += str(current.data)
            if current.next is not None:
                result += " -> "
            current = current.next
        result += " -> None"
        return result



print(stringify(Node(0, Node(1, Node(2, Node(3))))))
print(stringify(None))
print(stringify(Node(0, Node(1, Node(4, Node(9, Node(16)))))))
