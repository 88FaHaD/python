s1='hello how are u'
print(s1[2],s1[3],s1[6])

for i in range(0,len(s1)):
    print(s1[i])

#Q print a string in reverse
for j in range(len(s1)-1,-1,-1):
    print(s1[j])

#Q skiping one letter
for z in range(0,len(s1),2):
    print(s1[z])
print()
print()
#Q  print from reverse and skip one letter
s2='mamammcnnanc'
for i in range(len(s2)-1,-1,-2):
    print(s2[i])

