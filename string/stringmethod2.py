'''
spaces can be added by these functions these functions create new strings
1 ljust 2 rjust 3 center

spaces can be removed by these fnctions these functions  create new strings and also remove tailing characters
1 strip 2 rstrip 3 lstrip

'''
#ljust
# creates a new string with spaces on left
#syntax s.ljust(value,'optional')
s1='python'
print(s1,' length is ',len(s1))

print()
s2=s1.ljust(10)
print(s2,' length is ',len(s2))
print()
print(s1.ljust(10,'*'))
print()

#rjust 
#does same with spaces from right and creates a new string
# syntax same
s1='python'
print(s1.rjust(10))
print(s1.rjust(10,'*'))

print()
#center
#leave equal spaces on left as well as right and creates a new string
#syntax same
s1='python'
print(s1.center(10))
print(s1.center(10,'*'))
print()
print('orignal string no changed and remains same ')
print(s1)
print()

#strip
# removes spaces as well as tailing characters from bth left and right side also creates a new string
# syntax s1.strip() for removing space and s1.strip('character u want to remove')
s1='.. ++ hello .. ++'
s2='  hello   '
print(s2)
print(s1)
print()

print(s2.strip())
print(s1.strip('.. ++'))
print()

#rstrip
# removes spaces as well as tailing characters from right side also creates a  new string
#  ssyntax same
print(s2.rstrip())
print(s1.rstrip('.. ++'))
print()

#lstrip
# removes spaces as well as tailing characters from left side also creates a  new string
# syntax same
print(s2.lstrip())
print(s1.lstrip('.. ++'))