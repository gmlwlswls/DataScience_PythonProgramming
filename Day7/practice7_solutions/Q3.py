"""
Q3. Palindrome SLL

Define function `isPalindrome` that takes the head of a SLL and returns whether it is a palindrome.

- return boolean
- [1,2,3,4] is not a palindrome so False is returned
- [1,2,3,2,1] is a palindrome so True is returned
- Try doing it without reversing the whole linked list!
"""
### Define `LinkedNode` class for future usage, do not modify!
class LinkedNode():
    def __init__(self,x):
        self.val = x
        self.next = None


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

def isPalindrome(head):
   # Write your code
    reverse = reverse_SLL(head)
    while head:
        if head != reverse:
            return False
        head = head.next
        reverse = reverse.next
    return True
"""

def isPalindrome(head):
    # Write your code
    reverse = None
    fast = slow = head
    while fast and fast.next:
        fast = fast.next.next
        reverse, reverse.next, slow  = slow, reverse, slow.next
    if fast:
        slow = slow.next
    while slow:
        if slow.val != reverse.val:
            return False
        else:
            slow = slow.next
            reverse = reverse.next
    return True