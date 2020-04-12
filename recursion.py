def sum_integers(n):
    if n == 1:
        return 1

    return n + sum_integers(n - 1)


print(sum_integers(4))


def sum_array(array):
    # Base Case
    if len(array) == 1:
        return array[0]

    return array[0] + sum_array(array[1:])


arr = [1, 2, 3, 4]
print(sum_array(arr))


def sum_array_index(array, index):
    # Base Cases
    if len(array) - 1 == index:
        return array[index]

    return array[index] + sum_array_index(array, index + 1)


arr = [1, 2, 3, 4]
print(sum_array_index(arr, 0))


def sum_array_iter(array):
    result = 0

    for x in array:
        result += x

    return result


arr = [1, 2, 3, 4]
print(sum_array_iter(arr))


def factorial(n):
    """
    Calculate n!

    Args:
       n(int): factorial to be computed
    Returns:
       n!
    """
    # 5! = 5 * 4!
    # 4! = 4 * 3!
    # ...
    # 2! = 2 * 1!
    # 1! = 1 * 0!
    # base case: n = 0, return 1
    # factorial(5) = 5 * factorial(4)
    # factorial(4) = 4 * factorial (3)
    if n == 0:
        return 1

    return n * factorial(n-1)


def reverse_string(input):
    """
    Return reversed input string

    Examples:
        reverse_string("abc") returns "cba"

    Args:
      input(str): string to be reversed

    Returns:
      a string that is the reverse of input
    """

    if len(input) == 0:
        return ""
    return input[-1] + reverse_string(input[0:-1])


# Test Cases
print("Pass" if ("" == reverse_string("")) else "Fail")
print("Pass" if ("cba" == reverse_string("abc")) else "Fail")


def is_palindrome(input):
    """
    Return True if input is palindrome, False otherwise.
    
    Args:
       input(str): input to be checked if it is palindrome
    """
    
    if len(input) <= 1:
        return True
    
    return input[0] == input[-1] and is_palindrome(input[1:-1])

# Test Cases

print ("Pass" if  (is_palindrome("")) else "Fail")
print ("Pass" if  (is_palindrome("a")) else "Fail")
print ("Pass" if  (is_palindrome("madam")) else "Fail")
print ("Pass" if  (is_palindrome("abba")) else "Fail")
print ("Pass" if not (is_palindrome("Udacity")) else "Fail")

import copy

def permute(l):
    """
    Return a list of permutations
    
    Examples:
       permute([0, 1]) returns [ [0, 1], [1, 0] ]
    
    Args:
      l(list): list of items to be permuted
    
    Returns:
      list of permutation with each permuted item being represented by a list
    """  
    perm = []
    if len(l) == 0:
        perm.append([])
    else:
        first_element = l[0]
        after_first = slice(1, None)
        sub_permutes = permute(l[after_first])
        for p in sub_permutes:
            for j in range(0, len(p) + 1):
                r = copy.deepcopy(p)
                r.insert(j, first_element)
                perm.append(r)
    return perm

    # Test Cases 

# Helper Function
def check_output(output, expected_output):
    """
    Return True if output and expected_output
    contains the same lists, False otherwise.
    
    Note that the ordering of the list is not important.
    
    Examples:
        check_output([ [0, 1], [1, 0] ] ], [ [1, 0], [0, 1] ]) returns True

    Args:
        output(list): list of list
        expected_output(list): list of list
    
    Returns:
        bool
    """
    o = copy.deepcopy(output)  # so that we don't mutate input
    e = copy.deepcopy(expected_output)  # so that we don't mutate input
    
    o.sort()
    e.sort()
    return o == e

print ("Pass" if  (check_output(permute([]), [[]])) else "Fail")
print ("Pass" if  (check_output(permute([0]), [[0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1]), [[0, 1], [1, 0]])) else "Fail")
print ("Pass" if  (check_output(permute([0, 1, 2]), [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]])) else "Fail")

