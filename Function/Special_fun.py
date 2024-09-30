# Lambda Functions
# Lambda functions are small anonymous functions defined using the lambda keyword
add = lambda x, y: x + y
print(add(2, 3))  # Output: 5

# Docstrings
# You can add documentation to your functions using docstrings.
def multiply(a, b):
    """This function multiplies two numbers."""
    return a * b

print(multiply.__doc__)  # Output: This function multiplies two numbers.

# Example :
def calculate_area(radius, pi=3.14):
    """Calculate the area of a circle given its radius."""
    return pi * (radius ** 2)

def main():
    radii = [1, 2, 3, 4]
    for r in radii:
        area = calculate_area(r)
        print(f"Radius: {r}, Area: {area}")

if __name__ == "__main__":
    main()
