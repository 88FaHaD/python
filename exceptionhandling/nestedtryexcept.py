# if there is error in first try then second try will not be executed and exception of first try will be handled rest will
# be skiped
#if there is no  error in first try then second try will be executed if there is error then exception of second try will be
#executed  
print('before try ')
try:
    a=int(input('enter a number '))
    b=int(input('enter a divisor '))
    c=a//b
    print('first try executed ')
    try:
       m=[10,23,45,67]
       index=int(input('enter a index '))
       print(m[index])
       print('second try executed ')
    except IndexError as msg:
         print(msg)
         print('exception of second try ')
except ZeroDivisionError as msg:
   print(msg)
   print('exception of first try ')
   
print('terminated gracefully ')
   