import pandas as pd

df = pd.read_csv('movies.csv')
print(df)
print()

# 1. 장르별로 평균 내기
df1 =  df.groupby('장르')['평점'].mean()
print("1. 장르별로 평균 내기")
print(df1)
print("-"*30)


# 2. 감독별 총 관계수
df2 = df.groupby('감독')['관객수(만)'].sum()
print("2. 감독별 총 관계수")
print(df2)
print("-"*30)

# 3. 장르별 평균 통계
df3 = df.groupby(['장르']).agg({"평점": "mean", "관객수(만)": "sum"})
print("3. 장르별 평균 통계")
print(df3)
df3.to_csv('Ex08_df3.csv', index=False)
print("-"*30)

# 4. 감독 + 장르별 평균 요약
df4 = df.groupby(['감독', '장르'])[['평점', '관객수(만)']].mean()
print("4. 감독+장르별 평균 요약")
print(df4)