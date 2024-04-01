# check if password are same and confirm the password
str1 = input('Enter password: ')
str2 = input('Re-enter password: ')

if str1 == str2:
    print('Password confirmed.')
elif str1.lower() == str2.lower():
    print('Please check the cases.')
else:
    print('Passwords do not match.')
