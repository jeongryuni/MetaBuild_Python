L=[10,20,30]

L.insert(2,25) # 2번 인덱스에 25추가

# 추가 방법
# L[4] = 44
# L[4:4] = [44]
# L.insert(3, 44)
# L.append(44) # 맨끝에 추가
# print(L)

# 숫자 5개 입력받아 넣기
L =[]
for i in range(5):
    num = int(input("숫자 입력: "))
    L.insert(i,num)
    # L2+=[num]
print(f"숫자 5개 입력받아 넣기 L : {L}")

print(f"L 처음만나는 32의 인덱스: {L.index(32)}")
L.remove(32) # 처음만나는 32 삭제

L.sort(reverse=True) # sort() 적용된 리스트 (원본 변경됨) -- 내림차순
L2 = sorted(L, reverse=True) # sorted() 결과 (새로 만든 리스트) -- 내림차순

print("L", L)
print("L2", L2)

L = ['blueberry', 'apple', 'Grape', 'banana']
L.sort()        # 기본 오름차순 정렬 (대문자 우선) 아스키 순서정렬
print("L", L)

L=['2123','456','789']
L.sort() # L ['123', '456', '789']
print("L.sort()", L)

L.sort(reverse=True, key=int)
print("L.sort(reverse=True, key=int)", L)

L.clear()
del L