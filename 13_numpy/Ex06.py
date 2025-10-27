import random
from math import trunc

import numpy as np

count = 5
su = 2

# np.repeat(반복할 숫자, 반복횟수)
result = np.repeat(su, count)
print(result)

arr1 = np.array([1,2])
arr2 = np.array([3,4])
print(f"arr1 :{arr1}\narr2 :{arr2}")
print(arr1 + arr2) # [4,6]

# np.concatenate : array병합
result = np.concatenate((arr1, arr2))
print(result) #[1,2,3,4]

# hstack : 가로로 쌓기 hs:[1 2 3 4]
hs = np.hstack((arr1, arr2))
print(f"hs:{hs}")

# vstack : 세로로 쌓기
# vs:
# [[1 2]
#  [3 4]]
vs = np.vstack((arr1, arr2))
print(f"vs:\n{vs}")

print("-----------------------")
arr = np.array([1.57, 2.48, 3.93, 4.33, -1.57, -2.48])
print(f"arr:{arr}")

# np.ceil(x) : 올림 (Ceiling)
result = np.ceil(arr)
print("ceil:", result)

# np.floor(x) : 내림 (Floor)
result = np.floor(arr)
print("floor:", result)

# np.trunc(x) : 버림 (Truncate)
result = np.trunc(arr)
print("trunc:", result)

# np.round(x, n) : 반올림 (Round)
result = np.round(arr, 1)
print("round:", result)

# np.sqrt(x) : 제곱근 (Squared Root)
# sqrt = np.sqrt(arr)
# print(f"sqrt:{sqrt}")

# squared : 제곱(squared)
squared = arr ** 2
print(f"squared:{squared}")

arr2 = np.sum(arr), np.average(arr), np.mean(arr), np.max(arr),np.min(arr)
print(f"arr2:")
print(f"  총합(sum)     : {arr2[0]}")
print(f"  평균(average) : {arr2[1]}")
print(f"  평균(mean)    : {arr2[2]}")
print(f"  최댓값(max)   : {arr2[3]}")
print(f"  최솟값(min)   : {arr2[4]}")

print("---------------------------------")
arr1 = np.array([1.57, 2.48, 3.93, 4.33, -1.57, -2.48])
arr2 = np.array([1.57, -2.48, 3.93, -4.33, -1.57, -2.48])
arr3 = np.array([23.57, -2.48, 3.93, -4.33, -1.57, -2.48])
print(np.max(arr1))
print(np.maximum(arr1, arr2)) # np.maximum(arr1, arr2): 두 배열의 각 위치별로 큰 값을 선택해 반환
print(np.equal(arr1, arr2)) # np.equal(arr1, arr2) : 두 배열의 각 위치별로 동일한지 판단

arr1 = np.array([[1, 2],
                 [3, 4]])

arr2 = np.array([[5, 6],
                 [7, 8]])

print(f"arr1:\n", arr1)
print(f"arr2:\n", arr2)
print('1:', np.sum(arr1))
print('2:', np.sum(arr1, axis=0)) # 각열 합
print('3:', np.sum(arr1, axis=1)) # 각행 합
print('4:', np.mean(arr1))
print('5:', np.mean(arr1, axis=0)) # 각열 나누기
print('6:', np.mean(arr1, axis=1)) # 각행 나누기

print('--------------------------------')

# 난수 기본값
np.random.seed(0)
randomValue = np.random.random() # 0 < x < 1
print(randomValue)
print(round(randomValue * 10)) #  0 ~ 9
print(round(randomValue * 45)+1) # 1 ~ 45

print('--------------------------------')
import random
print(random.random())
print(random.randrange(2,30)) # 2~29사이 정수 난수

print(np.random.randint(1,7, 5)) # 1~7숫자 5개 난수
print(np.random.randint(1,30, (2,3))) # 1~29숫자 2행3열 행렬만들기

# 반복하여 난수 발생 : 중복발생
list_num = []
for i in range(10):
    num = random.randrange(1, 20)
    list_num.append(num)
print(list_num)

# sample : 중복이 나오지않음
list2 = random.sample(range(1,7), 5)
print(list2)
