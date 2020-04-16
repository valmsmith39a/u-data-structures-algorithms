# this code makes the tree that we'll traverse


class Node(object):

    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root


tree = Tree('apple')
tree.get_root().set_left_child(Node('banana'))
tree.get_root().set_right_child(Node('cherry'))
tree.get_root().get_left_child().set_left_child(Node('dates'))

# Binary tree traversal depth first, pre-order traversal with a stack
# Stack using a list


class Stack():

    def __init__(self):
        self.list = list()

    def push(self, value):
        self.list.append(value)

    def pop(self):
        return self.list.pop()

    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        return None

    def is_empty(self):
        return len(self.list) == 0

    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item)
                                               for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s

        else:
            return "<stack is empty>"


# check Stack
stack = Stack()
stack.push("apple")
stack.push("banana")
stack.push("cherry")
stack.push("dates")
print(stack.pop())
print("\n")
print(stack)

###

visit_order = list()
stack = Stack()

node = tree.get_root()
stack.push(node)

print(f"""
visit_order {visit_order}
stack:
{stack}
""")

visit_order.append(node.get_value())
print(f"""visit order {visit_order} 
{stack})
""")

print(f"{node} has left child? {node.has_left_child()}")

print(node.get_left_child())

if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")

print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order {visit_order}""")

# depth first search, pre-order traversal
# get the node and push it to the stack
# visit the node (get_value) and add it to the visit_order

print(f"{node} has left child? {node.has_left_child()}")

if node.has_left_child():
    node = node.get_left_child()
    stack.push(node)

print(f"""
visit_order {visit_order} 
stack:
{stack}
""")

print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order {visit_order}""")

print(f"{node} has left child? {node.has_left_child()}")

print(f"{node} has right child? {node.has_right_child()}")

print(stack)

# *** Since the dates node is a leaf node we can pop it off the stack ***
print(stack.pop())

print(stack)

# now we'll set the node to the new top of the stack, which is banana
node = stack.top()

# now check banana's right child
print(f"{node} has right child? {node.has_right_child()}")

# banana doesn't have a right child, done tracking it
# so we pop banana off the stack
print(f"pop {stack.pop()} off stack")
print(f"""
stack
{stack}
""")

# now we'll set the node to the new top of the stack, which is apple
node = stack.top()

print(node.has_right_child())

if node.has_right_child():
    node = node.get_right_child()
    stack.push(node)
    
print(f"""
visit_order {visit_order} 
stack
{stack}""")

# visit cherry
print(f"visit {node}")
visit_order.append(node.get_value())
print(f"""visit_order: {visit_order}""")

# Now we'll check if cherry has a left child
print(f"{node} has left child? {node.has_left_child()}")

# it doesn't, so we'll check if it has a right child
print(f"{node} has right child? {node.has_right_child()}")

# since cherry has neither left nor right child nodes,
# we are done tracking it, and can pop it off the stack

print(f"pop {stack.pop()} off the stack")

print(f"""
visit_order {visit_order} 
stack
{stack}
""")

print(f"pop {stack.pop()} off stack")
print(f"pre-order traversal visited nodes in this order: {visit_order}")

class State(object):
    def __init__(self,node):
        self.node = node
        self.visited_left = False
        self.visited_right = False
        
    def get_node(self):
        return self.node
    
    def get_visited_left(self):
        return self.visited_left
    
    def get_visited_right(self):
        return self.visited_right
    
    def set_visited_left(self):
        self.visited_left = True
        
    def set_visited_right(self):
        self.visited_right = True
        
    def __repr__(self):
        s = f"""{self.node}
visited_left: {self.visited_left}
visited_right: {self.visited_right}
        """
        return s

def pre_order_with_stack(tree, debug_mode=False):
  visit_order = list()
  stack = Stack()
  node = tree.get_root()
  visit_order.append(node.get_value())
  state = State(node)
  stack.push(state)
  count = 0

  while(node):
    count += 1

    if node.has_left_child() and not state.get_visited_left():
      state.set_visited_left()
      node = node.get_left_child()
      visit_order.append(node.get_value())
      state = State(node)
      stack.push(state)

    elif node.has_right_child() and not state.get_visited_right():
      state.set_visited_right()
      node = node.get_right_child()
      visit_order.append(node.get_value())
      state = State(node)
      stack.push(state)
    
    else: 
      stack.pop()

      if not stack.is_empty():
        state = stack.top()
        node = state.get_node()
      else: 
        node = None

    return visit_order


      


  


  


