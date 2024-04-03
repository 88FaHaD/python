#if try block gets executed sucessfully  then else block gets executed if there is exception then else block is not executed
print('welcome')

try:
  a=int(input('enter a number '))
  b=int(input('enter a divisor '))
  c=a//b
  print('try executed sucessfully ')
except (IndexError,ValueError) as msg:
  print(msg)
else:
  print('result is :-> ',c )

print('outside tryexcept else')