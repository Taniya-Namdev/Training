# Conditional statements in Python allow you to execute specific blocks of code based on certain conditions. They are fundamental for controlling the flow of your program.

# if Statement: Executes a block of code if the condition is true

x = 10
if x > 5:
    print("x is greater than 5")
# Output: x is greater than 5

# if-else Statement: Executes one block of code if the condition is true, and another block if the condition is false

x = 3
if x > 5:
    print("x is greater than 5")
else:
    print("x is not greater than 5")
# Output: x is not greater than 5

# if-elif-else Statement: Checks multiple conditions, executing the corresponding block of code for the first true condition

x = 7
if x > 10:
    print("x is greater than 10")
elif x > 5:
    print("x is greater than 5 but less than or equal to 10")
else:
    print("x is 5 or less")
# Output: x is greater than 5 but less than or equal to 10

# Nested if Statements: An if statement inside another if statement

x = 10
if x > 5:
    if x < 15:
        print("x is between 5 and 15")
# Output: x is between 5 and 15
