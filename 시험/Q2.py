"""
2. Count and Group Integers (7.pt)

Implement `count_and_group(lst)` function that counts the occurrences of integers in a list and groups them based on their counts.
"""
def count_and_group(lst) : 
  # counts of occurences of int
  # lists of int that appears many times (sorted ascending)
  lst.sort()
  seen = []
  duplicates= set()
  final_dict= {}

  for i in lst :
    if i in seen :
      duplicates.add(i)
    else :
      seen.append(i)

  for duplicate in duplicates :
    if duplicate in seen :   
      seen.remove(duplicate)

  final_dict[1] = seen
  duplicates = list(duplicates)
  for duplicate in duplicates :
    final_dict[lst.count(duplicate)] = [duplicate]

  return final_dict


lst = [1,2,2,3,3,3,4,5]
print(count_and_group(lst))

lst= [-1,0,1,2,3,100] 
print(count_and_group(lst))
    
"""
#### **Example**
# Example 1
lst = [1, 2, 2, 3, 3, 3, 4, 5]
print(count_and_group(lst))
# Expected Output: {1: [1, 4, 5], 2: [2], 3: [3]}

# Example 2
lst = [-1, 0, 1, 2, 3, 100]
print(count_and_group(lst))
# Expected Output: {1: [-1, 0, 1, 2, 3, 100]}
"""