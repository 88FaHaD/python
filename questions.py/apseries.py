# give the starting term the difference and and how many terms to be printed

a=int(input('enter the starting term '))
diff=int(input('enter the difference '))

count=int(input('enter the terms u want to print '))
print(a)
for i in range(count):
    a=a+diff
    print(a)
