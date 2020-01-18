# create a node 
class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

head = Node(2)
new_node = Node(1)
head.next = new_node

print(new_node.value)
print(head.next.value)

# create several nodes and link them together

head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)

# traverse a linked list

current_node = head

while current_node.next is not None:
	print(current_node.value)
	current_node = current_node.next 
