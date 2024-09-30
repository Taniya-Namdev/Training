# Implicit Conversion - Automatically handled by python to prevent data loss.
x = 10
y = 3.14
result = x+y
print(result, type(result))

# output is 13.14 <class 'float'>

# Explicit Conversion 
# int() , float() , str() , list(), tuple(), set()

num_str = "123"
num_int = int(num_str)
print(num_int,type(num_int))

# output will be 123 <class 'int'>

# Handlings Errors -
num_str = "123abc"
try:
    num_int = int(num_str)
except ValueError:
    print("Can't convert to integer.")