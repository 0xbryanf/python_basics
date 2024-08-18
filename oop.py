# Object-Oriented Programming (OOP) is a programming paradigm that revolves around organizing code into objects 
# and classes that contain data and functions.

# Classes
# In OOP, a class is a blueprint or template that defines the characteristics and behaviors of an object. 
# A class typically contains:

# 1. Attributes : Data members that describe the object's properties (e.g., name, age).
# 2. Methods : Functions that operate on the object's attributes (e.g., calculate age).

# Think of a class as a cookie cutter shape. Just like how you can use a cookie cutter to create multiple identical cookies, a class is used to create multiple objects with similar characteristics.

# Objects

# An object , also known as an instance , is a unique entity that represents a real-world thing or concept. 
# Objects are created from classes and have their own set of attributes and methods.

# In Python, you can create an object by calling the `__init__` method of its class. 
# This method initializes the object's attributes with default values.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello, my name is {self.name} and I'm {self.age} years old.")
        
if __name__ == "__main__":
    john = Person("Bryan", 35)
    john.greet()