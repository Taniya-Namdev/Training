# 1. Right Triangle Star Pattern
n = 5 
i = 1
while i <= n :
    j = 1
    while j <=i:
        print("*", end = " ")
        j+=1
    print()
    i+=1

# 2. Inverted Right Triangle Star Pattern
n = 5 
i = n 
while i>0:
    j=1 
    while j <= i:
        print("*", end=" ")
        j+=1
    print()
    i-=1

# 3. Pyramid Star Pattern
n= 5
i = 1
while i<=n:
    # print spaces
    j = n-i
    while j>0:
        print(" ", end=" ")
        j-=1

    # print stars
    k = 1 
    while k<=(2*i -1):
        print("*",end=" ")
        k+=1
    print()
    i+=1

# 4. Diamond Star Pattern
n= 5
i = 1
while i<=n:
    # print spaces
    j = n-i
    while j>0:
        print(" ", end=" ")
        j-=1

    # print stars
    k = 1 
    while k<=(2*i -1):
        print("*",end=" ")
        k+=1
    print()
    i+=1

i = n-1
while i > 0:
    j=n-i 
    while j >0:
        print(" ", end =" ")
        j-=1
    k=1
    while k<=(2*i-1):
        print("*",end = " ")
        k+=1
    print()
    i-=1