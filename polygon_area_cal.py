import math

# Base class
class Polygon:
    def __init__(self, name):
        self.name = name

    def area(self):
        raise NotImplementedError("Subclasses must implement area() method")

# Triangle class
class Triangle(Polygon):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

# Rectangle class
class Rectangle(Polygon):
    def __init__(self, length, width):
        super().__init__("Rectangle")
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

# Square class
class Square(Polygon):
    def __init__(self, side):
        super().__init__("Square")
        self.side = side

    def area(self):
        return se
