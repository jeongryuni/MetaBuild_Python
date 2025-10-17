print('가', end='\n')  # 기본값 end='\n' → 줄바꿈 O
print('가나다', end='')  # end=''로 지정하면 줄바꿈 없이 다음 문장과 이어짐
print('가나다마바사')

a = 10
print(a)
print('오늘은'+'즐거운'+'금요일'+'입니다')
print('오늘은' '즐거운' '금요일' '입니다')
print('오늘은','즐거운','금요일','입니다') # 쉼표 사용 시 자동 공백 추가

print(12+34) # 46
print('12'+'34') # 1234

# type 변환
print(12+int('34')) #46
print(str(12)+str('34')) # 1234

print(type(12)) # <class 'int'>
print(type('12')) # <class 'str'>

# 숫자 출력
print("%d / %d = %d" % (10, 3, 10/3))    # 10 / 3 = 3  (소수점 이하 버림)
print("%d / %d = %f" % (10, 3, 10/3))    # 10 / 3 = 3.333333
print("%d / %d = %.2f" % (10, 3, 10/3))  # 10 / 3 = 3.33 (소수 둘째 자리까지)
print("%d / %d = %5d" % (10, 3, 10/3))   # 10 / 3 =     3 (전체 5칸 확보)

# 문자열 출력
print("%s" % "python") # python
print("#" * 3) # ###
print("@#" * 3) # @#@#@#

print(15/6) # 몫 : 2.5
print(15//6) # 몫(정수) : 2
print(15%6) # 나머지 3
print(divmod(15,6)) # (2,3) divmod반환 -> 튜플(몫,나머지)

a=5
b=10
print((0>a) or (0<b)) #True
print((0>a) and (0<b)) #False

name = "아이유"
age = 30
height = 189.2

print('이름:',name)
print('나이:',age)
print('키:',height)

