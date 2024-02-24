num= int(input('enter a number '))
print('factors of the input number are ')

for i in range(1,num):
    if(num%i== 0):
        print(i)

print(num)
