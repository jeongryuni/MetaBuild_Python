import numpy as np

'''
41~100점 정수난수 5행 4열(5명 4과목)
0열 국어
1열 영어
2열 수학
3열 과학
'''

np.random.seed(0)
arr = np.random.randint(1,101,(5,4))
print(arr)

# 과목별 총점
sub_total = np.sum(arr, axis=0)
print(f"과목별 총점 : {sub_total}")

# 과목별 평균
sub_mean = np.mean(arr, axis=0) #열
print(f"과목별 평균 : {sub_mean}")

# 과목별 최대
sub_max = np.max(arr, axis=0)
print(f"과목별 최대 : {sub_max}")

# 과목별 최소
sub_min = np.min(arr, axis=0)
print(f"과목별 최소 : {sub_min}")

# 학생별 평균 >= 70점이면 합격
stu_avg = np.round(np.average(arr, axis=1))
result = np.greater_equal(stu_avg, 70)
print(f"70점이상 합격 : {result}")

# 전체 평균 :
total_avg = np.average(arr)
print(f"전체 평균 : {total_avg}")

# 영어점수 출력
eng_score = arr[0:,1]
print(f"영어점수 출력 : {eng_score}")

# 각 행에서 국어70, 수학80이 넘은 학생 찾기
for i in range(len(arr)):
    kor = arr[i][0]
    math = arr[i][2]
    if kor>=70 and math>=80:
        print(f"국어70, 수학80: {arr[i]}")

