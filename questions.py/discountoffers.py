amount=float(input('enter the shoping amount '))
if(amount<=1000):
    discount=amount*(10/100)
    print('discount is 10 percent:-> ',discount,'\n\n total amount to be paid is:-> ', amount-discount)
elif(amount > 1000 and amount <=5000 ):
    discount=amount*(20/100)
    print('discount is 20 percent:-> ',discount,'\n \ntotal amount to be paid is:-> ', amount-discount)
elif(amount > 5000 and amount<= 10000):
    discount=amount*(30/100)
    print('discount is 30 percent:-> ',discount,'\n \ntotal amount to be paid is:-> ', amount-discount)
else:
    discount=amount*(50/100)
    print('discount is 50 percent ',discount,'\n \ntotal amount to be paid is:-> ', amount-discount)