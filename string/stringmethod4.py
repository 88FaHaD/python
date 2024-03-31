# inquirymethods
s1='hello'
print(s1.islower())
print(s1.isupper())
print(s1.istitle())

#isalnum checks if string contains alphabets and numbers
s2="ll00"
print(s2.isalnum())

#isalpha checks if the string contains  alphabets
print(s1.isalpha())

#isspace if a string contains only spaces
s3="hello how are u"
print(s3.isspace())

#is ascii checks if string contains ascii codes
print(s3.isascii())

#is identifier checks if its an identifer and variable
s4='if'
print(s4.isidentifier())

#is printable there are some characters like escape sequence which are not printable is printable checks that
s5='hello'
print(s5.isprintable())
s6="hel \n"
print(s6.isprintable())

#is decimal returns if string contains only decimal 0-9 numbers no floating values square not allowed if in fracton not allowed floatig point not alowed
s7='256'
print(s7.isdecimal())
s8='abcd'
print(s8.isdecimal())

#is digit checks if numebrs are there only decimal square allowed if in fracton not allowed floatig point not alowed
s9='88892'
print(s9.isdigit()) 

#is numeric return true for any type of number sqauare alowed if in fracton  allowed floatig point not alowed
s10='89'
print(s10.isnumeric())

