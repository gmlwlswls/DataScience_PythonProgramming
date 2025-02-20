# 2. Finding Sum of Positive Integers in list
# Make a function `P2` that takes a list consisting of only integers as input, adds only the positive integers among the elements of the list, and returns the sum.

# **Conditions**

# - The input list consists only of integers.

# - Return 0 if there are no positive integers in the list.

# Ex 1) `P2([1, 2, -3])`
# > 3


# Ex 2) `P2([-1, 0])`

# > 0
   


def P2(lst) : 
  pos_sum = 0
  for num in lst :
    if num > 0 :
      pos_sum += num
  return pos_sum

P2([1,2,-3])
P2([-1, 0])
    

