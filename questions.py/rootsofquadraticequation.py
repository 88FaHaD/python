import math
a=int(input('enter A '))
b=int(input('enter B '))
c=int(input('enter c '))

d=b**2 - 4*a*c

if d >= 0:
    r1 = (-b + math.sqrt(d)) / (2*a)
    r2 = (-b - math.sqrt(d)) / (2*a)
    print('Roots are:', r1, r2)
else:
    print('Roots are complex')