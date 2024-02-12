students = ['sam', 'john', 'july', 'jimmy', 'julia']
for student in students:
    if student == 'jimmy':
        break
    print(student)
print(' ')
students = ['sam', 'john', 'july', 'jimmy', 'julia']
for student in students:
    if student == 'jimmy':
        continue
    print(student)