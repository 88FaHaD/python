math=float(input('enter marks of math out of 40 '))
physics=float(input('enter marks of physics out of 30 '))
chemistry=float(input('enter marks of chemistry out of 30  '))

totalmarks=math+physics+chemistry

print()
print('to pass the exam you shiould score minimum 45 ')
if (totalmarks>=45 and totalmarks <= 100):
    print()
    print('passed since marks are greater then 45 i-e totalmarks scored are ',totalmarks)
else:
    print()
    print('failed snce marks are less then 45 ie marks scored ',totalmarks)
