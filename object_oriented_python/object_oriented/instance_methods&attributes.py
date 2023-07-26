# INSTANCE METHODS AND ATTRIBUTES


class Book:

    def __init__(self, title, author, pages, price):
        # those attributes are instance attributes because the value it holds is unique to each value it is declared on
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        # if you use a '__' before attr, method name, python will change the name
        #  so it cannot be used outside the class. Help to prevent override by subclasses
        self.__secret = "secret attribute"
        pass

    def getprice(self):
        if hasattr(
                self, "_discount"
        ):  # inbuilt method to test if a specific attribute is present
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        self._discount = amount  # the '_' means the attribute is internal to the class


b1 = Book("Twilight", "Mayer", 435, 17)
b2 = Book("War and Peace", "Tolstoi", 1432, 17.99)

# TODO: print the price of book1
print(b1.title, b1.getprice())

# TODO: try setting the discount
print(b1.getprice())
print(b1.setdiscount(0.25))
print(b1.getprice())
# print(b1.__secret) prints an AttributeError
print(b1._Book__secret)  # have to call the class to display to __ atribute
