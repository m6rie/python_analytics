class Book:

    def __init__(self, title):
        self.title = title


class Newspaper:

    def __init__(self, title):
        self.title = title


# Create some instances of the classes
b1 = Book("Twilight")
b2 = Book("War and Peace")
n1 = Newspaper("New York Times")
n2 = Newspaper("Courrier International")

# TODO: use type() to inspect the object type
print(type(b1))
print(type(n1))

# TODO: compare two types together
print(type(b1) == type(b2))
print(type(n1) == type(b2))

# TODO: use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(b1, Newspaper))
print(isinstance(b1, object))
