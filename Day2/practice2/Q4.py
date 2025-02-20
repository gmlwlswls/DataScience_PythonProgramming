# 4. Nested List

# Make a function `P4` that receives a nested list as an input and returns a list that satisfies the conditions below.

# **Conditions**
# - The input list is looks like [[word, length]]
# - Words consist only of lower case letters
# - Collect words from the input list and return as a list
# - The list must be alphabetically ordered


def P4(lst) :
  word_list = []
  for element in lst :
    word_list.append(element[0])
  return sorted(word_list)

P4([['apple', 5], ['banana', 6]])
P4([['cup', 3], ['ace', 3], ['nice', 4], ['good', 4]])