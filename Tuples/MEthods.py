# Tuples in python have two built in methods that you can use for Tuples
# 1. count() - The count() method returns the number of times specific value appear in the tuple.
# syntax - tuple.count(value)
my_tuple = (1, 2, 3, 2, 2, 4, 5)
count_of_twos = my_tuple.count(2)
print(count_of_twos)  # Output: 3

# 2. index() - The inde() method searches the tuple for a specific value and retun the position of where it was found. If the value doesn't found , it raise a valueerror
# syntax - tuple.index(value, start, end)
my_tuple = (1, 2, 3, 2, 4, 5)
index_of_two = my_tuple.index(2)
print(index_of_two)  # Output: 1

# Searching for the next occurrence of 2 starting from index 2
index_of_two_again = my_tuple.index(2, 2)
print(index_of_two_again)  # Output: 3
