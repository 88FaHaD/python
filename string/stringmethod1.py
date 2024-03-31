#find
#rfind
#index
#rindex
#count

#find
# find method helps to search the substring to find in the string it will return where the substring is present if its not it
# will return -1
s1='helllo how are u'
print(s1.find('r')) # one letter
print()
print(s1.find('are')) # multipple letters
print()
print(s1.find('e',6,15)) # with starting and ending
print()
print(s1.find('k')) # will return -1

#rfind
# does the same operation but from reverse order
print()
print(s1.rfind('u')) # one letter
print(s1.rfind('are')) # multiple letters
print(s1.rfind('e',0,5)) # starting and endng 
print()

#index
#index is simlar to find  but when substring is not preset it throws an error
print(s1.index('e')) 
print(s1.index('are'))
# print(s1.index('k')) throws error
print(s1.index('o',7,11))
print()

#rindex
#does the operation from reverse side
print(s1.rindex('e'))
print(s1.rindex('are'))
print(s1.rindex('o',4,7))
print()

#count
#count is used to count number of times a lettter or letters are present in the string if the are notit returns 0
print(s1.count('o'))
print(s1.count('o',6,15))
print(s1.count('lll'))
print(s1.count('g'))