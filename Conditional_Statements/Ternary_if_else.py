# Ternary Conditional Operator: A shorthand way of writing an if-else statement
# Syntax : value_if_true if condition else value_if_false

a = 10
b = 20
min_value = a if a < b else b
print(min_value)  # Output: 10

# Nested Ternary Operator

a = 10
b = 20
c = 30
result = "a is the smallest" if a < b and a < c else ("b is the smallest" if b < c else "c is the smallest")
print(result)  # Output: a is the smallest
