import numpy as np
# list와 array비교

L = [0,1,2,3,4,5,6,7,8,9]
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arg = np.arange(10)

print(L)
print(arr)
print(arg)

print("-----------------------")
print(L[5])
print(arr[5])
print(arg[5])

print("-----------------------")
print(L[5:8]) # [5, 6, 7]
print(arr[5:8]) # [5 6 7]
print(arg[5:8]) # [5 6 7]

print("-----------------------")
print(L[3::2]) # [3, 5, 7, 9]
print(arr[3::2]) #[3 5 7 9]
print(arg[3::2]) # [3 5 7 9]

print("-----------------------")
print(L[::2]) # [0, 2, 4, 6, 8]
print(arr[::2]) #[0 2 4 6 8]
print(arg[::2]) #[0 2 4 6 8]

print("-----------------------")
#L[5] = [12]
#arr[5]=12 # 배열형태 X
#arg[5]=12
print(f"L:{L}") # [0, 1, 2, 3, 4, [12], 6, 7, 8, 9]
print(f"arr:{arr}") # [ 0  1  2  3  4 12  6  7  8  9]
print(f"arg:{arg}") # [ 0  1  2  3  4 12  6  7  8  9]

print("-----------------------")
L[5:8] = [12]
arr[5:8] = [12]
arg[5:8] = 12
print(L) # [0, 1, 2, 3, 4, 12, 8, 9]
print(arr)  # 괄호없어도 결과같음 [ 0  1  2  3  4 12 12 12  8  9]
print(arg) #[ 0  1  2  3  4 12 12 12  8  9]

print("-----------------------")
L = [0,1,2,3,4,5,6,7,8,9]
arr = np.array([0,1,2,3,4,5,6,7,8,9])
arg = np.arange(10)

# 리스트
list_slice=L[5:8]
print(f"list_slice:{list_slice}")
list_slice[1] = 100
print(f"list_slice:{list_slice}")
print(f"L : {L}") # 원본 변경 X

# array
arr_slice = arr[5:8]
print(f"arr_slice:{arr_slice}")
arr_slice[1] = 100
print(f"arr_slice:{arr_slice}")
print(f"arr : {arr}") # 원본 변경

# arange
arg_slice = arg[5:8]
print(f"arg_slice:{arg_slice}")
arg_slice[1] = 100
print(f"arg_slice:{arg_slice}")
print(f"arg : {arg}") # 원본 변경

print("-----------------------")
# array=np.array(range(1,13)).reshape((3,4))
array = np.arange(1,13).reshape(3,4)
print(f"array:\n{array}")

print(array[0][1])
print(array[0:2,1])
print(array[:2,1])
print(array[:2,1:]) # 0행~1행, 1열~끝열
print(array[1, 1:3]) # 1차원 [6, 7] == 정수 인덱싱 → 그 차원이 사라짐
print(array[1:2, 1:3]) # 2차원 [[6, 7]] == 슬라이싱(:) → 그 차원이 유지됨

