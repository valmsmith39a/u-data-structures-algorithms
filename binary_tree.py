class Node(object):
    
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
        
    def get_value(self):
        return self.value
        
    def set_value(self, value):
        self.value = value
        
    def set_left_child(self, node):
        self.left = node
        
    def set_right_child(self, node):
        self.right = node
        
    def get_left_child(self, node):
        return self.left
    
    def get_right_child(self, node):
        return self.right

node0 = Node()
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

node0 = Node()
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

node0 = Node("apple")
print(f"""
value: {node0.value}
left: {node0.left}
right: {node0.right}
""")

node0 = Node("apple")
node1 = Node("banana")
node2 = Node("orange")
node0.set_left_child(node1)
node0.set_right_child(node2)

print(f"""
node 0: {node0.value}
node 0 left child: {node0.left.value}
node 0 right child: {node0.right.value}
""")