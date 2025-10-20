# L = list(range(10))

L = [i for i in range(10)]

jumsu = [90, 25, 67, 45, 80]
print(f"합계: {sum(jumsu)}")
print(f"최대값: {max(jumsu)}")
print(f"최소값: {min(jumsu)}")

for i in enumerate(jumsu):
    print(i)
print()

for i,j in enumerate(jumsu, start=1):
    print(i, j)
print()
