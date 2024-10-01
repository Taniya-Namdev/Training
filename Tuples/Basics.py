# Tuples in Python are a type of collection that allows you to store multiple items in a single variable. They are similar to lists but have some key differences.

# Characteristics of Tuples:
# 1. Ordered - Tuples maintain the order of elements. The first element has an index of 0, the second element has an index of 1, and so on.
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[0])  # Output: apple

# 2. Immutability : Once a tuple create , its element cannot be changed, added, or removed. This makes tuple useful for storing data that should not be modified.
my_tuple = ("apple", "banana", "cherry")
# my_tuple[1] = "blueberry"  # This will raise a TypeError

# 3. Allow Duplicates : Tuples can contain duplicates
my_tuple = ("apple", "banana", "cherry", "apple")
print(my_tuple)  # Output: ('apple', 'banana', 'cherry', 'apple')

# CREATION Of TUPLES
# 1. Using parantheses
my_tuple = ("apple", "banana", "cherry")

# 2. Using tuple() Constructor
my_tuple = tuple(("apple", "banana", "cherry"))

# 3. Single Element Tuple - To create a single element tuple , we need to add a comma after the item
single_element_tuple = ("apple",)
print(type(single_element_tuple))  # Output: <class 'tuple'>

# ACCESSING TUPLE ELEMENTS
# 1. Index 
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[1])  # Output: banana

# 2. Negative index
my_tuple = ("apple", "banana", "cherry")
print(my_tuple[-1])  # Output: cherry

# 3. Slicing 
my_tuple = ("apple", "banana", "cherry", "date")
print(my_tuple[1:3])  # Output: ('banana', 'cherry')
