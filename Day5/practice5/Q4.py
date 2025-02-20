# # 4. String to Number Conversion

# Consider a converter that replaces some digits of a number with their English word equivalents, as shown in the following examples:
# - 1234 → “one23four”
# - 98765 → “9eight7six5”
# - 423 → “fourtwo3”

# Write a function `stringToNumberConverter(s)` that takes a string `s` containing numbers and/or their English word equivalents and converts it back to an integer.
# ***You must not use string methods.***
# Use ASCII codes to distinguish between numeric characters (e.g., '1') and alphabetic characters (e.g., 'a').

# | Digit | English Word |
# | ----- | ------------- |
# | 0     | zero          |
# | 1     | one           |
# | 2     | two           |
# | 3     | three         |
# | 4     | four          |
# | 5     | five          |
# | 6     | six           |
# | 7     | seven         |
# | 8     | eight         |
# | 9     | nine          |

# ### Requirements
# 1. The length of the input string `s` is between 1 and 50.
# 2. The input string `s` does not start with "zero" or "0".
# 3. Assume all inputs are valid.
# 4. Do not use string methods (e.g., replace, find, index).


def convertStringToNumber(s):
    # Write your code here

    return