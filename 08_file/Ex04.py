fr = open("sungjuk.txt", 'r')
fw = open("sungjuk_result.txt", 'w')

line = fr.readline()
fw.write(line)
pos = fw.tell() # 위치알기
# print(pos) # 38 <맨끝 엔터친후 아래
fw.seek(pos-2) # enter = 2칸
fw.write("\t합계\n")

lines = fr.readlines()
for line in lines:
    total=0
    arr = line.split()

    for i in range (1, len(arr)):
        total += int(arr[i])
    fw.write(line)
    pos = fw.tell()
    fw.seek(pos - 2)
    fw.write("\t"+str(total)+"\n")

fr.close()
fw.close()

