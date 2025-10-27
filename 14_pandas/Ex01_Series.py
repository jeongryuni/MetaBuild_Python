import pandas as pd
import numpy as np

arr = np.array([10, 20, 30, 40, 50])
print(arr)

# pd.Series : 1차원 배열 구조
s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)
print(s1[4])
print("type(s1):", type(s1))
print(s1[0])  # 10
print(s1.index)
print(s1.values)
print()

# pd.Series : 인덱스를 지정한 1차원 배열 구조
s1 = pd.Series([10, 20, 30, 40, 50], index=['정륜', '춘배', '애옹', '김정륜', '김애옹'])
print(s1)
print("type(s1):", type(s1))
print('s1["정륜"]:', s1["정륜"])          # 10
print('s1[["정륜"]]:', s1[["정륜"]])      # 정륜    10
print(s1.index)                           # Index(['정륜', '춘배', '애옹', '김정륜', '김애옹'], dtype='object')
print(s1.values)                          # [10 20 30 40 50]

s1["춘배"] = 50   # 존재하는 인덱스 : 값 변경
s1["나비"] = 70   # 존재하지 않는 인덱스 : 새로운 값 추가

print("s1[['춘배', '나비']] :\n", s1[['춘배', '나비']])
print("==========================")

print(f"1. ", s1.values < 50)
print()
print(f"2.\n", s1[s1.values < 50])
print()
print(f"3.\n", s1[(s1 >= 40) & (s1 <= 60)])
print()
print("4.", s1.index == "춘배")  # Boolean 반환
print()
print("5.", s1[s1.index == "춘배"])  # 값 반환
print()
print("6.", s1 * 100)
print()
print("7.", "박춘배" in s1)  # False
print("8.", "애옹" in s1)    # True
print("9.", 7000 in s1)      # False
print("10.", 7000 in s1.values)  # False : 찾지 못함
print()

print("==========================")
d = {"서울":2000, "부산":3000, "울산":7000, "광주":5000}
print("d:", d)
s2 = pd.Series(d)
print("s2:\n", s2)

print("==========================")
city = ['부산', '울산', '목포', '서울']
s3 = pd.Series(d, index=city)
print("s3:\n", s3)
print()
print("11. ", pd.isna(s3)) # isna == isnull 같음
print("12. ", pd.isnull(s3))
print()
print("13. ", pd.notna(s3))
print("14. ", pd.notnull(s3))
print("notnull.\n", s3[pd.notnull(s3)])
print()

# nan값 넣기
s3 = pd.Series([1, np.nan, 2,3])
print("s3:\n", s3)
print()

s4 = pd.Series([1, np.nan, 2, 3])
print("s4:\n", s4)

s3 = pd.Series([1, np.nan, 2, 3], index=['서울', '부산', '울산', '광주'])
print(s2 + s3)

s1 = pd.Series([10, 20, 30, 40, 50, 60, 70], index=['a', 'b', 'c', 'd', 'e','f','g'])
s1_drop = s1.drop(['a', 'b'])
print("s1_drop:\n", s1_drop)
print()

s1 = pd.Series([10, 20, 30, 40, 50, 60, 70], index=['a', 'b', 'c', 'd', 'e','f','g'])
print('16:\n', s1[2:4])
print('17:\n', s1[3:1:-1]) # 3번인덱스 => 1까지 역으로 가져오깅
# print('18:\n', s1[[1,3]])
print('19:\n', s1.iloc[[1,3]])
print()
print("==========================")

s1 = pd.Series([70, 120, 30, 66, 50, 60, 100], index=['a', 'b', 'c', 'd', 'e','f','g'])

# index값 기준 sort
sort_index = s1.sort_index()
print("sort_index:\n", sort_index)
print()

# values 값 기준 sort
sort_values = s1.sort_values(ascending=False)
print("sort_values:\n", sort_values)

