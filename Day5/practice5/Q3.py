# # 3. String List Sorting with Insertion Sorting

# Write a function `sort_strings(lst)` to sort a list of strings based on the following criteria using the insertion sort algorithm:

# ### Requirements
# 1. Strings with shorter lengths should come first.
# 2. If strings have the same length, they should be sorted in lexicographical order.
# 3. Do not use built-in sorting functions; instead, implement the insertion sort algorithm.

# 3.

# insertion sort
# unsorted의 가장 왼쪽 값을
# sorted의 오른쪽값부터 비교

def sort_strings(lst) :
  # first : order by lengths in ascending order
  # second : same lengths > alphabetical
  # using insertion sort algorithm.
  for i in range(1, len(lst)) :
    for j in range(i-1, -1, -1) :
      if len(lst[j]) > len(lst[j+1]) :
        lst[j], lst[j+1] = lst[j+1], lst[j]
      elif len(lst[j]) == len(lst[j+1]) :
        if lst[j] > lst[j+1] :
          lst[j], lst[j+1] = lst[j+1], lst[j]
  return lst

print(sort_strings(['solve', 'this', 'problem', 'or', 'you', 'will', 'get', 'f']))     
print(sort_strings(['computing', 'class', 'is', 'so', 'funny', 'haha']))