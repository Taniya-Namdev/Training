# Dictionary comprehension in Python is a concise and readable way to create dictionaries from iterables. It allows you to generate a dictionary in a single line of code using a similar syntax to list comprehensions.

# Basic syntax : {key_expression :value_expression for item in iterable}

# Simple Copmrehension:
# Create a dictionary with numbers as keys and their squares as values.
squares = {x: x**2 for x in range(5)}
print(squares)  # Output: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Using a List to Create a Dictionary:
# Create a dictionary from a list of tuples.
pairs = [("name", "Alice"), ("age", 30)]
my_dict = {key: value for key, value in pairs}
print(my_dict)  # Output: {'name': 'Alice', 'age': 30}

# Conditional Dictionary Comprehension:
# Create a dictionary with only even numbers and their squares.
even_squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(even_squares)  # Output: {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}

# Nested Dictionary Comprehension:
# Create a nested dictionary.
nested_dict = {x: {y: x * y for y in range(1, 4)} for x in range(1, 4)}
print(nested_dict)
# Output: {1: {1: 1, 2: 2, 3: 3}, 2: {1: 2, 2: 4, 3: 6}, 3: {1: 3, 2: 6, 3: 9}}

## Practical Use Case:
# 1. Transforming Data:
students = [("Alice", 85), ("Bob", 90), ("Charlie", 78)]
student_dict = {name: score for name, score in students}
print(student_dict)  # Output: {'Alice': 85, 'Bob': 90, 'Charlie': 78}

# 2. Filtering Data - 
high_scores = {name: score for name, score in students if score > 80}
print(high_scores)  # Output: {'Alice': 85, 'Bob': 90}

# 3. Inverting a Dictionary:
original_dict = {'a': 1, 'b': 2, 'c': 3}
inverted_dict = {value: key for key, value in original_dict.items()}
print(inverted_dict)  # Output: {1: 'a', 2: 'b', 3: 'c'}

