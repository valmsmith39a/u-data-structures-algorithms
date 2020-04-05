class LinkedListNode:

    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.num_elements = 0
        self.head = None

    def push(self, data):
        new_node = LinkedListNode(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.num_elements += 1

    def pop(self):
        if self.is_empty():
            return None
        temp = self.head.data
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def top(self):
        if self.head is None:
            return None
        return self.head.data

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

def evaluate_post_fix(input_list):
    """
    Evaluate the postfix expression to find the answer

    Args:
       input_list(list): List containing the postfix expression
    Returns:
       int: Postfix expression solution
    """
    
    stack = Stack()
    
    for x in input_list:
        if x == '+':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 + operand2
            stack.push(result)
        elif x == '-':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 - operand2
            stack.push(result)
        elif x == '*':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = operand1 * operand2
            stack.push(result)
        elif x == '/':
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = int(operand1 / operand2)
            stack.push(result)                       
        else:
            stack.push(int(x))
    
    return stack.pop()
    