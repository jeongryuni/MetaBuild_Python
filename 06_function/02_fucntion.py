print('--------func1--------')
def func(*args):
    for i in args:
        print(i, end="/")
    print()

func()
func(1,2)
func([1,2,3], (4,5,6))
func("apple", "banana", "orange")

print('--------func2--------')
def func2(a,b, *args):
    print('a', a)
    for i in args:
        print(i, end="/")
    print()

func2(1, 2)
func2([1,2,3], (4,5,6))
func2("apple", "banana", "orange")

print('--------func3--------')
tp = (1,2,3)
def func3(a,b,c) :
    print('a', a)

func3(tp[0], tp[1], tp[2])

print('--------func4--------')
def func4(a,b,c) :
    print(a,b,c)

func4(*tp)

print('--------func5--------')
d = {'x':10, 'b':20, 'c':30}
def func5(x,b,c) :
    print(x,b,c)

func5(*d)
func5(**d)

print('--------func6--------')
def func6(x) :
    if x > 1:
        return x + func6(x-1)
    elif x == 1:
        return 1
    return None

result = func6(5)
print(result)

print('--------func7--------')
def func7(x) :
    return {
        'a':1,
        'b':2
    }.get(x,100)

print(func7('a'))
print(func7('b'))
print(func7(100))

