# 4. Compare Integer and String Representing Integer
# Write a function `compare_int_and_str(num1, num2)` that takes an integer `num1` and a string `num2`.

# ### Requirements
# *   If `num1` is not an integer, print
# `Error: The first parameter should be an integer.`
# *   If `num2` is not a string or cannot be converted to an integer, print
# `Error: The second parameter should be a string that can be converted to an integer.`
#   - **Hint:** Use `try` and `except` to handle the conversion.
#   ``` Python
#           try:
#               # Attempt to convert num2 to an integer
#               do something
#           except ValueError:  # If an error occurs in the try block
#               # Print an error message
#               print("...")
#   ```
# *   If the integer value of `num2` is equal to `num1`, print `{num1} and {num2} represent the same value.`
# *   Otherwise, print `{num1} and {num2} do not represent the same value.`
# *   Ensure that the function produces the expected output for the given test cases.

# 4. def compare_int_and_str(num1, num2):
    # Write your code here

def compare_int_and_str(num1, num2) :
  if not isinstance(num1, int) :
    print('Eror: The first parameter should be an integer.')
    return # return이 없으면 계속 실행됨
  if not isinstance(num2, str) :
    print('Error: The second parameter should be a string.')
    return
  try :
    num2 = int(num2)
  except ValueError :
    print('Error: The second parameter should be a string that can be converted to an integer.')
    return
  
# 오류 상황이 발생한 경우를 제외하고 num2 = int(num2)
  if num2 == num1 :
    print(f'{num1} and {num2} represent the same value')
  else :
    print(f'{num1} and {num2} do not represent the same value')
    # return없어도 상관없음음

# compare_int_and_str(10, "10")
# compare_int_and_str("10", "10")
compare_int_and_str(10, 'ten')