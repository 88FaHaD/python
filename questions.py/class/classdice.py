from random import randint

class dice:
    def __init__(self,side):
        self.side=side
    def rolldice(self):
        return randint(1,self.side)
    
d1=dice(6)
print(d1.rolldice())
print(d1.rolldice())