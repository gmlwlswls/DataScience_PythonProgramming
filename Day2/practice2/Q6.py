# 6. Sum Values Until Threshold is Reached

# Write a function to sum values in a list until the sum reaches or exceeds a given threshold `K`.

# ### Requirements
# * Write a function `sum_until_threshold(lst, K)` that takes a list `lst` and a float `K`.
#     - The list `lst` contains integers, floats, and strings representing numbers.
#     - The function should convert all values to floats, if possible.
#     - If a value cannot be converted to a float, it should be ignored.
#     - If the sum of all valid values in the list is still less than `K`, the function should return `-1` and `None`.
#     - The function should return the sum of the values and the index if the threshold is reached or exceeded.
# * Ensure that the function produces the expected output for the given test cases.

# ### Constraints
# * The threshold `K` will be a positive float.
# * The function should not use any external libraries except for the built-in functions.


# if possible, should convert all values to floats
# if not possible, it should be ignored
# if sum < K, return -1 and None
# return the sum and the index if K is reached or exceeded

# K > 0, float

def sum_until_threshold(lst, K) :
  sum = 0
  for idx, element in enumerate(lst) :
    if isinstance(element, (int, float)) :
      element = float(element)
      sum += element
      if sum >= K : 
        return sum, idx
    elif isinstance(element, str) :
      try : 
        element = float(element)
        sum += element
      except :
        TypeError
      if sum >= K :
        return sum, idx
  if sum < K :
    return -1, None
    
print(sum_until_threshold([1, 2.5, '3', '4.5', 5, 'abc', 6], 10))
print(sum_until_threshold([1, '2', 3, 'abc', 4, 5.5], 15))
print(sum_until_threshold(['1.1', '2.2', 'abc', '3.3', '100.1.23'], 5))
print(sum_until_threshold([18.523, 32.1293, 22.123, '12.28321', 'abc'], 100))