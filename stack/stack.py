"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order. 

1. Implement the Stack class using an array as the underlying storage structure.
   Make sure the Stack tests pass.
2. Re-implement the Stack class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Stack?
"""
from singly_linked_list import Node, LinkedList


class Stack:
    def __init__(self):
        self.size = 0
        # self.values = []
        self.values = LinkedList()

    def __len__(self):
        # return len(self.values)
        current = self.values.head

        if current == None:
            return 0
        else:
            while current.get_next() is not self.values.tail:
                current = current.get_next()

        return current

    def push(self, value):
        # self.values.append(value)
        self.values.add_to_tail(value)

    def pop(self):
        # if self.values == []:
        #     return None
        # else:
        #     return self.values.pop()
        if self.values.head == None:
            return None
        else:
            return self.values.remove_tail()

    def peek(self):
        # if not self.values == []:
        #     return self.values[-1]
        if not self.values.head == None:
            return self.values.tail
