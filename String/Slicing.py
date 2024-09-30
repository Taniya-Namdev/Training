# String slicing is a technique used to extract a portion of a string by specifying a range of indices. It’s a powerful feature in many programming languages, including Python.

# Basic Syntax :
# String[start:stop:step]

# Simple Slicing:
text = "Hello, World!"
slice1 = text[0:5]  # "Hello"
slice2 = text[7:12] # "World"

# Omitting Start or Stop:
text = "Hello, World!"
slice1 = text[:5]   # "Hello"
slice2 = text[7:]   # "World!"

# Using Negative Indices:
# Negative indices count from the end of the string.
text = "Hello, World!"
slice1 = text[-6:-1]  # "World"
slice2 = text[-6:]    # "World!"

# Specifying a Step:
# The step parameter allows you to skip characters
text = "Hello, World!"
slice1 = text[::2]  # "Hlo ol!"
slice2 = text[1::2] # "el,Wrd"

# Reversing a String:
# You can reverse a string by using a negative step
text = "Hello, World!"
reversed_text = text[::-1]  # "!dlroW ,olleH"
