#slicing
s1='hello world'
print(s1[0:len(s1):1])
print(s1[:len(s1):1])
print(s1[::1])
print(s1[::])

# the above thing shows that startung point ending poinr and gap are optional

#Q print from third index ?
print(s1[3::])

#Q print from 6th index ?
print(s1[6::])

#Q print from 6th to 8th index
print(s1[6:8])

#Q print with 2 gap
print(s1[::2])

#Q print a string in reverse
print(s1[::-1])
print(s1[-1:-len(s1)-1:-1])
print(s1[-1::-1])

print()
print()

#Q print  a string in reverse and a gap ofone letter
print(s1[::-2])