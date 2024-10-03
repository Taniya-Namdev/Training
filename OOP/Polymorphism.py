# Polymorphism allows objects of different classes to be treated as objects of common superclass. It enables a single interface to represent different underlying forms , In Python polymorphism is achieved by method overriding and method overloading.

# Method Overriding - Allows a subclass to provide a specific implementation of a method that is already defined in superclass.
class Bird:
  def intro(self):
    print("There are many types of birds.")
    
  def flight(self):
    print("Most of the birds can fly but some cannot.")
  
class sparrow(Bird):
  def flight(self):
    print("Sparrows can fly.")
    
class ostrich(Bird):
  def flight(self):
    print("Ostriches cannot fly.")
    
obj_bird = Bird()
obj_spr = sparrow()
obj_ost = ostrich()

obj_bird.intro()
obj_bird.flight()

obj_spr.intro()
obj_spr.flight()

obj_ost.intro()
obj_ost.flight()

# Method Overloading - Allows multiple methods in the same class to hab=ve same name but different parameters. Python does not support method overloading directly but it can be achieved using default arguments or variable length arguments.
class Example:
    def add(self, *args):
        return sum(args)

# Creating an instance of Example
obj = Example()

# Calling the method with different numbers of arguments
print(obj.add(10))        # Output: 10
print(obj.add(10, 20))    # Output: 30
print(obj.add(10, 20, 30)) # Output: 60


# Using Multiple Dispatch (library)
from multipledispatch import dispatch

class Example:
    @dispatch(int, int)
    def add(self, a, b):
        return a + b

    @dispatch(int, int, int)
    def add(self, a, b, c):
        return a + b + c

# Creating an instance of Example
obj = Example()

# Calling the method with different numbers of arguments
print(obj.add(10, 20))    # Output: 30
print(obj.add(10, 20, 30)) # Output: 60