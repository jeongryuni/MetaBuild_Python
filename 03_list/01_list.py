a=1
print(type(a)) # int

b="123"
print(type(b)) # str

c=True
print(type(c)) # bool

L = [10, 20, 30]
print(type(L)) # list
print(f"L[0]: {L[0]}")
print(f"L[-1]: {L[-1]}")
print(f"len(L): {len(L)}")
print(f"L.__len__(): {L.__len__()}")

for i in range(len(L)):
    print(f"{i}: {L[i]}")

for j in L:
    print(j)

L[0] = 1 # 0번째 인덱스 100으로 변경
print(L)

print(f"L+L : {L+L}") # [1, 20, 30, 1, 20, 30]
print(f"L*3 : {L*3}") # [1, 20, 30, 1, 20, 30, 1, 20, 30]