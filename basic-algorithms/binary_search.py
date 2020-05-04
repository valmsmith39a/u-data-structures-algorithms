# Udacity solution
def binary_search(array, target):
    """Write a function that implements the binary search algorithm using iteration

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found"""
    start_index = 0
    end_index = len(array) - 1

    while start_index <= end_index:
        # integer division in Python 3
        mid_index = (start_index + end_index)//2

        mid_element = array[mid_index]

        if target == mid_element:                       # we have found the element
            return mid_index

        elif target < mid_element:                      # the target is less than mid element
            end_index = mid_index - 1                   # we will only search in the left half

        else:                                           # the target is greater than mid element
            # we will search only in the right half
            start_index = mid_element + 1

    return -1


# def test_function(test_case):
#     answer = binary_search(test_case[0], test_case[1])
#     if answer == test_case[2]:
#         print("Pass!")
#     else:
#         print("Fail!")


# array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# target = 6
# index = 6
# test_case = [array, target, index]
# test_function(test_case)


# Udacity solution
def binary_search_recursive(array, target, start_index, end_index):
    '''Write a function that implements the binary search algorithm using recursion

    args:
      array: a sorted array of items of the same type
      target: the element you're searching for

    returns:
      int: the index of the target, if found, in the source
      -1: if the target is not found
    '''
    if start_index > end_index:
        return -1

    mid_index = (start_index + end_index)//2
    mid_element = array[mid_index]

    if mid_element == target:
        return mid_index
    elif target < mid_element:
        return binary_search_recursive(array, target, start_index, mid_index - 1)
    else:
        return binary_search_recursive(array, target, mid_index + 1, end_index)


def test_function(test_case):
    answer = binary_search_recursive(
        test_case[0], test_case[1], 0, len(test_case[0]) - 1)
    if answer == test_case[2]:
        print("Pass!")
    else:
        print("Fail!")


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 4
index = 4
test_case = [array, target, index]
test_function(test_case)
