#replace 
#replaces an letter with anoter letter,word digit etc and creates a new string
#syntax s.replae('old','new'[count which is optional])
s="a,b,c,d"
print(s.replace(',','-'))
print(s)
#join
#joins chracters of one string with another s='xyz' s2='abc' sj.join(s2)=axyzbxyzcxyz 
# also can be used with list and tuple
s='xyz'
s2='abc'
print(s.join(s2))

#Q print /a/b/c using s.join
s1='/'
s2='abc'
print(s1.join(s2))

#Q print a*b*c
s='*'
s2='abc'
print(s.join(s2))

#split
#for eg s='john july sam' is a string if we use s.split it will find space which is seperator  and when space is
# find it will create a list if there are n spces there will be n+1 
# seperator can be any space , - etc  
# also can mention max  split which is optional
s='john july sam'
s2=s.split()
print(s2)
print(type(s2))
m='john-july-sam'
print(m.split('-'))

#r-split spliting done from right side