class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)

# Example usage
rect1 = Rectangle(5, 4)
print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())
