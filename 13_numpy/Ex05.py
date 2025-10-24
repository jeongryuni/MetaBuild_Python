import numpy as np

arr = np.array([[1,2],[3,4],[5,6]])
print(f"arr:\n{arr}")
print(arr[0][0], arr[1][1], arr[2][0])

# (0행, 0열) → 1
# (1행, 1열) → 4
# (2행, 0열) → 5
print(f"arr[[0,1,2],[0,1,0]] :\n{arr[[0,1,2],[0,1,0]]}") #
print(arr[np.arange(3),[0,1,0]]) # == arr[[0,1,2],[0,1,0]] (같음)

# arr[[0,2]] → 행 인덱스 0과 2만 선택
# 즉, 첫 번째 행([1,2])과 세 번째 행([5,6])을 동시에 추출
print(f"arr[[0,2]]:\n{arr[[0,2]]}")

# 1행 1열
print(f"arr[1,1]:\n{arr[1,1]}")

print("----------------------------")
arr = np.array([[1,2],[3,4],[5,6]])
print(f"arr:\n{arr}")
result = arr>2
print()
print(arr[result]) #[3 4 5 6]
print(arr[arr>2]) #[3 4 5 6]
print()

