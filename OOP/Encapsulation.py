# Encapsulation is fundamental concept of oop that involves bundling data and methods that operate on the data into a single unit, typically a class . This helps in restricting direct access to some of an object's components, which can prevent the accidential modification.

# Key Concept -
# 1. Public Members - Accessible from anywhere outside the class.
# 2. Protected Members - Accessible within the class and its subclasses. In python , these are indicated by a single underscore prefix(eg - _protected)
# 3. Private Members - Accessible only within the class . In [python , these are indicated by a double underscore prefix (eg - __private)
 
class Employee:
    def __init__(self, name, salary):
        self.name = name  # Public attribute
        self._salary = salary  # Protected attribute
        self.__bonus = 0  # Private attribute

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_bonus(self):
        return self.__bonus

    def display_info(self):
        return f"Name: {self.name}, Salary: {self._salary}, Bonus: {self.__bonus}"

# Creating an instance of Employee
emp = Employee("John Doe", 50000)

# Accessing public attribute
print(emp.name)  # Output: John Doe

# Accessing protected attribute (not recommended)
print(emp._salary)  # Output: 50000

# Accessing private attribute directly (will raise an AttributeError)
# print(emp.__bonus)  # Uncommenting this line will raise an error

# Using getter and setter methods to access private attribute
emp.set_bonus(5000)
print(emp.get_bonus())  # Output: 5000

# Displaying employee information
print(emp.display_info())  # Output: Name: John Doe, Salary: 50000, Bonus: 5000

# What is Self ?
# In python self is a reference to instance of the class. It is used to access variables and methods associated with the current object .

# Instance Reference - self efers to the instance of the class. It allows you to access instance attributes and methods from within the class.
# First Parameter - In instance methods, self is always the frist parameter . Although you canname it anything , self is the convention.
# self is Not a Keyword but a strong convention.

# What is init in python ?
# The __init__ method in pyhton is a special method called a constructor. It is automatically invoked when a new instance of a class is created. The primary purpose of __init__ is to initialize the instance's attributes with the values provided during the creation of the object.