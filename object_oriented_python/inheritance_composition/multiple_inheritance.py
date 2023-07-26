class A:

    def __init__(self):
        super().__init__()
        self.foo = "foo"
        self.name = "Class A"


class B:

    def __init__(self):
        super().__init__()
        self.bar = "bar"
        self.name = "Class B"


class C(A, B):  # it is inheriting from both class A and class B

    def __init__(self):
        super().__init__()

    def showproperty(self):
        print(self.foo)
        print(self.bar)
        print(self.name)


c = C()
c.showproperty()
print(
    c.name
)  # prints 'Class A'. The method resolution order looks at the parent clas in the order
# in which they were defined to assign the value

# to inspect the method resolution orde, call the mro attribute
print(C.__mro__)
