# raise is used to creat user defined error

class Myerror(Exception):
    pass
try:
  a=int(input('enter a number '))
  b=int(input('enter a divisor '))
  if b==0:
   raise Myerror('some  error')
  else:
     c=a//b
     print('try executed sucessfully')
except Myerror as e:
    print(e)
else:
   print('result is ', c)

print('terminated sucessfully')