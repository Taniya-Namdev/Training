# the concept of scope determines the visibility and lifetime of variables. Understanding scope is crucial for writing clean and bug-free code. 

# Types of Scope
# 1. Local Scope: Variables defined inside a function are in the local scope of that function. They can only be accessed within that function
def my_function():
    x = 10  # Local variable
    print(x)

my_function()  # Output: 10
# print(x)  # Error: NameError: name 'x' is not defined

# 2.Global Scope: Variables defined outside any function are in the global scope. They can be accessed from anywhere in the code.
x = 10  # Global variable

def my_function():
    print(x)

my_function()  # Output: 10
print(x)  # Output: 10

# 3. Enclosing Scope: This refers to the scope of a nested function. Variables in the enclosing (outer) function can be accessed by the nested (inner) function.
def outer_function():
    x = 10  # Enclosing variable

    def inner_function():
        print(x)

    inner_function()

outer_function()  # Output: 10

# 4. Built-in Scope: This is the scope of built-in names in Python. These are available in all scopes.
print(len("Hello"))  # Output: 5


# The LEGB Rule
# Python resolves variable names using the LEGB rule, which stands for:

# Local: Names assigned within a function.
# Enclosing: Names in the local scope of any enclosing functions.
# Global: Names assigned at the top-level of a module or declared global within a function.
# Built-in: Names preassigned in the built-in names module.

# Modifying Scope
# Global Keyword: Use the global keyword to modify a global variable inside a function.
x = 10

def my_function():
    global x
    x = 20

my_function()
print(x)  # Output: 20

# Nonlocal Keyword: Use the nonlocal keyword to modify a variable in the enclosing scope
def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 20

    inner_function()
    print(x)

outer_function()  # Output: 20

# Advantages of Scoping :
# 1. Avoiding Name Collisions - Using local variables helps avoid unintended modifications to global variables.
x = 10

def my_function():
    x = 20  # Local variable
    print(x)

my_function()  # Output: 20
print(x)  # Output: 10

# 2. Closures - Functions can capture and carry some of the enclosing scope with them.
def outer_function(x):
    def inner_function(y):
        return x + y
    return inner_function

add_five = outer_function(5)
print(add_five(10))  # Output: 15
