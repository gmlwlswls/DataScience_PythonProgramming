# # 2. Intermediate Steps of Selection Sort
# Write function `print_selection` that prints list immediate result at Kth iteration during selection sort.

# If `K` is larger than length of list, function prints -1
   
# 2.

# selection sort : 정렬된 오른쪽 리스트에서 가장 작은 값을 
# 왼쪽의 리스트의 마지막값과 비교해서 swap하여 정렬 

# selection sort
# [0:] min
# lst[0] = min > lst[1:] min > swap

def print_selection(arr, K) :
  if len(arr) < K :
    print(-1)
  else :
    # print the list arr at the kth iteration during selection sort.
    # if K > len(lst), prints -1
      for i in range(K) :
        min_value = min(arr[i:])
        min_value_idx = arr.index(min_value)
        if arr[i] > arr[min_value_idx] :
          arr[i], arr[min_value_idx] = arr[min_value_idx], arr[i]
      print(f'{K}th iteration {arr}')


print_selection([7,5,9,1,3], 0)
print_selection([7,5,9,1,3], 1)
print_selection([7,5,9,1,3], 2)
print_selection([7,5,9,1,3], 3)
print_selection([7,5,9,1,3], 4)
print_selection([7,5,9,1,3], 5)
print_selection([7,5,9,1,3], 6)
