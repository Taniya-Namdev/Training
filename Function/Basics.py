# Functions in Python are blocks of reusable code that perform a specific task. They help in organizing code, making it more readable and maintainable

# Defining a Function:
# Define a function using the def keyword, followed by the function name and parentheses () which may include parameters
def my_function():
    print("Hello from a function")


# Calling a Function:
# To call a function, use the function name followed by parentheses.
my_function()  # Output: Hello from a function

# Function Parameters
# Functions can take parameters (arguments) to pass data into them.
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# Return Values
# Functions can return values using the return statement.
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8

# Default Parameters
# You can define default values for parameters.
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("Bob")    # Output: Hello, Bob!

# Arbitrary Arguments
# If you don’t know how many arguments will be passed to your function, use *args for a tuple of arguments, or **kwargs for a dictionary of keyword arguments.
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4)  # Output: 1 2 3 4

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30)  # Output: name: Alice age: 30

