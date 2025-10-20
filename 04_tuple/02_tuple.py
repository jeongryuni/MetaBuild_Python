t1 = ()
t2 = (1, 2, 3)
t3 = 1,2,3
t4 = (1,)
t5 = 1,
t6 = (1)
t7 = 1

print("t1 :",t1, type(t1)) # tuple
print("t2 :",t2, type(t2)) # tuple
print("t3 :",t3, type(t3)) # tuple
print("t4 :",t4, type(t4)) # tuple
print("t5 :",t5, type(t5)) # tuple
print("t6 :",t6, type(t6)) # int
print("t7 :",t7, type(t7)) # int


t = (1,2,3)
print(t[0])

t2 = t+('kim', 'park')
print("1) t2:",t2)      # (1, 2, 3, 'kim', 'park')

t2 = t, ('kim', 'park')
print("2) t2:", t2)         # ((1, 2, 3), ('kim', 'park'))
print("t2[1][0]", t2[1][0]) # kim

x,y,z = 1,2,3
print(x,y,z) # 1,2,3

x,y = y,x   #(자리바꿈 가능)
print(x,y) # 2,1

p,q,r = t       # 튜플t에 들어있는 값 1,2,3을 각각 변수에 넣음
print(p,q,r)

t=(1,2,3)
L = list(t) # 임시로 리스트 변경 후 값 변경
L[0] = 99
print("리스트 L",L)

t3 = tuple(L)
print("튜플 L:", t3)

print("id:%s pw:%s" %("kim", "1234")) #튜플 형태