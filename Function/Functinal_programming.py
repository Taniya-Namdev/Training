# Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing state and mutable data. It emphasizes the use of functions as first-class citizens, meaning functions can be passed as arguments to other functions, returned as values from other functions, and assigned to variables.

# 1. Pure Function:  Functions that always produce the same output for the same input and have no side effects (i.e., they don’t modify any state or data outside the function).
def add(a, b):
    return a + b

# 2. First-Class Function:  Functions that can be treated like any other variable. They can be passed as arguments, returned from other functions, and assigned to variables.
def greet(name):
    return f"Hello, {name}!"

def call_function(func, value):
    return func(value)

print(call_function(greet, "Alice"))  # Output: Hello, Alice!

# 3. Higher-Order Functions: Functions that take other functions as arguments or return them as results.
def apply_twice(func, value):
    return func(func(value))

def increment(x):
    return x + 1

print(apply_twice(increment, 3))  # Output: 5

# 4. Immutability: Data is immutable, meaning it cannot be changed once created. Instead of modifying data, new data structures are created.
original_list = [1, 2, 3]
new_list = original_list + [4]
print(original_list)  # Output: [1, 2, 3]
print(new_list)       # Output: [1, 2, 3, 4]
