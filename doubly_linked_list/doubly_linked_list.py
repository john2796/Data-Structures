

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

    def add_to_head(self, value):
        new_node = ListNode(value)
        if not self.head and not self.tail:  # empty node
            self.head = new_node
            self.tail = new_node
        else:  # more than one node
            cur_head = self.head
            self.head = new_node
            self.head.next = cur_head
        self.length += 1            # psuedo code
        # 1 head  <-->, prev 2 , next  <--> 3 tail
        # 4 ---> 1 head  <-->, prev 2 , next  <--> 3 tail
        # 4 head ---> 1 head_next  <-->, prev 2 , next  <--> 3 tail
        pass

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
    # * [x]  `add_to_tail` replaces the tail of the list with a new value that is passed in.

    def add_to_tail(self, value):
        new_node = ListNode(value)  # hold value of what we want to ad
        if not self.head and not self.tail:  # empty list
            self.head = new_node  # 1 head and tail
            self.tail = new_node
        else:  # if we have one or more node
            curr_tail = self.tail  # hold entire value of current node
            self.tail.next = new_node  # 1 (head) --> 2 (tail) pointer
            self.tail = new_node  # node
            self.tail.prev = curr_tail
        self.length += 1
        pass

    # * []  `remove_from_tail` removes the tail node and returns the value stored in it.
    def remove_from_tail(self):
        if not self.head and not self.tail:
            return None
        old_tail = self.tail
        if self.head == self.tail:  # means there's only one
            self.tail = None
            self.head = None
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

    # * []  `move_to_front` takes a reference to a node in the list and moves it to the front of the list, shifting all other list nodes down.
    def move_to_front(self, node):

        pass

    # * []  `move_to_end` takes a reference to a node in the list and moves it to the end of the list, shifting all other list nodes up.
    def move_to_end(self, node):
        pass

    # * []  `delete` takes a reference to a node in the list and removes it from the list. The deleted node's `previous` and `next` pointers should point to each afterwards.
    def delete(self, node):
        pass

    # * []  `get_max` returns the maximum value in the list.
    def get_max(self):
        pass


test = DoublyLinkedList()
print(test.add_to_tail(1))
print(test.add_to_tail(2))
print(test.add_to_tail(3))
print(test.add_to_head(4))
print(test.remove_from_tail(), '--> removed tail')
print(test.__len__(), '--> length')
print(test.display())


#     """Wrap the given value in a ListNode and insert it
#   after this node. Note that this node could already
#   have a next node it is point to."""

#     def insert_after(self, value):  # 1(curr) --> 2 (next)
#         current_next = self.next  #
#         self.next = ListNode(value, self, current_next)
#         if current_next:
#             # self.next.prev (current) = self.next
#             current_next.prev = self.next

#     """Wrap the given value in a ListNode and insert it
#   before this node. Note that this node could already
#   have a previous node it is point to."""

#     def insert_before(self, value):
#         current_prev = self.prev
#         self.prev = ListNode(value, current_prev, self)
#         if current_prev:
#             current_prev.next = self.prev

#     """Rearranges this ListNode's previous and next pointers
#   accordingly, effectively deleting this ListNode."""

#     def delete(self):
#         if self.prev:
#             self.prev.next = self.next
#         if self.next:
#             self.next.prev = self.prev


# """Our doubly-linked list class. It holds references to
# the list's head and tail nodes."""
