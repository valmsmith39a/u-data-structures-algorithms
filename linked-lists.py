# create a node 
"""
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None
"""

"""
head = Node(2)
new_node = Node(1)
head.next = new_node

print(new_node.value)
print(head.next.value)
"""

# create several nodes and link them together
"""
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
"""

# traverse a linked list
"""
current_node = head

while current_node.next is not None:
	print(current_node.value)
	current_node = current_node.next
"""

# iterative method to create a linked list
"""
# print a linked list (to test create method later)
def print_linked_list(head):
	current_node = head
	while current_node.next is not None:
		print(current_node.value)
		current_node = current_node.next
"""
# create a linked list: method 1 
# runtime is O(n^2), quadratic time
def create_linked_list(input_list):
    """
    Function to create a linked list
    @param input_list: a list of integers
    @return: head node of the linked list
    """
    # head
    # i = 1
    # if head is None, create the head node
    # head.value = 1, head.next = None
    # i = 2
    # head is *not* None, create the next node
    # use head to get the first node
    # use current_node to move to the end of the list
    # then create the next node
    # i = 3, ... 

    head = None
    for i in input_list:
        if head is None:
            head = Node(i)
        else:
            current = head
            while current.next:
                current = current.next
            current.next = Node(i)
        
    return head

"""
input_values = [1, 2, 3, 4, 5, 6]
new_head = create_linked_list(input_values)
print('create a new linked list, the values are: ')
print_linked_list(new_head)
"""

# create linked list: method 2
# runtime is O(n), linear time
def create_linked_list_better(input_values):
  head = None
  tail = None

  for value in input_values:
    if head is None:
      head = Node(value)
      tail = head
    else:
      tail.next = Node(value)
      tail = tail.next

  return head
"""
input_values = [1, 2, 3, 4, 5, 6]
new_head = create_linked_list_better(input_values)
print('create a new linked list, the values are: ')
print_linked_list(new_head)
"""

"""
# Define a Singly Linked List class with methods that operate on the list

# Define a node
class Node:
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  # add a node to the end of the list
  # method takes O(n) time, linear time
  def append(self, value):
    if self.head is None:
      self.head = Node(value)
      return
    
    node = self.head
    while node.next:
      node = node.next
    
    node.next = Node(value)
    node = node.next
    return
  
  # convert linked list to a Python list
  def to_list(self):
    # iterate through linked list and insert value of each node into the python list
    # get the head
    node = self.head
    py_list = []
    
    while node:
      py_list.append(node.value)
      node = node.next
    
    return py_list


# create a LinkedList object
linked_list = LinkedList()

# create nodes for the linked list
linked_list.append(1)
linked_list.append(2)
linked_list.append(3)

# print out values of linked list
node = linked_list.head
while node:
  print(node.value)
  node = node.next
"""

# Define a doubly linked list class with methods that operate on the list
"""
class DoubleNode:
  def __init__(self, value):
    self.value = value
    self.next = None
    self.previous = None


class DoublyLinkedList:
  def __init__(self):
    self.head = None 
    self.tail = None

  # add a node to the end of a doubly linked list in contant time, O(1) time.
  def append(self, value):
    # get the head
    if self.head is None:
      self.head = DoubleNode(value)
      self.tail = self.head
      return

    self.tail.next = DoubleNode(value)
    self.tail.next.previous = self.tail
    self.tail = self.tail.next
    return 
    
# create a doubly linked list and add nodes to the list
doubly_linked_list = DoublyLinkedList()
doubly_linked_list.append(4)
doubly_linked_list.append(5)
doubly_linked_list.append(6)

"""
# print the nodes of the doubly linked list
"""
node = doubly_linked_list.head
while node:
  print(node.value)
  node = node.next
"""

class Node:
  def __init__(self, value):
    self.value = value
    self.next = None


class LinkedList:
  def __init__(self):
    self.head = None
  
  # runtime: O(1) time, constant time
  def prepend(self, value):
    if self.head is None:
      self.head = Node(value)
      return 
    
    new_head = Node(value)
    new_head.next = self.head
    self.head = new_head
    return

  def search(self, value):
    if self.head is None:
      return None

    node = self.head
      
    while node:
      if node.value is value:
        return node
      node = node.next

    return None

# Test prepend
linked_list = LinkedList()
linked_list.prepend(1)
linked_list.prepend(2)
linked_list.prepend(3)

node = linked_list.head

while node:
  print(node.value)
  node = node.next

# Test search
"""
found_node = linked_list.search(2)
print('found node', found_node.value)
"""

# Runtime: O(n), linear time
def remove(self, value):
  """ Remove first occurrence of value. """

  if self.head is None:
      return

  if self.head.value == value:
      self.head = self.head.next
      return

  node = self.head

  while node.next:
    if node.next.value == value:
        node.next = node.next.next
        return
    node = node.next

def pop(self):
  """ Return the first node's value and remove it from the list. """

  if self.head is None:
      return None

  node = self.head
  self.head = self.head.next

  return node.value
  