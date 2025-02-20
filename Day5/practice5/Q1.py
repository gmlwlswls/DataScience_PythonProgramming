# 1. Find Insert Position in Sorted Array

# Given a sorted array of distinct integers and a target value, write a function `searchInsert(nums, target)` that returns the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

# ### Requirements
# *   `nums` contains distinct values sorted in ascending order.
# *   *** The search algorithm must have O(log n) runtime complexity. ***


def searchinsert(nums, target) :
  # returns the index if the target is found.
  for i in range(len(nums)) :
    if nums[i] == target :
      return i
    elif nums[i-1] < target and nums[i] > target :
      return i
    
searchinsert([1,3,5,6], 5)
searchinsert([1,3,5,6], 2)