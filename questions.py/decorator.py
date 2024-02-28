def greet(fxn):
  def wrapper(*args,**kwargs):
    print(' hello ')
    return fxn(*args,**kwargs)   
  return wrapper
@greet
def wel():
   return print('welcome to the university ')


wel()
