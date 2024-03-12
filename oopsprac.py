class rectangle:
    count=0
    def __init__(self,l,b):
        self.l=l
        self.b=b
        rectangle.count+=1
    
    def area(self):
        print(self.l*self.b)
    
    @classmethod
    def countrect(cls):
        print(rectangle.count)

r1=rectangle(2,4)
r2=rectangle(3,8)

r1.area()

rectangle.countrect()