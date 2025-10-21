import pprint

print("------------Ex01------------")
def func(x):
    return x**2

print(func(4))

print("------------Ex02------------")
# lambda 매개변수1, 매개변수2, ... : 반환값

a = lambda x: x**2
print(a(5))

print("------------Ex03------------")
b = lambda x,y: x+y
print(b(10, 20))

print("------------Ex04------------")
L = 1,2,3,4,5
print(L) #튜플

#map(함수, 작업대상)
# map()이 리스트의 각 요소(= 문자열)에 len()을 “하나씩” 적용
result = list(map(lambda x : x**2, L))
print(result)

print("------------Ex05------------")
fruit = ["apple", "banana", "orange", "kiwi"]
result2 = list(map(lambda x : len(x), fruit))
print(result2)

print("------------Ex06------------")
a = [1,2,3]
b = [10,20,30]

result3 = list(map(lambda x,y : x+y, a,b))
print(result3)

print("------------Ex07--------------")
L = [13,16,11,15,14]
result4 = list(map(lambda x: "짝" if x%2 == 0 else"홀", L))
print(result4)

print("------------Ex08--------------")
fruit = ["apple", "banana", "orange", "kiwi"]
result5 = list(map(lambda x : (x.upper(),len(x)), fruit))
print(result5)

print("------------Ex09--------------")
students = [
    ["kim", 90, 90],
    ["park", 85, 71],
    ["choi", 90, 75],
    ["jung", 45, 82],
    ["hong", 50, 60]
]
students.sort(key=lambda x : (-x[1], x[2]))
pprint.pprint(students)


print("------------Ex10--------------")
L = [13,16,11,15,14]
result6 = list(filter(lambda x : x%2==0, L))
print("filter :",result6)
result6_2 = list(map(lambda x : x%2==0, L))
print("map :",result6_2)

print("------------Ex11--------------")
fruit = ["apple", "banana", "orange", "kiwi"]
result7 = list(filter(lambda x : len(x)>=6, fruit))
print("6글자 이상 필터 :",result7)

print("------------Ex12--------------")
students = [
    ["kim", 90, 90],
    ["park", 85, 71],
    ["choi", 90, 75],
    ["jung", 45, 82],
    ["hong", 87, 87]
]

result8 = list(filter(lambda x : x[1]>=80, students))
print("국 80점 이상 :", result8)

result9 = list(filter(lambda x : (x[1]>=87 and x[2]>=87), students))
print("국,영 87이상 :",result9)

# 튜플(kim,평균), (jung,평균)  튜플로 묶꼬 리스트로 만들기
result10 = list(map(lambda x : (x[0], ((x[1]+x[2])/2)), students))
print(result10)

# result10에서 평균 80이상 걸러내기
result11 = list(filter(lambda x: x[1]>=80, result10))
print(result11)

print("------------Ex13--------------")
score = {
    '윤아': {'국어':99, '수학':99, '영어':99},
    '정국': {'국어':15, '수학':12, '영어':13},
    '태연': {'국어':41, '수학':25, '영어':78},
    '보검': {'국어':75, '수학':83, '영어':75}
}

result = {}
for name in score.keys():
    total = sum(score[name].values())
    sub_count = len(score[name])
    avg = round(total / sub_count, 2)
    result[name] = avg

# 80점 이상 출력
avg_80 = list(filter(lambda x: x[1] >= 80, result.items()))
print(avg_80)