"""
Ex of simple hash function:
Sum the ascii value corresponding to 
each character

Problem is collisions. 'abcd' will produce
the same hash code as 'bcda'

"""


def hash_function(string):
    hash_code = 0
    for c in string:
        hash_code += ord(c)
    return hash_code


print(hash_function('abcd'))
