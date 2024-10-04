import math


class Shape:
    """All geometric shapes will inherit from this Shape class."""
    def __init__(self, name):
        self.name = name

    def area(self):
        """Returns the area of a shape"""
        print("Override this method in ", type(self))

    def perimeter(self):
        """Returns the perimeter of a shape"""
        print("Override this function in ", type(self))

class Circle(Shape):
    """A circle is characterized by its radii"""
    def __init__(self, name, radius):
        "*** YOUR CODE HERE ***"
        self.name = name
        self.radius = radius


    def perimeter(self):
        """Returns the perimeter of a circle (2πr)"""
        "*** YOUR CODE HERE ***"
        return 2 * math.pi * self.radius

    def area(self):
        """Returns the area of a circle (πr^2)"""
        "*** YOUR CODE HERE ***"
        return math.pi * self.radius ** 2

class RegPolygon(Shape):
    """A regular polygon is defined as a shape whose angles and side lengths are all the same.
    This means the perimeter is easy to calculate. The area can also be done, but it's more inconvenient."""
    def __init__(self, name, num_sides, side_length):
        "*** YOUR CODE HERE ***"

    def perimeter(self):
        """Returns the perimeter of a regular polygon (the number of sides multiplied by side length)"""
        "*** YOUR CODE HERE ***"
class Square(RegPolygon):
    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"

    def area(self):
        """Returns the area of a square (squared side length)"""
        "*** YOUR CODE HERE ***"

class Triangle(RegPolygon):
    """An equilateral triangle"""
    def __init__(self, name, side_length):
        "*** YOUR CODE HERE ***"

    def area(self):
        """Returns the area of an equilateral triangle is (squared side length multiplied by the provided constant"""
        constant = math.sqrt(3)/4
        "*** YOUR CODE HERE ***"

