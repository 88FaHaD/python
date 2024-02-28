def dec(fxn):
    def wrapper(*args,**kwargs):
        print('addition is ')
        return fxn(*args,**kwargs)
    return wrapper

@dec
def add(a,b):
     print(a+b)

add(2,5)