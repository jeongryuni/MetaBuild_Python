# 연도에 해당하는 txt 파일 생성
fr = open("member.txt", 'r')
lines = fr.readlines()
for line in lines:
    arr = line.split(",")
    year = arr[1].split("-")[0]

    fw = open(f"{year}.txt",'a')
    fw.write(line)
