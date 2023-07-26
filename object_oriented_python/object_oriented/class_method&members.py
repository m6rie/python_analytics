class Book:
    # Properties defined at the class level are shared by all instances
    # it is good practice to write them in all caps
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")
    __booklist = None

    # class method only work on a class instance, not an object instance
    # class method decorator should be used when creating a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []
        return Book.__booklist

    def __init__(self, title, booktype):
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            print(f"{booktype} is not a valid booktype")
        else:
            self.booktype = booktype

    def setTitle(self, newtitle):
        self.title = newtitle


class Newspaper:

    def __init__(self, title):
        self.title = title


# TODO: Create some book instances
b1 = Book("Twilight", "PAPERBACK")
b2 = Book("War and Peace", "HARDCOVER")

# TODO: access the class attribute
print("Book types: ", Book.getbooktypes())

thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
