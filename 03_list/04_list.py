L=[
    ['apple', 'banana'],
    [10,20,30]
]

print("L", L)
print("L[0][0] :", L[0][0])
print("L[0] :", L[0])
print("L[1] :", L[1])
print("----------")

# 배열 인덱스로 접근
for i in range(0,len(L)):
    for j in range(len(L[i])):
        print(L[i][j], end=" ")
    print()
print("----------")

# 리스트 직접 접근
for i in L:
    for j in i:
        print(j, end=" ")
    print()

