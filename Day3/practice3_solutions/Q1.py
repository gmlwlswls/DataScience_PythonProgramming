"""
Q1. Find duplicates

[KOR] 정수(int)로만 구성된 리스트를 변수(argument)로 받고, 그 중 두 번 이상 반복되는 정수의 집합(set)을 리턴하는 함수를 작성하시오.

[ENG] Take a list of integers as input argument, and return a set of numbers that appear two or more times.

ex1 - P1([1, 2, 3, 1])
> {1}

ex2 - P1([1, 1, 2, 3, 3, 3])
> {1,3}

ex3 - P1([1, 2, 3, 4, 5])
> set()
"""

def P1(lst: list) -> set:
    ### Write code here ###
    seen = set()
    duplicates = set()
    
    for i in lst:
        if i not in seen:  
            seen.add(i)
        else: duplicates.add(i)
    return duplicates
    ### End of your code ###