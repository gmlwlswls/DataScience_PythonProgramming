"""
Q2. Reversing SLL

Implement functions `create_linked_list` and `print_linked_list` using the predefined `LinkedNode` class

- `create_linked_list` takes a Python list and returns the head of the created linked list
- `print_linked_list` takes the head of a linked list and prints the values in it
"""

### Define `LinkedNode` class for future usage, do not modify!
class LinkedNode():
    def __init__(self,x):
        self.val = x
        self.next = None


def create_linked_list(lst) :
    # Write your code
    if len(lst) == 0:
        return None
    start = LinkedNode(lst[0])
    current_node = start
    for i in range(1,len(lst)):
        node_new = LinkedNode(lst[i])
        current_node.next = node_new
        current_node = node_new
    return start

def print_linked_list(head):
    # Write your code
    lst = []
    while head is not None:
        lst.append(head.val)
        head = head.next
    print(lst, end = " ")

"""
Implement function `reverse_SLL` that takes in the head of a SLL and returns the head of a reversed SLL

※ Space complexity should be O(1)  
(Generating new linked lists or lists is not allowed)
"""

def reverse_SLL(head):
    # Write your code
    current = head
    prev = None
    while current != None:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev