def add(a,b):
    print("add")
    return a+b

result = add(1,2)
print(result)

result = add(1.1, 2.2)
print(result)

result = add([1,2,3],[4,5,6])
print(result)

print("-----------")
def func():
    pass
result = func()
print(result)


print("-----------")
def func2(x,y=0,z=0):
    return x+y+z

print(func2(1))
print(func2(1,3))
print(func2(1,3,5))

