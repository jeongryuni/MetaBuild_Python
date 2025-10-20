print("==========Ex01==========")
for i in range(1,5): # 1 ~ 4
    print(i, end="")
    print('*')

print("==========Ex02==========")
for i in range(5): # 0 ~ 4
    print(i, end="")
    print('*')

print("==========Ex03 : 1~10합계 출력 ==========")
sum = 0
for i in range(1,11):
    sum += i
print("sum :",sum)
print("sum :" + (str)(sum))
print(f"sum : {sum}")

print("==========Ex04==========")
for i in range(10,0,-1): # 10 ~  1
    print(i)

print("==========Ex05 : 1~10짝수/홀수의 합 ==========")
even  = 0
odd = 0
for i in range(1, 11, 1):
    if i % 2 == 0:
        even  += i
    else:
        odd += i
print(f"짝수 합계: {even} , 홀수 합계: {odd}")

print("==========Ex06 ==========")
for i in range(1, 11, 1):
    pass

print("==========Ex07 : break/continue ==========")
print("break : 5이상 되면 멈추기")
for i in range(1, 11, 1):
    if i > 5:
        break
    print(i)

print("continue : 5가 됐을때 5만 건너뛰기")
for i in range(1, 11, 1):
    if i == 5:
        continue
    print(i)

print("==========Ex08 : 이중for문 ==========")
for i in range(1, 4, 1):
    for j in range(5, 8):
        print(i,j)
    print("🌈")
print("🌰")

print("==========구구단==========")
for i in range(2, 10, 1):
    print(f"{i}단🌈")
    print("----------")
    for j in range(1, 10, 1):
        print(f"{i} * {j} = {i*j}")

print("==========Ex09 : 별만들기==========")
num = int(input("입력"))
for i in range(1, num, 1):
    for j in range(i):
        print("*", end="")
    print("")

