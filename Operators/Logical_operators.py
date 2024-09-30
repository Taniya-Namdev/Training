# LOgical Operators are used to combine conditional statements , allowing you to perform operations based on multiple conditions.
# logical AND(and) - gives True if both statements are true.
# Logical OR(or) - gives True if one of both statements is true.
# Logical NOT(not) - revert the result , gives False if Result is true

# These operators are essential for controlling the flow of program, especially in conditional statements and loops.

a = 5 
b = 3 
result1 = (a>0 and b>0)
result2 = (a>0 or b<0)
result3 = not(a>0 and b<0)
print(result1,result2,result3)