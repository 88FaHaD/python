#print the string in less then 25 letters in given format chickenpizza........350
s1=input('enter the order ')
s2=input('enter the price ')
total_len=len(s1)+len(s2)
print(total_len)
s3='.' * (25-total_len)
s4=s1+s3+s2
print(s4)
print(len(s4))