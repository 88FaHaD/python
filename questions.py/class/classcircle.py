class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 *(self.radius ** 2)
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
r=circle(7)
print('area is ', r.area())
print('perimeter is',r.perimeter())