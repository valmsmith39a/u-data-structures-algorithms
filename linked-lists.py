class Node:
	def __init__(self, value):
		self.value = value
		self.next = None

head = Node(1)
new_node = Node(2)
head.next = new_node

print(new_node.value)
print(head.next.value)
