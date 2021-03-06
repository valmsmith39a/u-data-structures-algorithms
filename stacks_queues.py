class Stack:

  def __init__(self, initial_size = 10):
    self.arr = [ 0 for _ in range(initial_size)]
    self.next_index = 0
    self.num_elements = 0

  def push(self, data):
    if(self.next_index == len(self.arr)):
      print("Out of space! Increasing array capacity ...")
      self._handle_stack_capacity_full()

    self.arr[self.next_index] = data
    self.next_index += 1 
    self.num_elements += 1

  def pop(self):
    if self.is_empty():
      self.next_index = 0
      return None
    self.next_index -= 1
    self.num_elements -= 1
    return self.arr[self.next_index]

  def _handle_stack_capacity_full(self):        
        old_arr = self.arr
        self.arr = [0 for _ in range(2*len(old_arr))]
        
        for idx, element in enumerate(old_arr):
            self.arr[idx] = old_arr[idx]

  def size(self):
    return self.num_elements

  def is_empty(self):
    return self.num_elements == 0

"""
# Test creating the Stack
foo = Stack()
print('Pass' if foo.arr == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] else 'Fail')

# Test pushing to the Stack
foo = Stack()
foo.push('Test')
print('Pass' if foo.arr[0] == 'Test' else 'Fail')

# Handle stack overflow
foo = Stack()
foo.push(1)
foo.push(2)
foo.push(3)
foo.push(4)
foo.push(5)
foo.push(6)
foo.push(7)
foo.push(8)
foo.push(9)
foo.push(10) # Array at capacity
foo.push(11) # Array increases in size
print(foo.arr) # new array
print("Pass" if len(foo.arr) == 20 else "Fail") # Array size should be 20 if doubled the size

# size and is_empty
foo = Stack()
foo.push('test')
print(foo.is_empty())
print(foo.size())

# pop
foo = Stack()
foo.push('test1')
foo.push('test2')
print('Pass' if foo.pop() == 'test2' else 'Fail')
print('Pass' if foo.pop() == 'test1' else 'Fail')
print('Pass' if foo.pop() == None else 'Fail')
"""
