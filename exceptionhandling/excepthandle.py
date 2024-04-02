l=[2,3,4,5,6]
index=int(input('enter a number '))

try:
    print(l[index])
    print('end of try block ')
except:
    print('Invalid index ')

print('terminated gracefully ')
