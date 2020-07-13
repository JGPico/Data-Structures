"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
from singly_linked_list import Node, LinkedList
import sys
sys.path.append('../singly_linked_list/')


class Queue:
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

    def enqueue(self, value):
        # self.values.insert(0, value)
        self.values.add_to_tail(value)

    def dequeue(self):
        # if self.values == []:
        #     return None
        # else:
        #     return self.values.pop()
        if self.values.head == None:
            return None
        else:
            return self.values.remove_head()
