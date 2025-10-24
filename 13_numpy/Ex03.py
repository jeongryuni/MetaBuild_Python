import numpy as np

a = range(5)
print(a)

b=np.arange(5)
print(b)
print(type(b))
for i in np.arange(5):
    print(i, end=" ")
print()

c = np.arange(20, 7, -1)
print(c)

d = np.arange(2*3).reshape(2,3)

print(f"d:{d}")
print(f"d.ndim:{np.ndim(d)}")
print(f"d.shape:{d.shape}")

e = np.arange(2*3).reshape(3,2)
print(f"e:{e}")
print(f"e.ndim:{np.ndim(e)}")
print(f"e.shape:{e.shape}")
print(np.matmul(d,e))
# 0 1 2
# 3 4 5
#
# (0,0) = 0*0 + 1*2 + 2*4 = 0+2+8 = 10
# (0,1) = 0*1 + 1*3 + 2*5 = 0+3+10 = 13
# (1,0) = 3*0 + 4*2 + 5*4 = 0+8+20 = 28
# (1,1) = 3*1 + 4*3 + 5*5 = 3+12+25 = 40

f = np.array([0,1,'2','abc',True,'True'])
print(f"f:{f}")
print("---------------------")

# 0으로 채움 : zeros
arr1 = np.zeros(3)
print(arr1)
'''
[0. 0. 0.]
'''

arr2 = np.zeros((2,3))
print(arr2)
'''
[[0. 0. 0.]
 [0. 0. 0.]]
'''

# 2,3shape으로 1로 채움
arr3 =np.ones((2,3))
print(arr3)
'''
[[1. 1. 1.]
 [1. 1. 1.]]
'''

arr4 = np.full((2,3), 7)
print(arr4)
'''
[[7 7 7]
 [7 7 7]]
'''

# 대각선으로 1이 채워짐 (3,3)
arr5 = np.eye(3)
print(arr5)
'''
[[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]
'''


