import numpy as np

'''
41~100점 정수난수 5행 4열(5명 4과목)
0열 국어
1열 영어
2열 수학
3열 과학
'''

np.random.seed(40)
arr = np.random.randint(60,101,(5,4))
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
name = np.array(['윤아', '민호', '혜수', '해영', '민지'])
stu_mean = np.greater_equal(stu_avg, 70)
print(name[stu_mean]) # 슬라이싱 출력

# 결과 출력
result = list(map(lambda n, p: (n, '합격' if p else '불합격'), name, stu_mean))
for r in result:
    print(r) # 람다출력

# 전체 평균 :
total_avg = np.average(arr)
print(f"전체 평균 : {total_avg}")

# 영어점수 출력
eng_score = arr[0:,1]
print(f"영어점수 출력 : {eng_score}")

# 각 행에서 국어70, 수학80이 넘은 학생 찾기
cond = (arr[:,0] >= 70) & (arr[:,2] >= 80)
print(arr[cond])

