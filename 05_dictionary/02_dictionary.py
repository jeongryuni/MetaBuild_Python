mb1 = {"kim":33, "park":44, "choi":55}
mb2 = {"kim":77, "jung":88, "hong":99}

print(mb1['park'])
print(mb1.get('lee')) # 없으면 none

if mb1.get('jung') == None:
    print('jung 없음')
else:
    print('jung 있음')

# 업데이트(update)
mb1.update(mb2) # 같은 키-> 값 업데이트/ 새로운 키 -> 딕셔너리 추가
print(mb1)

# 삭제(delete)
del mb1 # 딕셔너리 {}구조도 삭제

del mb2['jung']
print(mb2)

mb2.clear() # 딕셔너리 {}구조는 남음
print(mb2)
