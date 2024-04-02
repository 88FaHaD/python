l=[5,6,8,9]
try:
    index=int(input('enter a number '))
    print(l[index])
    print('executed sucessfully ')
except (IndexError,ValueError ) as msg:
    print('error is ', msg)
except:
    print('other error')
print('terminated gracefully')
