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
        bucket_index = self.get_hash_code(key)
        head = self.bucket_array[bucket_index]
        while head is not None:
            if head.key == key:
                return head.value
            head = head.next
        return None

    def get_bucket_index(self, key):
        return self.get_hash_code(key)

    def get_hash_code(self, key):
        key = str(key)
        num_buckets = len(self.bucket_array)
        current_coefficient = 1
        hash_code = 0

        for character in key:
            hash_code += ord(character) * current_coefficient
            hash_code = hash_code % num_buckets
            current_coefficient *= self.p
            current_coefficient = current_coefficient % num_buckets

        return hash_code % num_buckets

    def size(self):
        return self.num_entries


hash_map = HashMap()

hash_map.put("one", 1)
hash_map.put("two", 2)
hash_map.put("three", 3)
hash_map.put("neo", 11)
hash_map.put("mary", 55)
hash_map.put("john", 59)

print("size: {}".format(hash_map.size()))
print("one: {}".format(hash_map.get("one")))
print("neo: {}".format(hash_map.get("neo")))
print("three: {}".format(hash_map.get("three")))
print("john's height {}".format(hash_map.get("john")))
print("mary's heigh {}".format(hash_map.get("mary")))
print("size: {}".format(hash_map.size()))
