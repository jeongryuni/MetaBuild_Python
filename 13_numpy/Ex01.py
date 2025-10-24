import numpy as np
print("=============== a ===============")
a = 100
print(a)
print(type(a))

print("=============== b ===============")
b = [1,2,3,4]
print(b)
print(type(b)) # list
print(len(b)) #4
print(sum(b)) # 10

print("=============== c ===============")

c = [[1,2,3,4],[5,6,7,8]]
print(c)
print(type(c)) # list
# print(len(c)) #2
for i in range(len(c)):
    for j in range(len(c[i])):
        print(c[i][j], end="")
    print()

print("=============== d ===============")
d = np.array(200)
print(d) # 200
print(type(d)) # numpy.ndarray

print("=============== e ===============")
e = np.array([1,2,3])
print(f"e:{e}")
print(type(f"e_type:{e}"))
print(f"e.ndim{e.ndim}") # 1차원

print("=============== f ===============")
f = np.array([[1,2,3,4],[5,6,7,8]])
print(f"f:{f}")
print(f"f_type:{type(f)}")
print(f"f.shape:{f.shape}") # 2,4 (2행 4열)
print(f"f.ndim:{f.ndim}") # 2차원
print(f"f.size:{f.size}") # 8

for i in range(f.shape[0]):
    for j in range(f.shape[1]):
        print(f[i][j], end="")
    print()

print("=============== g ===============")

g = np.array([[1,2,3,4]])
print(f"g:{g}")
print(f"g_type:{type(g)}")
print(f"g.shape:{g.shape}") # 1,4 (1행 4열)
print(f"g.ndim:{g.ndim}") # 2차원
print(f"g.size:{g.size}") # 4
print(f"g.itemsize:{g.itemsize}") #8
print(f"g.dtype:{g.dtype}") # int64

print("=============== h ===============")

h = np.array(c)
print(f"h:{h}")
print(f"h_type:{type(h)}") #numpy.ndarray
print(f"h.shape:{h.shape}") # (2, 4)
