# 3. Number Comparison

# Write functions to compare two numbers using if/else statements.

### Requirements
# *   Write a function `compare_numbers(num1, num2)` that takes two integers `num1` and `num2`.
#     - Print whether `num1` is equal to `num2`
#     - Print whether `num1` is greater than `num2`
#     - Print whether `num1` is less than `num2`
#     - If the inputs are not integers, print an error message: `Error: Both parameters should be integers.`
# *   Ensure that the functions produce the expected output for the given test cases.

# 3. isisntance 활용한 sol
def compare_numbers(num1, num2) :
  if not isinstance(num1, int) or not isinstance(num2, int) : # 둘 중에 하나 True(: int가 아닌게 True)라면면 출력
    print('Error : Both parameters should be integers.')
    return
  
  if num1 > num2 : 
    print(f'{num1} is greater than {num2}')
    
  elif num1 == num2 :
    print(f'{num1} is equal to {num2}')
    
  else :
    print(f'{num1} is less than {num2}')
    
compare_numbers(10, 5)
compare_numbers("10", 5) 