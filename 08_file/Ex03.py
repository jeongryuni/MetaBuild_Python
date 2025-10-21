f = open('gugudan.txt', 'w')
for i in range(1,10):
    f.write(f"3 * {i} = {3 * i} \n")
f.close()

print("-----console에 구구단 출력1 : read(전체 읽기)-----")
f = open('gugudan.txt', 'r') #기본값 'r'
read_dan = f.read()
print(read_dan)
print(type(read_dan)) # <class 'str'>
f.close()

print("-----console에 구구단 출력2 : readline(한줄 읽기)-----")
f = open("gugudan.txt", "r")
while True:
    line = f.readline()
    if line == '':
        break
    print(line, end='')
print(type(line)) # <class 'str'>
f.close()

print("-----console에 구구단 출력3 : readlines(가지고 온 전체내용 리스트로 가지고옴)-----")
f = open("gugudan.txt", "r")
lines = f.readlines()
print(lines)
print(type(lines)) # <class 'list'>

f.seek(0)
for line in f.readlines():
    print(line, end='')
f.close()