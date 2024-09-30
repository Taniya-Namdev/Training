# A for loop is a control flow statement that allows you to execute a block of code repeatedly based on a specified condition. It’s commonly used when you know in advance how many times you want to execute a statement or a block of statements.

# Range In For Loops - The range() function is commonly used in for loops in Python to generate a sequence of numbers. This function is very versatile and can be used in several ways to control the iterations of the loop.

# range(start,stop,step)

for i in range(5):
    print(i)

# Specifying Start and Stop:
for i in range(2, 6):
    print(i)

# Specifying Step:
for i in range(1, 10, 2):
    print(i)

# Iterating Over a List with Indices
fruits = ["apple", "banana", "cherry"]
for i in range(len(fruits)):
    print(f"Index {i}: {fruits[i]}")
