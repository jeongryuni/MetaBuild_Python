x = 3
y = 0
L = [1,2,3]

try:
    #print(x/y) # ZeroDivisionError : 0으로 못나눔
    print(L[3]) # IndexError : 없는 인덱스
    print('a'+2) # TypeError
    print(int('a')) # ValueError

except ZeroDivisionError:
    print("ZeroDivisionError 발생!!")
except IndexError:
    print("IndexError 발생!!")
except TypeError:
    print("TypeError 발생!!")
except ValueError:
    print("ValueError 발생!!")
finally:
    print("finally!!")


print("------------Exception-------------")
# Exception : 모든 에러 처리
try:
    print(x/y)

except Exception as e:
    print("오류 발생!!", e)
    print("Exception!!")
finally:
    print("finally!!")

print("------------else-------------")
# else : 처리할 에러가 없을떄 else ㅊ출력
try:
    print("Hi")
except Exception as e:
    print(e)
else:
    print("else!! 오류없어용~")
finally:
    print("finally!!")