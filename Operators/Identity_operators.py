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

# In the first example, a and b reference the same list object, so a is b evaluates to True. In the second example, a and b are two different list objects with the same content, so a is not b evaluates to True