import pandas as pd

col = ('이름', '나이')
enc = "utf-8"
data = [('유재석', 50),('송은이', 30)]

df = pd.DataFrame(data, columns = col)
print("---------------DataFrame생성---------------")
print(df)
print()

print("---------------csv 파일 생성---------------")

filename = "result.csv"
df.to_csv(filename, encoding=enc, index = False, mode='w')
print("csv파일 쓰기 완료!!")
print()

print("---------------csv 파일 불러오기---------------")
df = pd.read_csv(filename, encoding=enc)
print(df)
print()

# index=False : 인덱스를 파일에 저장하지 않음 (인덱스 열이 제외됨)
# index=True  : 인덱스를 파일에 함께 저장함 (인덱스 열이 포함됨)
df2 = pd.read_csv(filename, encoding=enc, index_col=0)
print(df2)
print()

