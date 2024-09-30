# A while loop in Python allows you to repeatedly execute a block of code as long as a specified condition is true. 

 # while condition:
    # code block to be executed
  
i = 1
while i <= 5:
    print(i)
    i += 1

# Condition: The loop checks the condition before each iteration. If the condition is True, the code block inside the loop is executed. If the condition is False, the loop stops

# Infinite Loop: If the condition never becomes False, the loop will run indefinitely

# Break Statement : The break statement use to exit the loop prematurely.

i = 1
while i <= 5:
    if i == 3:
        break
    print(i)
    i += 1
# Output: 1 2

# Continue Statement : The continue statement skips the rest of the code inside the loop for the current iteration and moves to the next iteration.

i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
# Output: 1 2 4 5

# Else Clause : The else clause can be used with a while loop. It runs a block of code once when the condition becomes False.

i = 1
while i <= 5:
    print(i)
    i += 1
else:
    print("Loop is done")
# Output: 1 2 3 4 5
#         Loop is done

# The while loop is very powerful and can be used in various scenarios where you need to repeat an action until a certain condition is met