# Abstraction is a core concept in object-oriented programming (OOP) that focuses on hiding the complex implementation details and showing only the essential features of an object. It helps in reducing programming complexity and effort by allowing the programmer to focus on interactions at a higher level

# Key Points - 
# Simplification - Abstraction simplifies complex systems by breaking them down into more manageable parts.
# Hinding Details - It hides the internal implementation details an exposes only the neccessary parts.
# Interfaces - Abstraction is often achieved through the use of abstract classes or interfaces.

# abc MODULE - This provides the infrastructure for defining Abstract Base Classes(ABCs).
# ABCs are classes that cannot be instantiated on their own and designed to be inherited by other classes. They define a set of methods and properties that must be implemented by any subclass.

# Abstract class - A class that cannot be instantiated and often contains one or more abstract methods.
# Abstract methods - A method that is declared, but contains no implementation in the abstract class that can be inherited by subclasses.
# Concrete Method - A method with an implementation in abstract class that can be inherited by subclasses.

# Key Concept of abc Module-
# 1. ABCMeta - A metsclass for defining ABCs.
# ABC - A helper class that uses ABCMeta as its metaclass.
# @abstarctmethod - A decorator to declafre  abstract method. 
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("This animal is sleeping")

class Dog(Animal):
    def sound(self):
        print("Woof woof")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Creating instances of Dog and Cat
dog = Dog()
cat = Cat()

# Calling the abstract method
dog.sound()  # Output: Woof woof
cat.sound()  # Output: Meow

# Calling the concrete method
dog.sleep()  # Output: This animal is sleeping
cat.sleep()  # Output: This animal is sleeping
