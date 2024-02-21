p1=int(input('enter the age of person 1 '))
p2 = int(input('enter age of person 2 '))
p3=int(input('enter age of person 3 '))

if(p1>p2 and p1>p3):
    print('person1  is the eldest ')
elif(p2>p1 and p2>p3):
    print('p2 is the eldest ')
else:
    print('p3 is the eldest ')