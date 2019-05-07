
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:
    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None
        # what data structure should we
        # use to store queue elements?
        # self.storage = []

    def enqueue(self, item):
        # `enqueue` should add an item to the back of the queue.
        new_node = Node(item)
        if not self.head and not self.tail:  # empty
            self.head = new_node
            self.tail = new_node
            self.size += 1
        else:
            self.tail.next_node = new_node
            self.tail = new_node
            self.size += 1
        pass

    def dequeue(self):
        # `dequeue` should remove and return an item from the front of the queue.
        if not self.head and not self.tail:  # empty
            return None
        if self.head == self.tail:  # if only one list item
            old_head = self.head
            self.head = None
            self.tail = None
            return old_head.value
        else:  # more than one item  1(removed)(h)(n) -> 2
            self.size -= 1
            old_head = self.head
            self.head = self.head.next_node
            return old_head.value

    def len(self):
        # `len` returns the number of items in the queue.
        if not self.head and not self.tail:
            return 0
        return self.size

    def display(self):
        elems = []
        cur = self.head
        while cur:
            elems.append(cur.value)
            cur = cur.next_node
        return elems


test = Queue()
# print(test.enqueue(1))
# print(test.enqueue(2))
# print(test.enqueue(3))
print(test.len())
print(test.dequeue(), '<---')
print(test.display())
