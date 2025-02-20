"""
Q4. String Permutations
Given a string `s`, create a function that returns a `list` of all permutations of the characters of the string with no duplicates
"""

def permutations(s):
    # Write your code
    if len(s) == 1:
        return set([s])

    result = []
    for i in range(len(s)):
        current_char = s[i]
        remaining = s[:i] + s[i+1:]
        for perm in permutations(remaining):
            result.append(current_char + perm)

    return set(result)