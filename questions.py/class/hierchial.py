class Shape:
    def area(self):
        return "Area method in Shape class"

class Circle(Shape):
    def circle_area(self):
        return "Area method in Circle class"

class Rectangle(Shape):
    def rectangle_area(self):
        return "Area method in Rectangle class"

class Triangle(Shape):
    def triangle_area(self):
        return "Area method in Triangle class"

# Instances
circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

# Hierarchical Inheritance Example
print(circle.area())      
print(rectangle.area())   
print(triangle.area())    
