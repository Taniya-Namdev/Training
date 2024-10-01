# In Python , a set is an unordered collection of unique elements . Sets are mutable , meaning you can add or remove items creation, but the elemr=ents themselves must be immutable.
# Characristics of Sets:
# 1. Unordered : Set do not maintain any order . The elements can appear in a different order every time you use them
my_set = {"apple", "banana", "cherry"}
print(my_set)  # Output: {'banana', 'apple', 'cherry'} (order may vary)

# Unique Elements: Sets do not allow duplicate elements . If you try to add a duplicate, it will ignore
my_set = {"apple", "banana", "cherry", "apple"}
print(my_set)  # Output: {'banana', 'apple', 'cherry'}

# Mutable : You can add or remove elements from a set , but the elements themselves must be immutable
my_set = {"apple", "banana", "cherry"}
my_set.add("orange")
print(my_set)  # Output: {'banana', 'apple', 'cherry', 'orange'}

# CREATING SETS
# 1. Using Curly Braces:
my_set = {"apple", "banana", "cherry"}

# 2. Using se() constructor:
my_set = set(["apple", "banana", "cherry"])

