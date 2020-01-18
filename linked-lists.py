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

def create_linked_list(input_values):
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

def print_linked_list(head):
	current_node = head
	while current_node.next is not None:
		print(current_node.value)
		current_node = current_node.next

new_head = create_linked_list(input_values)
print('created a new linked list: ')
print_linked_list(new_head) 
