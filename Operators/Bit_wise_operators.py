# These operators allowed to perform operations on binary representation of integers
# Bitwise AND (&)
# Bitwise OR (|)
# Bitwise XOR (^)
# Bitwise NOT (~)
# Bitwise Left Shift (<<)
# bitwise right shift (>>)

a = 5 # 0101 in binary 
b = 3 # 0011 in binary 
result1 = a & b # output 1 - 0001 in binary
result2 = a|b # output 7 - 0111 in binary
result3 = a^b # output 6 - 0110 in binary 
result4 = ~a # output -6 (invert to 1010 in binary , which is -6 in two's complement)
result5 = a << 1 # output  10 - 1010 in binary
result6 = b >> 1 # output 1 - 0001 in binary
print(result1,result2,result3,result4,result5,result6)