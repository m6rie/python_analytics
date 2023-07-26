# Abstract class provide a template base class for other classes to inherit from
# There can't be instances of the abstract class itself
# The subclasses themselves will provide the implementation of the abstract class
# Allows to make it mandatory for subclasses to implement certain method
'''
We want to create geometrical shape.
All the shape will inherit from the GraphicShape class but
we don't want the user to be able to create instance of GraphicShape
To achieve that, we'll use the ABC (or Abstract Base Class) module
'''
from abc import ABC, abstractmethod


class GraphicShape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod  # indicates the calcArea function below is an abstract method.
    # this tells Python there is not implementation and each subclass should overwrite the method
    def calcArea(self):
        pass


class Circle(GraphicShape):

    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius**2)


class Square(GraphicShape):

    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


# g = GraphicShape() this gives a TypeError error

c = Circle(
    10
)  # this will give a TypeError error if no calcArea method is added to the method
print(c.calcArea())
s = Square(12)
print(s.calcArea())
