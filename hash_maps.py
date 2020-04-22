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


class HashMap():

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37  # or 31
        self.num_entries = 0

    def put(self, key, value):
        pass

    def get(self, key):
        pass

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        current_coefficient = 1
        hash_code = 0

        for character in key:
            hash_code += ord(character) * current_coefficient
            current_coefficient *= self.p
            current_coefficient = current_coefficient

        return hash_code

    def size(self):
        return self.num_entries
