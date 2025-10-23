print("-------------ValueError--------------")
try:
    a = int(input('숫자1 :'))
    b = int(input('숫자2 :'))
except ValueError:
    print("숫자로 입력하세요")
else:
    print("a+b = ", a + b)

print("-------------FileNotFoundError--------------")
try:
    fr = open("a.txt", "r", encoding="utf-8")
    read = fr.read()
except FileNotFoundError:
    print("FileNotFoundError 발생")
    fw = open("a.txt", "w", encoding="utf-8")
    fw.write("Hi")
    fw.close()
else:
    print(read)
    fr.close()

print("-------------에러 강제로 발생시키기--------------")
try:
    c = int(input('숫자1 :'))
    d = int(input('숫자2 :'))

    if c<0 or d<0 :
        raise ArithmeticError("두 수 중 하나 음수")

except ArithmeticError as ae:
    print("음수 입력됨=>", ae)
else:
    print("두 수 모두 양수 입력됨")


