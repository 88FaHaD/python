# check if string is palindrome or not
s1='madam'
s2=s1[::-1]
if(s1==s2):
    print('the given string is palindrome')
else:
    print('it is not a palindrome ')

# convert a strinf to palindrome
s1=input('enter a string ')
s2=s1+s1[::-1]
print(s2)