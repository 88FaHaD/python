l=[2,3,4,5,6,7]

try:
    index=int(input('enter a value '))
    print(l[index])
    print('end of try block ')
except IndexError:
    print('invalid index ')
except ValueError:
    print('integer values only allowed  ')
except:
    print('some error will occur')

print('terminated gracefully')
