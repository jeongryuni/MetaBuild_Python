t=(1,2,3,4,5)
print(type(t))
print(t[0], t[1], t[2], t[3], t[4])
print(t[-1])


for i in range(len(t)):
    print(t[i])
print()

for num in t:
    print(num)

# t[2]=8 튜플은 변경 안됨