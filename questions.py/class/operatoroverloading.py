#operator overloading upon rational numbers
class rational:
    def __init__(self,p=1,q=1):
        self.p=p
        self.q=q

    def __add__(self,other):
        s=rational()
        print(other.p) #some how they get the value
        print(other.q) # somehow they get the value
        s.p=self.p*other.q + self.q* other.p
        s.q=self.q * other.q
        return s
r1=rational(2,3)
r2=rational(3,5)
sum=r1+r2
print(sum.p,sum.q)