

# Doubly Linked Lists
#  * [x]  The `ListNode` class, which represents a single node in the doubly-linked list, has already been implemented for you. Inspect this code and try to understand what it is doing to the best of your ability.
"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""


class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

#  * [x]  The `DoublyLinkedList` class itself should have the methods: `add_to_head`, `add_to_tail`, `remove_from_head`, `remove_from_tail`, `move_to_front`, `move_to_end`, `delete`, and `get_max`.


class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        #  * [x]  The `head` property is a reference to the first node and the `tail` property is a reference to the last node.
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
#    * []  `add_to_head` replaces the head of the list with a new value that is passed in.

    def display(self):
        elems = []
        cur = self.head
        while cur:
            elems.append(cur.value)
            cur = cur.next
        return elems
    # * []  `remove_from_head` removes the head node and returns the value stored in

    def remove_from_head(self):
        if not self.head and not self.tail:  # empty node
            return None
        old_head = self.head
        if self.head == self.tail:  # only one item
            self.head = None
            self.tail = None
        else:  # more than one item   1(head) -->   2 ---> 3
            self.head = self.head.next  # 1 , 2 head , 3
            self.head.prev = None
            # {1} head  , prev 2 , next      3  tail
            #   ,   prev head 2 , next      3  tail
            #   ,   None   head 2 , next      3  tail
        self.length -= 1
        return old_head.value

    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        old_tail = self.tail
        if self.head == self.tail:  # means there's only one
            self.tail = None
            self.head = None
            self.length = 0
            return old_tail.value
        else:  # means more than one node
            self.tail = self.tail.prev
            self.tail.next = None
        self.length -= 1
        return old_tail.value
        #  head  <-->, prev 2 , next  <--> 3 tail
        #  head  <-->, prev 2 , next  <--> X3 tail (remove tail)
        #  head  <-->, prev 2 ,(added tail) next  <-->  x
        #  head  <-->, prev 2 ,(added tail) removed next  <-->  x
        pass

    def add_to_tail(self, value):
        new_node = ListNode(value)
        if self.head is None:  # no list add it to as first
            self.head = new_node
            self.head.prev = None
        else:  # adding to the end
            old_head = self.head
            while old_head.next:
                old_head = old_head.next
            new_node.next = None
            new_node.prev = old_head  # previous last node or tail
            old_head.next = new_node
        self.length += 1

    def add_to_head(self, value):  # add to first list
        new_node = ListNode(value)
        if self.head is None:
            new_node.prev = None
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node
            new_node.prev = None
        self.length += 1

    def add_after_node(self, key, data):
        old_head = self.head
        while old_head:
            # if next is none and data is equal to key , then we just need to end of the list
            if old_head.next is None and old_head.value == key:
                self.add_to_tail(data)
                return  # break while loop
            # a <--> b <--> c <--> d , insert E after b
            # a <--> b <--> e <--> c <--> d , insert E after b
            elif old_head.value == key:  # next is none which mean it's adding in the middle
                new_node = ListNode(data)
                nxt = old_head.next  # c
                old_head.next = new_node
                new_node.next = nxt  # point new node to the variable we stored nxt
                new_node.prev = old_head  # point E.prev to B
                nxt.prev = new_node  # point c prev to new node
            old_head = old_head.next  # keep loop
            self.length += 1

    def add_before_node(self, key, data):
        old_head = self.head
        while old_head:
            # which means there's only one node and we need to add_to_tail before node item
            if old_head.prev is None and old_head.value == key:
                # add_to_head will take care all the pointers
                self.add_to_head(data)
                return
            elif old_head.value == key:  # if old_head value is equal to key
                # a <--> b <--> c <--> d , insert E BEFORE C
                # a <--> b <--> E <-->  c <--> d , insert E BEFORE C
                new_node = ListNode(data)
                prev = old_head.prev
                prev.next = new_node
                old_head.prev = new_node
                new_node.prev = prev
                new_node.next = old_head
            old_head = old_head.next
            self.length += 1

    def move_to_front(self, node):
        old_head = self.head
        while old_head:
            if old_head is None and old_head.value == node:
                self.add_to_head(node)
                return
            elif old_head.value == node:  # found match to node then move it to the front
                # a <--> b <--> c <--> d , Find d and move it to the front
                # first remove that node and create a new one
                self.delete(node)
                self.add_to_head(node)
            old_head = old_head.next

    def move_to_end(self, node):
        old_head = self.head
        while old_head:
            if self.head is None and old_head.value == node:
                self.add_to_head(node)
            elif old_head.value == node:
                self.delete(node)
                self.add_to_tail(node)
            old_head = old_head.next

    def delete(self, node):
        cur = self.head
        while cur:
            if cur.value == node and cur == self.head:
                # case 1:
                if not cur.next:  # node to right is empty
                    cur = None
                    self.head = None
                    return
                # case 2: delete head node and pointers following to it
                else:
                    nxt = cur.next
                    cur.next = None  # remove head next
                    nxt.prev = None  # removed prev to null
                    cur = None
                    self.head = nxt
                    return
                # case 3: removed node that has prev and next ( or middle of list)
            elif cur.value == node:
                if cur.next:  # if it has a node after it
                    nxt = cur.next  # current next pointer cur is the value === node
                    prev = cur.prev  # current prev pointer
                    prev.next = nxt
                    nxt.prev = prev
                    cur.next = None  # all three removing pointers of the one we want to delete
                    cur.prev = None
                    cur = None
                    return
                # case 4: next is none but prev is available
                else:  # next is none
                    # a <---> b <---> c <---> d (remove last)
                    prev = cur.prev   # point to C
                    prev.next = None  # point C and set next to None
                    cur.prev = None  # remove prev of D because we're getting rid of it
                    cur = None
                    return
            self.length -= 1
            cur = cur.next  # move to next every iteration loop
        pass
# case 3 example: we want to remove b
        # a <---> b <---> c <---> d
        # first thing we need to do is hold the value and update pointers
        # nxt = cur.next ,  points to c
        # prev = cur.prev , points to a
        # prev.next = nxt , A <--> C move a next to c
        # next.prev = A <--> move prev C to A we're saying point C prev to be A
        # then get rid of B pointers prev and next

    # key things
    # case 1:  when we have node == to head
    # case 2:  when removing head make sure head.next is pointing to the next one  # case 4:  tail.prev is pointing to the new one
    # case 3:

    # * []  `get_max` returns the maximum value in the list.

    def get_max(self):
        if not self.head and not self.tail:
            return None
        if self.head == self.tail:
            return self.head
        cur = self.head
        elems = []
        while cur:
            elems.append(cur.value)
            cur = cur.next
        elems.sort()
        return elems[len(elems) - 1]

        # store max item


test = DoublyLinkedList()
print(test.add_to_head(1))
print(test.add_to_head(2))
print(test.add_to_tail(3))
print(test.add_to_tail(4))
print(test.add_to_tail(5))
print(test.move_to_end(3))
print(test.move_to_front(1))
print(test.get_max(), '-- max')
print(test.__len__(), '--> length')
print(test.display())
