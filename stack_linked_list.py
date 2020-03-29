class Node:

  def __init__(self, value):
    self.value = value
    self.next = None


class Stack:

    def __init__(self):
        self.head = None
        self.num_elements = 0

    def push(self, value):
        new_node = Node(value)
        # Check if stack is empty
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.num_elements += 1

    def size(self):
        return self.num_elements
    
    def is_empty(self):
        return self.num_elements == 0
        