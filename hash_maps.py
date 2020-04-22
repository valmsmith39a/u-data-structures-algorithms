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


class LinkedListNode:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashMap():

    def __init__(self, initial_size=10):
        self.bucket_array = [None for _ in range(initial_size)]
        self.p = 37  # or 31
        self.num_entries = 0

    def put(self, key, value):
        bucket_index = self.get_bucket_index(key)
        new_node = LinkedListNode(key, value)
        head = self.bucket_array[bucket_index]

        # if key is present in map, update the value
        while head is not None:
            if head.key == key:
                head.value = value
                return
            head = head.next

        # key not found in chain -> create new entry, insert at head of chain
        head = self.bucket_array[bucket_index]
        new_node.next = head
        self.bucket_array[bucket_index] = new_node
        self.num_entries += 1

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
