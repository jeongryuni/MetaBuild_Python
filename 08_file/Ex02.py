import os
from os import remove

print(os.getcwd())

#w : 없으면 생성/ 존재하면 내용을 비운 후 작성가능 (작성용도)
#a : 없으면 생성/ 존재하면 그대로 냅둠 (내용 비움x)
# open("test.txt", "w")
f = open("test.txt", "a", encoding="utf-8")
f.write("안녕하세용~~\n")
f.close()

with open("test.txt", "w", encoding="utf-8") as f:
    f.write("애옹~~~~\n")
    f.write("애옹애옹!!!\n")
    f.write("hello!!!\n")
    # 자동 close

# close 이후 같은 변수 사용 가능
f = open("test.txt", "r", encoding="utf-8")
pos = f.tell()
print('pos:', pos) #파일 포인터위치
s = f.read()
print(s)

pos2 = f.tell()
print('pos:', pos2) #파일 포인터위치
f.seek(10) # 파일포인터 위치 변경 (1)
s = f.read()
print(s)

f.close()

