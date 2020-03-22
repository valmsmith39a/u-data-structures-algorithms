class Stack:

  def __init__(self, initial_size = 10):
    self.arr = [ 0 for _ in range(initial_size)]
    self.next_index = 0
    self.num_elements = 0

  def push(self, data):
    self.arr[self.next_index] = data
    self.next_index += 1 
    self.num_elements += 1

"""
# Test creating the Stack
foo = Stack()
print('Pass' if foo.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] else 'Fail')

# Test pushing to the Stack
foo = Stack()
foo.push('Test')
print('Pass' if foo.arr[0] == 'Test' else 'Fail')
"""




