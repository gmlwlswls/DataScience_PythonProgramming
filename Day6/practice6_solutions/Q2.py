"""
Q2. Pascal's Triangle
Create a function for calculating a desired row of the Pascal’s triangle using Recursion
Pascal's Triangle: Each number lies between two numbers and below them, and its value is the sum of the two numbers above it.
"""

def Pascal_Recursion(n:int) -> list[int]:
    # Write your code
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        prev_list = Pascal_Recursion(n - 1)
        new_list = [prev_list[i] + prev_list[i + 1] for i in range(len(prev_list) - 1)]
        return [1] + new_list + [1]
    
"""
def Pascal_Recursion(n:int) -> list[int]:
    # Write your code
    if n == 0:
        return [1]
    answer = []
    answer.append(1)
    P = Pascal_Recursion(n - 1)
    for r in range(n - 1):
        answer.append(P[r] + P[r + 1])
    answer.append(1)

    return answer
"""

"""
Extra) Maybe use combination properties?
"""

def Pascal_Comb(n:int) -> list[int]:
    # Write your code
    res = [1] * (n + 1)
    for i in range(n - 1):
        res[i + 1] = int(res[i] * (n - i) / (i + 1))
    return res