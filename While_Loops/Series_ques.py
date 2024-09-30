# 1. Print a Series of Numbers

i = 1
while i <= 10:
    print(i)
    i += 1

# 2. Print Even Numbers from 1 to 20

i = 1
while i <= 20:
    if i % 2 == 0:
        print(i)
    i += 1

# 3. Sum of First N Natural Numbers

N = 10
i = 1
sum = 0
while i <= N:
    sum += i
    i += 1
print("Sum of first", N, "natural numbers is:", sum)

# 4. Fibonacci Series

N = 10
a, b = 0, 1
count = 0
while count < N:
    print(a)
    a, b = b, a + b
    count += 1

# 5. Factorial of a Number

num = 5
factorial = 1
i = 1
while i <= num:
    factorial *= i
    i += 1
print("Factorial of", num, "is:", factorial)

# 6. Print Multiplication Table

num = 5
i = 1
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1

# 7. Reverse a Number

num = 12345
reversed_num = 0 
while num > 0 :
    digit = num % 10 
    reversed_num = reversed_num * 10 + digit
    num//=10
print("Reversed number is :", reversed_num)