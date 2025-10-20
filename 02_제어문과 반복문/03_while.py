total=0
i=0
while i<11:
    total += i
    i += 1
print(total)

print("----------")
while True:
    if i>5:
        break
    i+=1

print("----------")
sum = 0
count=0
while True:
    score = int(input('점수 입력'))
    if score >= 0:
        sum += score
        count+=1

    elif(score < 0):
        break
avg = sum/count
print('{:2f}'.format(avg))
print('%.2f' %avg)
print(f"합: {sum}, 평균 :{int(sum/(count))}, ronud평균: {round(avg, 2)}, 평균.2f: {avg:.2f}")