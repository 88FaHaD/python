class rectangle:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    
    @staticmethod
    def issquare(l,b):
        if l==b:
            return True
        else:
            return False
        
r1=rectangle(10,10)
print(rectangle.issquare(10,10))
print(rectangle.issquare(10,5))