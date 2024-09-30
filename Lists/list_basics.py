#  A list is a versatile and powerful data structure that allows you to store an ordered collection of items. Lists are mutable, meaning you can change their content after they are created. 

# Creating a List 

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Creating a list of numbers
numbers = [1, 2, 3, 4, 5]
print(numbers)  # Output: [1, 2, 3, 4, 5]

# Creating a mixed list
mixed_list = [1, "apple", 3.14, True]
print(mixed_list)  # Output: [1, 'apple', 3.14, True]

# Accessing List Elements

fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana
print(fruits[-1]) # Output: cherry (negative index starts from the end)

# Modifying List Elements

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# Adding Elements to a List
# You can add elements to a list using methods like append(), insert(), and extend().

# Using append() to add an element at the end
fruits = ["apple", "banana"]
fruits.append("cherry")
print(fruits)  # Output: ['apple', 'banana', 'cherry']

# Using insert() to add an element at a specific position
fruits.insert(1, "blueberry")
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry']

# Using extend() to add multiple elements
fruits.extend(["date", "elderberry"])
print(fruits)  # Output: ['apple', 'blueberry', 'banana', 'cherry', 'date', 'elderberry']

# Removing Elements from a List
# You can remove elements using methods like remove(), pop(), and clear().

# Using remove() to remove a specific element
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")
print(fruits)  # Output: ['apple', 'cherry']

# Using pop() to remove an element by index
fruits.pop(1)
print(fruits)  # Output: ['apple']

# Using clear() to remove all elements
fruits.clear()
print(fruits)  # Output: []

# Common List Methods
# len(list): Returns the number of elements in the list.
# list.append(element): Adds an element to the end of the list.
# list.insert(index, element): Inserts an element at the specified position.
# list.remove(element): Removes the first occurrence of the element.
# list.pop(index): Removes and returns the element at the specified position.
# list.clear(): Removes all elements from the list.
# list.index(element): Returns the index of the first occurrence of the element.
# list.count(element): Returns the number of occurrences of the element.
# list.sort(): Sorts the list in ascending order.
# list.reverse(): Reverses the order of the list.

# List Comprehensions:

# Creating a list of squares
squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]
