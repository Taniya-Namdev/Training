# Python provides several built-in methods for dictionaries that allow for efficient manipulation, access, and transformation of dictionary data.

# Common Dictionary Methods:
# 1. clear() - Removes all items from the dictionary.
my_dict = {"name": "Alice", "age": 30}
my_dict.clear()
print(my_dict)  # Output: {}

# 2. copy() - Returns a shallow copy of the dictionary
my_dict = {"name": "Alice", "age": 30}
new_dict = my_dict.copy()
print(new_dict)  # Output: {'name': 'Alice', 'age': 30}

# 3. fromkeys() - Creates a new dictionary with keys from an iterable and values set to a specified value.
keys = ["name", "age"]
new_dict = dict.fromkeys(keys, "unknown")
print(new_dict)  # Output: {'name': 'unknown', 'age': 'unknown'}

# 4. get() - Returns value for a specified key , if the key does not exist , it returns a default value.
my_dict = {"name": "Alice", "age": 30}
print(my_dict.get("name"))  # Output: Alice
print(my_dict.get("gender", "Not specified"))  # Output: Not specified

# 5. items() - Returns a view object containing the dictionary's key - value pairs as tuples.
my_dict = {"name": "Alice", "age": 30}
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 30)])

# 6. keys() - Return a view object containing the dictionary's keys.
my_dict = {"name": "Alice", "age": 30}
print(my_dict.keys())  # Output: dict_keys(['name', 'age'])

# 7. pop():
# Removes the specified key and returns the corresponding value. If the key is not found, it raises a KeyError.
my_dict = {"name": "Alice", "age": 30}
age = my_dict.pop("age")
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'Alice'}

# 8. popitem():
# Removes and returns the last inserted key-value pair as a tuple.
my_dict = {"name": "Alice", "age": 30}
item = my_dict.popitem()
print(item)  # Output: ('age', 30)
print(my_dict)  # Output: {'name': 'Alice'}

# 9. setdefault():
# Returns the value of a specified key. If the key does not exist, it inserts the key with a specified value.
my_dict = {"name": "Alice"}
age = my_dict.setdefault("age", 30)
print(age)  # Output: 30
print(my_dict)  # Output: {'name': 'Alice', 'age': 30}

# 10. update():
# Updates the dictionary with elements from another dictionary or an iterable of key-value pairs.
my_dict = {"name": "Alice"}
my_dict.update({"age": 30, "city": "New York"})
print(my_dict)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}

# 11. values():
# Returns a view object containing the dictionary’s values.
my_dict = {"name": "Alice", "age": 30}
print(my_dict.values())  # Output: dict_values(['Alice', 30])
