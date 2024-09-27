# The input() function is used to get input from user .
# By default return type of input function is string.

name = input("Enter your age:")
print(type(name))
# output is <class 'str'>

# we can convert the type by using int(),float()
age = int(input("Enter your age:"))
print(age, type(age))

#handling multiple inputs
Data = input("Enter your Name and Age separated by comma:").split(",")
Name = Data[0]
Age = int(Data[1])
print(f"Name:{Name},Age:{Age}")

#Example with Error Handling

try:
    roll_no = int(input("Enter your age:"))
    print(f"You are {roll_no} in this class")
except ValueError:
    print("Please enter a valid number.")