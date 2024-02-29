# if we create two functions with same name and different arguments the first fuvtion will be shadowed 
#first function
def sum(a,b):
    return a+b
#seconf function
def sum(a,b,c):
    return a+b+c

print(sum(2,4,6))

print('the first function will not be executed ')
print(sum(2,4))