import numpy as np
a = np.array([-1,3, 2, 6])
b = np.array([3,6,1,2])
print(f"a+b={a+b}") # 같은 인덱스번호끼리 연산
print(f"a*b={a*b}")
print(f"np.matmul(a,b):{np.matmul(a,b)}") #각방끼리 곱하고 더하기 -3+18+2+12=29
print(f"a.ndim:{a.ndim}") # 1차원
print(f"a.shape:{a.shape}") # (2,2)

#A = np.reshape(a,(2,2)) #shape변경
A = a.reshape([2,2])
print(A)
print(f"A.ndim:{A.ndim}") # 2차원
print(f"A.shape:{A.shape}") #2,2

B = np.reshape(b,[2,2])
print(B)

print(f"A+B\n:{A+B}")
print(f"A*B\n:{A*B}")
print(f"np.matmul:\n{np.matmul(A,B)}")

# matmul
# 결과 행렬 AB = A × B
# 각 원소의 계산 과정:
# AB[0][0] = A[0][0]*B[0][0] + A[0][1]*B[1][0] = (-1)*3 + (3)*1 = 0
# AB[0][1] = A[0][0]*B[0][1] + A[0][1]*B[1][1] = (-1)*6 + (3)*2 = 0
# AB[1][0] = A[1][0]*B[0][0] + A[1][1]*B[1][0] = (2)*3 + (6)*1 = 12
# AB[1][1] = A[1][0]*B[0][1] + A[1][1]*B[1][1] = (2)*6 + (6)*2 = 24

result = A.T
print(result)

