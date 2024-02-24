num=int(input('enter a number for checking if its prime oor not '))
count=0
for i in range(1,num+1):
     if (num%i==0):
          count=count+1
          

       
if(count==2):
     print('its  prime')
else:
     print('not pprime')