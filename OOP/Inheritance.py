# Ineritance is fundamental concept in oop that allows a class to inherit attributes and methods from another class. This promotes code reuse and establishes a natural hierarchy between classes.

# Types of Inheritance : 
# Single Inheritance - A child class inherit from one parent class .
# Multiple Inheritance - A child class inherits from more than one parent class.
# Multilevel Inheritance - A class is derived from another derived class.
# Hierarchical Inheritance - Multiple Classes inherit from a single parent class.
# Hybrid Inheritance - A combination of two or more types of inheritance.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)
        self.employee_id = employee_id

    def display_employee(self):
        self.display()
        print(f"Employee ID: {self.employee_id}")

# Creating an instance of Employee
emp = Employee("John Doe", 30, "E12345")
emp.display_employee()

# Syntax - 
# Inheritance syntax - The child class defined by passing parent class as a parameter.
# super() Function - Used to call the parent class's __init__ method to initialize inherited attributes.
# Method Overriding - The child classs can override methods of the parent classs to provide specific implementations.

 