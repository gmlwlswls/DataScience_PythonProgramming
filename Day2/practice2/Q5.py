# 5. Toggle Case of Each Character in a String
# Write a function `toggle_case(text)` that takes a string `text` and returns a new string with each uppercase letter converted to lowercase and each lowercase letter converted to uppercase.

# ### Requirements
# *   Use a `for` loop to iterate through each character in the string.
# *   If a character is uppercase, convert it to lowercase.
# *   If a character is lowercase, convert it to uppercase.
# *   Leave non-alphabetic characters unchanged.
# *   Ensure that the function produces the expected output for the given test cases.



def toggle_case(text) :
  new_text = ''
  for str in text :
    if str.isupper() :
      # new_text = new_text.join(str.lower())
      new_text = new_text + str.lower()
    elif str.islower() :
      # new_text = new_text.join(str.upper())
      new_text = new_text + str.upper()
    else :
      new_text = new_text + str
  return new_text

toggle_case('Hello World')
toggle_case('Python3.8')

