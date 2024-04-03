#finally will be always executed  used for releasing resources 
print('welscome')

try:
  a=int(input('enter a number '))
  b=int(input('enter a divisor '))
  c=a//b
  print('try executed sucessfully')
except (ValueError,IndexError) as msg:
  print(msg)
except:
  print('other type of error ')
else:
  print('result is ',c)
finally:
  print('always will be executed ')

print('outside try except else finally ')