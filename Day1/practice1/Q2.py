# 2. String Manipulation and Useful Methods
# Write functions to manipulate a given text using various string methods.

### Requirements
# *   Write a function `replace_word(text, old_word, new_word)` that takes a string `text`, a string `old`, and a string `new`. It returns a new string with all occurrences of `old` replaced by `new`.
#   - **Hint:** Use the `str.replace(old_word, new_word)` method.
# *   Write a function `to_uppercase(text)` that takes a string `text` and returns the string converted to uppercase.
#   - **Hint:** Use the `str.upper()` method.
# *   Write a function `remove_spaces(text)` that takes a string `text` and returns the string with all spaces removed.
#   - **Hint:** Use the `str.replace(old_word, new_word)` method.
# *   Write a function `is_numeric(text)` that takes a string `text` and returns `True` if the string is numeric, otherwise `False`.
#   - **Hint:**  Use the `str.isnum()` method.
# *   Write a function `contains_substring(main_string, sub_string)` that takes `main_string` text, and `sub_string` text and returns `True` if `sub_string` is found within `main_strin`g, otherwise return `False`.   
#   - **Hint:** Use the in operation.
# *   Ensure that the functions produce the expected output for the given test cases.
   

# 2-1. 
def replace_word(text, old_word, new_word):
    # Write your code here
  return text.replace(old_word, new_word)

text = "I love python programming"

print(replace_word(text, 'python', 'java'))


# 2-2.
def to_uppercase(text):
  return text.upper()

text= "hello"
print(to_uppercase(text))


# 2-3. remove_spaces(text)
# hint : str.replace(old_word, new_word)
def remove_spaces(text) :
  return text.replace(" ", "")

text= "hello world"
print(remove_spaces(text))

    
# 2-4. is_numeric(text)
# hint : str.isdigit()
def is_numeric(text) :
  return text.isdigit()

text= "12345"
print(is_numeric(text))
    

def contains_substring(main_string, sub_string) :
  return sub_string in main_string

main_string= "hello world"
sub_string= "world"
print(contains_substring(main_string, sub_string))
    