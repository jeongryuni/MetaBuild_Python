su = 11
if su % 2 == 0:
    print(su, "짝수")
    print(su, "히하~")
else:
    print(su, "홀수")
    print(su, "하히~")
print('헤헤헤')

# 점수 입력
score = int(input('점수 입력:'))
if score >= 90:
    result1 = 'A'
elif score >= 80:
    result1 = 'B'
elif score >= 70:
    result1 = 'C'
else:
    result1 = 'F'

print(result1)

# 80이상 pass, fail


if score >= 80:
    result2 = 'Pass'
else:
    result2 = 'Fail'
print(result2)

result3 = 'Pass' if score >= 80 else 'Fail';
print(result3)

result4 = 'A' if score >= 90 else \
          'B' if score >= 80 else \
          'C' if score >= 70 else \
          'F'
print(result4)

result5 = ('A' if score >= 90 else
          'B' if score >= 80 else
          'C' if score >= 70 else
          'F')
print(result5)