"""
Q1. Stack
Implement stack with `myStack` using given `LinkedNode`.

`myStack` Class Methods:  
- `push(x)`: Add a `LinkedNode` that has val x to `myStack`.
- `pop()`: Remove the most recently added `LinkedNode` from `myStack`.
- `top()`: Return val of the most recently added `LinkedNode`.
- `getSize()`: Return the number of `LinkedNode`s in `myStack`.
- `isEmpty()`: Return True if `myStack` is empty, or False otherwise.
- `clear()`: Remove all `LinkedNode`s.
- `status_check()`: prints status of stack.
"""


### Define `LinkedNode` class for future usage, do not modify!
class LinkedNode():
    def __init__(self,x):
        self.val = x
        self.next = None


class myStack():
    def __init__(self):
        self.sentinel = LinkedNode(0)
        self.size = 0

    def push(self, x):
        # Write your code
        pass

    def pop(self):
        # Write your code
        pass

    def top(self):
        # Write your code
        pass
    def getSize(self):
        # Write your code
        pass

    def isEmpty(self):
        # Write your code
        pass

    def clear(self):
        # Write your code
        pass

    # Do not modify
    def status_check(self):
        if self.isEmpty():
            print("IsEmpty:",self.isEmpty(), " | Size:", self.getSize(),"| Top:", self.top(), end = " ")
        else:
            print("IsEmpty:",self.isEmpty(), "| Size:", self.getSize(),"| Top:", self.top(),  end = " ")