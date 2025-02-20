"""
Q1. Power of Three

i) Create a function for checking a number if it is a power of 3 using recursion.
- ex1 - ```P1(27)```
> ```True```
- ex2 - ```P1(15631)```
> ```False```
- ex3 - ```P1(-1)```
> ```False```
"""
def P1_Recursion(n) -> bool:
    # Write your code
    if n == 1:
        return True
    elif n <= 0 or n % 3 != 0:
        return False
    return P1_Recursion(n / 3)

"""
ii) Create a function for checking a number if it is a power of 3 without using recursion.
"""

def P1_Loop(n) -> bool:
    # Write your code
    while (n % 3 == 0):
        n = n / 3
    return n == 1