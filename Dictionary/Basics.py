# A a dictionary is a collection of key-value pairs. It is an unordered, mutable, and indexed data structure that allows you to store and retrieve data efficiently.
# Creating a Dictionary: a) using {} or b) dict()
# Using curly braces
my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

# Using the dict() function
my_dict = dict(name="Alice", age=30, city="New York")

# Accessing Values:
print(my_dict["name"])  # Output: Alice
print(my_dict.get("age"))  # Output: 30

# Adding and Updating Values :
my_dict["email"] = "alice@example.com"  # Adding a new key-value pair
my_dict["age"] = 31  # Updating an existing key-value pair

# Removing Key-Value Pairs: remove key-value pairs using the del statement or the pop() method.
del my_dict["city"]  # Removes the key "city"
email = my_dict.pop("email")  # Removes the key "email" and returns its value

# Iterating Over a Dictionary:
# Iterating over keys
for key in my_dict:
    print(key)

# Iterating over values
for value in my_dict.values():
    print(value)

# Iterating over key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")
