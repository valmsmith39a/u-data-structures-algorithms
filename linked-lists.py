# create a node 
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

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

# print a linked list (to test create method later)
def print_linked_list(head):
	current_node = head
	while current_node.next is not None:
		print(current_node.value)
		current_node = current_node.next


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

input_values = [1, 2, 3, 4, 5, 6]
new_head = create_linked_list_better(input_values)
print('create a new linked list, the values are: ')
print_linked_list(new_head)
