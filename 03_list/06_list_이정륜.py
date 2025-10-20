students = [
    ["kim", 80, 90],
    ["park", 80, 71],
    ["choi", 30, 75],
    ["jung", 40, 22],
    ["hong", 50, 60]
]

# 이름기준 오름차순
# 이름 대문자 변경

for student in students:
    student[0] = student[0].upper()
    total = student[1] + student[2]
    avg = total/len(student[1:])
    student.append(avg)

    if student[3] >= 70:
        student.append("A")
    elif student[3] >= 60:
        student.append("B")
    elif student[3] >= 50:
        student.append("C")
    else:
        student.append("D")
    students.sort()

print(students)