def custom_sort(nums):
    """
    Sort a list of integers using custom rules:
    1. All even numbers appear before odd numbers.
    2. Even numbers are sorted in ascending order.
    3. Odd numbers are sorted in descending order.

    :param nums: A list of integers. (list[int])
    :return: A list of integers sorted based on the custom rules. (list[int])
    """
    odd_nums = []
    even_nums= []

    for num in nums :
        if num % 2 == 0 :
            even_nums.append(num)
        else :
            odd_nums.append(num)


    # for i in range(0, len(even_nums)) :
    # even_min_num = min(even_nums)
    # even_min_idx = even_nums.index(even_min_num)
    # even_nums[even_min_idx], even_nums[i] = even_nums[i], even_nums[even_min_idx]
    # for j in even_nums[i+1: ] :
    #     even_min_num = min(even_nums[i+1 :])
    #     even_min_idx = even_nums.index(even_min_num)
    #     if even_nums[j] > even_nums[even_min_idx] :
    #     even_nums[even_min_idx], even_nums[i] = even_nums[i], even_nums[even_min_idx]
    



"""
#### **Example**
# Example 1
nums = [5, 2, 9, 4, 7, 10, 3, 6]
print(custom_sort(nums))
# Expected Output: [2, 4, 6, 10, 9, 7, 5, 3]

# Example 2
nums = []
print(custom_sort(nums))
# Expected Output: []
"""