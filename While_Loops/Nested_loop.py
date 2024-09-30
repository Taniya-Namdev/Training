# A nested while loop in Python is a while loop inside another while loop. This allows you to perform more complex iterations

i = 1
while i <= 3:  # Outer loop
    j = 1
    while j <= 3:  # Inner loop
        print(f"{i} * {j} = {i * j}")
        j += 1
    i += 1
    print()  # Print a new line for better readability


# Outer Loop: The outer loop runs from i = 1 to i = 3.
# Inner Loop: For each iteration of the outer loop, the inner loop runs from j = 1 to j = 3.
# Print Statement: During each iteration of the inner loop, the product of i and j is printed.
# Increment: Both i and j are incremented in their respective loops.