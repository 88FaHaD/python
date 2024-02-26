class rectangle:
    count=0     #class variable
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
        rectangle.count +=1

    def perimeter(self):
        return 2 * (self.length+self.breadth)
    def area(self):
        return (self.length * self.breadth)
    
    @classmethod 
    def countrect(cls):
        return cls.count
    
r1=rectangle(2,4)
r2=rectangle(3,6)

print("total no of rectangle are ",rectangle.countrect())
