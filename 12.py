class Shape:
    def __init__(self, color):
        self.color = color

    def draw(self):
        print(f"Drawing a {self.color} shape")

class Circle(Shape):
    def draw(self):
        print(f"Drawing a {self.color} circle")

class Square(Shape):
    def draw(self):
        print(f"Drawing a {self.color} square")

# Usage
circle = Circle("red")
circle.draw()  # Output: Drawing a red circle

square = Square("blue")
square.draw()  # Output: Drawing a blue square
