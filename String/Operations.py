# Few operations we already learn in file Basics.py
# Replacing: Replacing a part of the string with another string
str = "Hello World"
new_str = str.replace("World", "Python")  # "Hello Python"

# Splitting: Splitting a string into a list of substrings
str = "Hello World"
words = str.split(" ")  # ['Hello', 'World']

# Joining: Joining a list of strings into a single string
words = ['Hello', 'World']
str = " ".join(words)  # "Hello World"

# Advance String Operations 
# 1. Case Convesion : Changing the case of characters in a string
str = "Hello World"
lower_str = str.lower()  # "hello world"
upper_str = str.upper()  # "HELLO WORLD"

# 2. Trimming : Removing whitespace from the beginning and end of the string
str = "  abHello Worldba  "
trimmed_str = str.strip("  ab")  # "Hello World"
print(trimmed_str)

# 3. Checking Content: Checking if the string contains only certain types of characters.
str = "Hello123"
is_alpha = str.isalpha()  # False
is_digit = str.isdigit()  # False

# Formatting: Inserting variables into a string.
name = "Alice"
age = 30
formatted_str = f"My name is {name} and I am {age} years old."  # "My name is Alice and I am 30 years old."
