"""
# 5-1. Nested Singly Linked Lists (2.pt)
Implement a nested singly linked list (SLL), where the value of the outer SLL is the head of an inner SLL. First, implement the `OuterNode` class that will act as the outer linked node class and its methods.
"""

# Do not modify
class InnerNode:
  def __init__(self, value = None, next = None):
    self.value = value
    self.next = next

# Write your code here about `OuterNode`
"""
    OuterNode Represents an outer node in a nested singly linked list (SLL). Each outer node contains an 
    inner singly linked list.

    Intializer
      Initializes an `OuterNode` with a given maximum inner list size, head value, and next node.
          
      :param maxsize: The maximum allowed size of the inner SLL. (int)
      :param value: The head of the inner SLL. (InnerNode or None)
      :param next: The next node in the outer SLL. (OuterNode or None)
      
    isfull
      Checks if the inner singly linked list has reached its maximum size.
      
      :return: `True` if the inner SLL is full, otherwise `False`. (bool)
    
    __len__
      Returns the current size of the inner singly linked list.
      
      :return: The number of elements in the inner SLL. (int)
"""


"""
# Example Usage
innernode1 = InnerNode(value=1, next=None)
outernode = OuterNode(maxsize=2, value=innernode1, next=None)

print(outernode.isfull()) # Expected Output: False
print(len(outernode)) # Expected Output: 1

innernode2 = InnerNode(value=2, next=innernode1)  # Fixed reference to previous node
outernode.value = innernode2
outernode.currsize += 1  # Note: There is no method for automatically updating currsize here. It will be implemented in 5-2.

print(outernode.isfull()) # Expected Output: True
print(len(outernode)) # Expected Output: 2
"""


"""
# 5-2. Nested Singly Linked Lists (5.pt)

Using the `OuterNode` class, implement the `NestedSLL` class to manage a nested singly linked list (SLL).  
"""

class NestedSLL:
    def __init__(self, maxsize):
        """
        Initializes the NestedSLL with a given maximum size for the first outer node.
        
        :param maxsize: The maximum size of the first outer linked node. (int)
        """
        # Write your code here

    def get_size(self):
        """
        Calculates the number of outer linked nodes and the total number of inner linked nodes in the nested SLL.

        :return: A tuple containing:
                - The number of outer linked nodes. (int)
                - The number of inner linked nodes. (int)
        """
        # Write your code here
    
    def append(self, value):
        """
        Appends a value to the nested SLL. If the current inner SLL is full, creates a new outer node
        with double the `maxsize` of the previous node and adds the value to it.

        Must operate under constant time complexity O(1).

        :param value: The value to append. (int)
        """
        # Write your code here

    def pop(self):
        """
        Removes and returns the last-inserted value from the nested SLL.

        Must operate under constant time complexity O(1). If the outer node becomes empty
        after the pop and there's a `next` outer node, the current outer node is removed.

        :return: The popped value. (int or None)
        """
        # Write your code here
    
    def to_list(self):
        """
        Converts the nested SLL into a nested list of integers.

        :return: A nested list representing the values in the nested SLL. (list[list[int]])
        """
        # Write your code here

"""
### **Example Usage**
# Create a nested SLL with an initial maxsize of 1
mySLL = NestedSLL(maxsize=1)
print(mySLL.head.maxsize) # Expected Output: 1
print(mySLL.get_size()) # Expected Output: (1, 0)

# Append values
mySLL.append(value=1)
print(mySLL.get_size()) # Expected Output: (1, 1)
print(mySLL.to_list()) # Expected Output: [[1]]

# Append more values
mySLL.append(value=2)
mySLL.append(value=3)

print(mySLL.get_size()) # Expected Output: (2, 3)
print(mySLL.to_list()) # Expected Output: [[3, 2], [1]]
print(mySLL.head.maxsize) # Expected Output: 2
print(mySLL.head.value.value)  # Expected Output: 3

# Append another value
mySLL.append(value=4)
print(mySLL.get_size()) # Expected Output: (3, 4)
print(mySLL.to_list()) # Expected Output: [[4], [3, 2], [1]]
print(mySLL.head.maxsize)  # Expected Output: 4

# Pop a value
popval = mySLL.pop()
print(popval) # Expected Output: 4
print(mySLL.get_size()) # Expected Output: (2, 3)
print(mySLL.to_list()) # Expected Output: [[3, 2], [1]]
print(mySLL.head.maxsize) # Expected Output: 2
"""
