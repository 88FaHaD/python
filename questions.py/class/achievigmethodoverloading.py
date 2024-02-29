#Achieving method overloading in python
def sum(a,b,c=None):
     s=a+b
     if(c==None):
          return s
     else:
          return s+c
     
print(sum(2,4))

print(sum(2,4,5))