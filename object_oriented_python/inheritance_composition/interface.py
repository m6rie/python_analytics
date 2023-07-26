# to get previously created classes to inherit from a new class
from abc import ABC, abstractmethod


class JSONfy(ABC):

    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape):

    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius**2)


c = Circle(10)
print(c.calcArea())
