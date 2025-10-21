import os

print(os.getcwd()) # 현재위치
#os.chdir("./../") # 직접 경로 적기
print(os.listdir('.')) # .상위파일
print(os.listdir('..')) # ..상위파일

# 파일 이름 바꾸기 : rename
# os.rename('a.txt', 'c.txt')
# os.rename('c.txt', 'my/d.txt') # c.txt => my 폴더의 d.txt로 변경

# os.rename('b.txt')
# os.remove('my') # 폴더안에 파일이 있으면 삭제불가

import shutil
# shutil.rmtree('my') # 폴더안에 파일이 있어도 삭제 가능
shutil.copy('b.txt', 'a.txt')

