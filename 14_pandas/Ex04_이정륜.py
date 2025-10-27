import pandas as pd

# 생성1
d = {
    "도서명":
         ["파이썬 입문","데이터 사이언스","머신러닝 완벽 가이드","딥러닝 실습","웹 개발 기본"],
     "저자":
         ["김철수","이영희","박민수","정소영","최민호"],
     "출판연도":
         [2018,2020,2019,2021,2017],
     "가격":
         [30000,45000,50000,55000,35000],
     "판매부수":
         [1500,1200,800,600,2000]
}
df = pd.DataFrame(d)

# 생성2
col = ['도서명', '저자', '출판연도', '가격', '판매부수']
data = [
    ['파이썬 입문', '김철수', 2018, 30000, 1500],
    ['데이터 사이언스', '이영희', 2020, 45000 , 1200],
    ['머신러닝 완벽 가이드', '박민수', 2019, 50000, 800],
    ['딥러닝 실습', '정소영', 2021, 55000, 600],
    ['웹 개발 기본', '최민호', 2017, 35000, 2000]
]

# df = pd.DataFrame(data, columns=col)


# 1. 인덱스 지정 후:
df.index = ["B1", "B2", "B3", "B4", "B5"]
print("1. 인덱스 지정 후")
print(df)
print()

# 2. 카테고리 컬럼 추가
df["카테고리"] = ['프로그래밍', '데이터', 'AI', 'AI', '웹']
print("2. 카테고리 컬럼 추가")
print(df)
print()

# 3. 인덱스 'B3'제거
df_drop_B3 = df[df.index!="B3"]
print("3. 인덱스 'B3'제거")
print(df_drop_B3)
print()

# 4. 저자 열 제거
df_drop_col = df.drop(columns="저자", axis=1)
print("4. 저자 열 제거")
print(df_drop_col)
print()

# 5. 인덱스 'B5'와 '판매부수' 열 동시 제거
df_multi_drop = df.drop(columns="판매부수", index="B5")
print("5. 인덱스 'B5'와 '판매부수' 열 동시 제거")
print(df_multi_drop)
print()

# 6. 2019년 이후 출판된 도서
df_2019 = df[df["출판연도"]>=2019].reset_index(drop=True)
print("6. 2019년 이후 출판된 도서")
print(df_2019)


# 7. 총 매출 컬럼 추가
df["총매출"] = df["가격"] * df["판매부수"]
print("7. 총 매출 컬럼 추가")
print(df)
print()

# 8. 가격내림차순 상위 3권
df_sort_price = df.sort_values(by="가격", ascending=False).iloc[0:3]
print("8. 가격내림차순 상위 3권")
print(df_sort_price)