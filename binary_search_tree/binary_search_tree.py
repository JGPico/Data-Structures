"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        pass
        # Case 1 value is less than self.value
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)

        # Case 2 value is greater than or equal to self.value
        elif value >= self.value:
            if self.right is None:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not

    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True
        # Case 2: if target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # fuhgedabout the left subtree
        # iterate throught he nodes using a loop construct

        # current = self
        # while current.right != None:
        #     if current.right is None:
        #         return current.value
        #     else:
        #         current = current.right
        # return current.value

        # Recursive approach
        if not self.right:
            return self.value
        return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # recursive
        fn(self.value)

        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return
        # check if can move left
        if self.left:
            self.left.in_order_print()

        # visit the node
        print(self.value)

        # check if can move right
        if self.right:
            self.right.in_order_print()

        # visit the node
        print(self.value)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass
        # Use a queue to form a "line"
        # for the nodes to get in

        # start by placing the root in the queue

        # need a while loop to iteratate using queue length
        while None:
            pass
            # dequeue item from front of queue
            # print that item

            # place current item's left node in queue if not None

            # place current items's right node in queue if not None

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass
        # initialize an empty stack
        # push the root node onto the stack

        # need a while loop to iterate
        while None:
            pass
            # check if stack is not empty, enter the while loop
            if None:
                pass
                # pop top item off the stack
                # print that item's value

                # if right subtree
                # push right item onto the stack

                # if left subtree
                # push left item onto the stack

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
