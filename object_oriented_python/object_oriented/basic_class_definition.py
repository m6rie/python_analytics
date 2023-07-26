# OO Terms and Principles

# Class: A blueprint for creating objects of a particular type
# Methods: Regular functions that are part of a class
# Attributes: Variables that hold data that are part of a class
# Object: A specific instance of a class
# Inheritance: Means by which a class can inherit capabilities from another
# Composition: Means of building complex objects out of other objects


# BASIC CLASS DEFINITION
# Create a basic class
class Book:  #() after a class indicates that the class inherite from another class
    # the init function is one of Python special function for classes.
    # It is called before any othe function when a class is created to initialise it the new object with information
    def __init__(self, title):
        self.title = title
        pass  #this keyword can be used as a placeholder for future code


# Create instances of the class
b1 = Book("Twilight")
b2 = Book("War and Peace")

# Print the class and property
print(b1.title)
print(b2)
