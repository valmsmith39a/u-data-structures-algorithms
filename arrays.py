# runtime: O(n)
def add_one(arr):
    output = 1;

    for i in range(len(arr), 0, -1):
        output = output + arr[i - 1]
        borrow = output//10
        if borrow == 0:
            arr[i - 1] = output
            break
        else:
            arr[i - 1] = output % 10
            output = borrow
    arr = [borrow] + arr
    index = 0
    while arr[index]==0:
        index += 1
    return arr[index:]

# time complexity: O(n), linear time
# space complexity: O(1), constant space
def duplicate_number(arr):
    current_sum = 0
    expected_sum = 0
    
    for num in arr:
        current_sum += num
        
    for i in range(len(arr) - 1):
        expected_sum += i
        
    return current_sum - expected_sum

# get max subarray method 1
def max_sum_subarray(arr):
  """
  :param - arr - input array
  return - number - largest sum in contiguous subarry within arr
  """
  size = len(arr)
  sums = []
  for i, num_i in enumerate(arr):
      for j, num_j in enumerate(arr):
          sums.append(sum(arr[i: size - j]))

  return max(sums)

# get max subarray method 2
def max_sum_subarray2(arr):
  max_sum = arr[0]
  current_sum = arr[0]

  for num in arr[1:]:
      current_sum = max(current_sum + num, num)
      max_sum = max(current_sum, max_sum)
  return max_sum

  # Pascal's Triangle
  # Method 1
  # runtime: O(n^2 + n)
  def nth_row_pascal(n):
    row = []
    prev_row = []
    
    if n == 0:
        return [1]
    
    for i in range(n):
        if i == 0:
            prev_row = [0, 1, 0]
            for idx, num in enumerate(prev_row):
                if idx == (len(prev_row) - 1):
                    break
                row.append(num + prev_row[idx + 1])
        else:
            prev_row = row
            prev_row.insert(0, 0)
            prev_row.append(0)
            row = []
            for idx, num in enumerate(prev_row):
                if idx == (len(prev_row) - 1):
                    break
                row.append(num + prev_row[idx + 1])
            
    return row 

# Pascal's Triangle: Solution 2

def nth_row_pascal(n):
  if n == 0:
      return [1]

  current_row = [1]
  for i in range(1, n + 1):
      prev_row = current_row
      current_row = [1]
      for j in range(1, i):
          next_number = prev_row[j] + prev_row[j-1]
          current_row.append(next_number)
      current_row.append(1)
  return current_row

  # even after odd
  def even_after_odd(head):
    """
    :param - head - head of linked list
    return - updated list with all even elements are odd elements
    """
    even = None
    even_tail = None
    odd = None
    odd_tail = None
    
    if head is None:
        return head
    
    while head:
        next_node = head.next
        
        if head.data % 2 == 0:
            if even is None:
                even = head
                even_tail = even
            else:
                even_tail.next = head
                even_tail = even_tail.next
        else: 
            if odd is None:
                odd = head
                odd_tail = odd
            else:
                odd_tail.next = head
                odd_tail = odd_tail.next
                
        head.next = None
        head = next_node
        
    if odd is None:
        return even
    odd_tail.next = even
    return odd

# skip i delete j
def skip_i_delete_j(head, i, j):
    """
    :param: head - head of linked list
    :param: i - first `i` nodes that are to be skipped
    :param: j - next `j` nodes that are to be deleted
    return - return the updated head of the linked list
    """
    if i == 0:
        return None
    
    if head is None or j < 0 or i < 0:
        return head
    
    current = head
    previous = None
    
    while current:
        for _ in range(i-1):
            if current == None:
                return head
            current = current.next
        previous = current
        current = current.next
        
        for _ in range (j):
            if current is None:
                break
            next_node = current.next
            current = next_node
        previous.next = current
    return head


# swap nodes - method 1
def swap_nodes(head, left_index, right_index):
    """
    :param: head- head of input linked list
    :param: left_index - indicates position
    :param: right_index - indicates position
    return: head of updated linked list with nodes swapped
    """
    
    if head is None:
        return head
    
    node = head
    i_node = None
    j_node = None
    i_prev_node = None
    j_node_node = None
    idx = 0

    while node:
        idx += 1
        
        if left_index == 0:
            i_node = head
            i_prev_node = i_node
            head = i_node
            
        if idx == left_index - 1:
            i_prev_node = node
            i_node = node.next
            
        elif idx == right_index - 1:
            j_prev_node = node
            j_node = node.next
        
            i_prev_node.next = j_node
            j_prev_node.next = i_node
            
            temp_next_node = i_node.next
            i_node.next = j_node.next
            j_node.next = temp_next_node

        node = node.next
    
    return head
