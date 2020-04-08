class Node():

    __init__(self, value):
        self.value = value
        self.next = None


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enqueue(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = self.head

        else:
            self.tail.next = node
            self.tail = self.tail.next

        self.num_elements += 1
