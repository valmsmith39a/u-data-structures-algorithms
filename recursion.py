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
