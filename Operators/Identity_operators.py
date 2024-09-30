# These operators used to compare the memory location of two objects. They help determinewhether twovariables reference the same object in memory .
# is : Returns True if both variables point to the same object
a = [1,2,3]
b = a
result = (a is b)
print(result)

# is not : Return True if both variables do not point the same object
a =[1,2,3]
b =[1,2,3]
result2 = (a is not b)
print(result2)