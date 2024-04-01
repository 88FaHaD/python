#display credit card number in secret format
s1=input('enter the card number ')
print(len(s1))
s2=s1[15:19]
print(s2.rjust(15,'*'))

#alternative method
s1=input('enter the card number ')
s2=s1[15:19]

s3='**** ' * 3
print(s3+s2)