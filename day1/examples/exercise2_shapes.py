"""
Refactor the code to eliminate duplication by creating a base class
from which other classes inherit common methods.
"""

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement the area method")

    def perimeter(self):
        raise NotImplementedError("Subclasses must implement the perimeter method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.1416 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.1416 * self.radius

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

class EquilateralTriangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return (3 ** 0.5 / 4) * self.side ** 2

    def perimeter(self):
        return 3 * self.side

# Example usage
if __name__ == "__main__":
    print("Code Debugging[2] Shapes")

    circle = Circle(radius=5)
    print(f"Circle Area: {circle.area()}")

    square = Square(side=4)
    print(f"Square Perimeter: {square.perimeter()}")

    triangle = EquilateralTriangle(side=3)
    print(f"Equilateral Triangle Area: {triangle.area()}")
