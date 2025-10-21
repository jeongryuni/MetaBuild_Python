print("----------func1-----------")
x = 10 #전역변수
def func():
    x=30 #지역변수
    print('func x:', x)

func() # 지역변수 출력
print('x:', x) # 전역변수 출력

print("----------func2-----------")
y = 10
def func2(y):
    y=y*y
    global k
    k=30
    print('func2 y:', y)

func2(y)
print('y:', y)
print('k:', k)