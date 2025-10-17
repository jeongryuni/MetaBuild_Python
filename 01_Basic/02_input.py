print("a 입력 :", end='')
a=input()
print('a', a)

b = input('b 입력 :' )
print('b', b)

# 10 + 20 = 30
a = int(a)
b = int(b)
print('a+b=:',a+b)

c = int(input('정수 c 입력:'))
print(c)
d = float(input('float d 입력:'))
print(d)

print('나이는 10살이고 키 123.4')

age = int(input('나이 :'))
height = int(input('키 :'))
print("1) 나이는 {}살이고 키는 {}입니다.".format(age, height))
print("2) 나이는 {0}살이고 키는 {1}입니다.".format(age, height))
print("3) 나이는 {1}살이고 키는 {0}입니다.".format(age, height))
print("3) 나이는 {a}살이고 키는 {h}입니다.".format(a=age, h=height))
print(f"4) 나이는 {age}살이고 키는 {height}입니다.")


