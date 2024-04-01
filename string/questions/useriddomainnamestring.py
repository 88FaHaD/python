# find user id and domain name in an email address
s=input('enter email address ')
print(s.find('@'))
print(len(s))
name=s[0:5]
domain=s[6:15]
print('user id :- ',name)
print('domain name :- ',domain)