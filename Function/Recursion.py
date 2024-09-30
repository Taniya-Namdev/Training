# Recursion is a powerful programming technique where a function calls itself to solve smaller instances of the same problem. This approach can simplify complex problems by breaking them down into more manageable sub-problems. 

# Base Case :
# The condition under which the recursion stops. Without a base case, the function would call itself indefinitely, leading to a stack overflow.
def factorial(n):
    if n == 0:
        return 1  # Base case
    else:
        return n * factorial(n - 1)  # Recursive case
    
# Recursive Case:
# The part of the function where it calls itself with a smaller or simpler argument, moving towards the base case.

# Advantages of Recursion
# Simplifies Code: Makes the code more readable and easier to understand for problems that have a natural recursive structure.
# Reduces Complexity: Breaks down complex problems into simpler sub-problems.
# Disadvantages of Recursion
# Memory Usage: Each recursive call adds a new layer to the call stack, which can lead to high memory usage and stack overflow if the recursion is too deep.
# Performance: Recursive solutions can be less efficient than iterative ones due to the overhead of multiple function calls.
# When to Use Recursion
# Divide and Conquer Algorithms: Such as quicksort and mergesort.
# Tree and Graph Traversals: Such as depth-first search (DFS).
# Problems with a Natural Recursive Structure: Such as the Tower of Hanoi, factorial, and Fibonacci sequence.

print(factorial(5))