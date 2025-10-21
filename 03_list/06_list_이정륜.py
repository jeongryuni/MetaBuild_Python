students = [
    ["kim", 90, 90],
    ["park", 85, 71],
    ["choi", 80, 75],
    ["jung", 45, 82],
    ["hong", 50, 60]
]

# 이름기준 오름차순
# 이름 대문자 변경

for student in students:
    student[0] = student[0].upper()
    total = student[1] + student[2]
    avg = total/len(student[1:])
    # avg = sum(student[1:])/len(student[1:])
    student.append(avg)

    if student[3] >= 90:
        grade = "A"
    elif student[3] >= 80:
        grade = "B"
    elif student[3] >= 70:
        grade = "C"
    elif student[3] >= 60:
        grade = "D"
    else:
        grade = "F"
    student.append(grade)
    students.sort()

from pprint import pprint
pprint(students)