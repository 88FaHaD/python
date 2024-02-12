a=int(input('enter num 1 '))
b=int(input('enter num 2 '))
num=int(input('enter 1 for add, 2 for sub 3 for mult i 4 for div 5 for modular div '))

if num==1:
    print('add is ',a+b)
elif num==2:
     print('sub is ',a-b)
elif num==3:
     print('mul is ',a*b)   
elif num==4:
     print('div is ',a/b) 
elif num==5:
     print('moddiv is ',a%b) 
else:
     print('invalid input ')