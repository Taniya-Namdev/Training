my_set = {"Apple","Banana","Cherry"}
# 1. add() - Adds an element to the set.
my_set.add("Orange")

# 2. remove() - Removes a specified element . Raise keyerror if the element is not found
my_set.remove('Banana')

# 3. discard() - Removes a specified element, Does not raise an error if the element is not found.
my_set.discard("Banana")

# 4. pop() - Removes and return an arbitrary element from the set. Raise keyerror if the set is empty
my_set = {"apple", "banana", "cherry"}
element = my_set.pop()
print(element)  # Output: 'apple' (or another element)
print(my_set)  # Output: {'banana', 'cherry'}

# 5. clear() - Removes all elements from the set
my_set = {"apple", "banana", "cherry"}
my_set.clear()
print(my_set)  # Output: set()

# 6. union() - Returns a new set with all elements from bot sets
set1 = {"apple", "banana"}
set2 = {"cherry", "date"}
set3 = set1.union(set2)
print(set3)  # Output: {'banana', 'apple', 'cherry', 'date'}

# 7. intersection() - Returns a new set with elements common to both sets
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date"}
set3 = set1.intersection(set2)
print(set3)  # Output: {'banana'}

# 8. difference() - Returns a new set with elements in the first set but not in second 
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date"}
set3 = set1.difference(set2)
print(set3)  # Output: {'apple', 'cherry'}

# 9. symmetric_difference() - Returns a new set with elements in either set but not in both
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date"}
set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {'apple', 'cherry', 'date'}

# 10. copy() - Returns a shallow copy of the set
my_set = {"apple", "banana", "cherry"}
new_set = my_set.copy()
print(new_set)  # Output: {'apple', 'banana', 'cherry'}

# 11. isdisjoint() - Returns True if two sets have no elements in common
set1 = {"apple", "banana"}
set2 = {"cherry", "date"}
print(set1.isdisjoint(set2))  # Output: True

# 12. issubset() - REturns TRue if all elements of the set are present in another set
set1 = {"apple", "banana"}
set2 = {"apple", "banana", "cherry"}
print(set1.issubset(set2))  # Output: True

# 13. issuperset() - REturns True if the set contains all elements of another set
set1 = {"apple", "banana", "cherry"}
set2 = {"apple", "banana"}
print(set1.issuperset(set2))  # Output: True

# 14. update() - Updates the set with elements from another set or iterable
set1 = {"apple", "banana"}
set2 = {"cherry", "date"}
set1.update(set2)
print(set1)  # Output: {'banana', 'apple', 'cherry', 'date'}

# 15. difference_update() - Removes the elements in this set that are also included in another , specified set
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date"}
set1.difference_update(set2)
print(set1)  # Output: {'apple', 'cherry'}

# 16.intersection_update() - Updates the set with the intersection of itself and another
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date"}
set1.intersection_update(set2)
print(set1)  # Output: {'banana'}

# 17.symmetric_difference_update() - Updates the set with symmetric difference of itself and another
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "date"}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {'apple', 'cherry', 'date'}
