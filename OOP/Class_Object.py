# Class - A class is a blueprint for creatingnobjects . It defines a set of attributes and methods that the created object will have.

# Object - An object is an instance of a class is instantiated, it creates an object with the defined attributes and methods.

# Attributes - Variables that belong to a class or an instance 

# Method - Function defined within a class that describe the behaviors of an object.

# Step - by - step to create a class 
# 1. Define a class - Use class keyword followed bu=y class name
# 2. Initialize the class - Use the __init__ method to initialize the class attributes.
# 3. Define Methods - Add methods to define the behavior of the class

class Car:
    # Class attribute
    wheels = 4

    def __init__(self, make, model, year):
        # Instance attributes
        self.make = make
        self.model = model
        self.year = year

    # Instance method
    def description(self):
        return f"{self.year} {self.make} {self.model}"

    # Another instance method
    def start_engine(self):
        return f"The engine of the {self.model} is now running."

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2020)

# Accessing instance attributes
print(my_car.description())  # Output: 2020 Toyota Corolla

# Calling an instance method
print(my_car.start_engine())  # Output: The engine of the Corolla is now running.

# Accessing class attribute
print(Car.wheels)  # Output: 4
