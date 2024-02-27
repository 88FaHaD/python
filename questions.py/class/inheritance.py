class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.bradth=breadth
    def area(self):
        return self.length * self.bradth
    
class square(rectangle):
    def __init__(self, length, breadth):
        self.length=length
        self.bradth=breadth

s=square(5,5)
print('area is ',s.area())