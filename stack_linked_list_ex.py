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

def test_function_post_fix(test_case):
    output = evaluate_post_fix(test_case[0])
    print(output)
    if output == test_case[1]:
        print("Pass")
    else:
        print("Fail")

test_case_1 = [["3", "1", "+", "4", "*"], 16]
test_function_post_fix(test_case_1)

test_case_2 = [["4", "13", "5", "/", "+"], 6]
test_function_post_fix(test_case_2)

test_case_3 = [["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22]
test_function_post_fix(test_case_3)

def reverse_stack(stack):
    """
    Reverse a given input stack

    Args:
        stack(stack): Input stack to be reversed
    Returns:
        stack: Reversed Stack
    """

    holder_stack = Stack()
    while not stack.is_empty():
        popped_element = stack.pop()
        holder_stack.push(popped_element)

    return holder_stack

def reverse_stack_recursion(stack, holder_stack):
    if stack.is_empty():
      return
    holder_stack.push(stack.pop())
    reverse_stack_recursion(stack, holder_stack)

def test_function(test_case):
    stack = Stack()
    holder_stack = Stack() # own addition for recursive version
    for num in test_case:
        stack.push(num)
    
    reverse_stack(stack)
    reverse_stack_recursion(stack, holder_stack)
    index = 0
    while not stack.is_empty():
        popped = stack.pop()
        if popped != test_case[index]:
            print("Fail")
            return
        else:
            index += 1
    print("Pass")

test_case_1 = [1, 2, 3, 4]
test_function([1, 2, 3, 4])

test_case_2 = [1]
test_function(test_case_2)
