import pandas as pd
from pandas import to_datetime

mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드', \
            'TCS하이패스구분코드', '1종교통량', '2종교통량', \
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량']

filename = "capital_area.csv"
df = pd.read_csv(filename, sep='|', header=None, names=mycolumn, index_col=False)

# 영업소코드 출력
df_code = df[["영업소코드"]]
print("1. 영업소코드 출력")
print(df_code)
print()

# 여러개 컬럼 가져오기
df_code2 = df[["영업소코드", "1종교통량", "총교통량"]]
print("2. 여러개 컬럼 가져오기")
print(df_code2)
print()

# groupby('영업소코드')
my_group = df.groupby(['영업소코드'])
my_group_sum = my_group.sum()
print()

# 영업소코드별로 총교통량 합계
my_group_total = df.groupby('영업소코드')['총교통량'].sum()
print("3. 영업소코드(groupby) 총교통량 합계")
print(my_group_total)
print()

# 영업소코드별로 1종, 2종, 총교통량 합계
my_group_sum_total = df.groupby('영업소코드')[['1종교통량', '2종교통량', '총교통량']].sum()
print("4. 영업소코드(groupby) 1종, 2종, 총교통량 합계")
print(my_group_sum_total)
print()

# 영업소코드190 입출구 구분코드 1
# df_cond = df.loc[(df["영업소코드"]==190) & (df["입출구구분코드"]==1)]
df_cond = df[(df["영업소코드"]==190) & (df["입출구구분코드"]==1)]
print("5. 영업소코드190 입출구 구분코드 1인 데이터")
print(df_cond)
print()

# 1종 교통량 가장 큰값, 가장 작은값
df_max = df['1종교통량'].max()
df_min = df['1종교통량'].min()
print('df_max:\n',df_max)
print('df_min:\n',df_min)
print()

# 영업소 코드별로 1종 교통량, 2종교통량 가장 큰값
df_cond = df.groupby('영업소코드')['1종교통량'].max().reset_index().iloc[0]
print("6. 영업소 코드별로 1종 교통량, 2종교통량 가장 큰값")
print(df_cond)
print()

# 영업소 코드별로 1종 교통량, 2종교통량 가장 큰값, 작은값 (agg(['max', 'min']))
print("7. 영업소 코드별로 1종 교통량, 2종교통량 가장 큰값, 작은값")
df_agg_max_min = df_group = df.groupby('영업소코드')[['1종교통량', '2종교통량']].agg(['max','min']).reset_index().iloc[0]
print(df_agg_max_min)
print()

# 1종 교통량 min값만 가져오기
print("8. 1종 교통량 min값만 가져오기")
print(df_agg_max_min['1종교통량']['min'])
print()

# 집계일자 별로 총교통량 평균
df_mean = df.groupby('집계일자')['총교통량'].mean().reset_index()
print("9. 집계일자 별로 총교통량 평균")
print(df_mean)
print()

# 집계일자 집계시 별로 총 교통량 평균
df_hour = df.groupby(['집계일자','집계시'])[['총교통량']].sum()
print(df_hour)
print()

# 집계시 7~9시 별로 총교통량 합계
df_filter = df[(df["집계시"] >= 7) & (df["집계시"] <= 9)]
groupDay = df_filter.groupby(['집계일자',"집계시"])['총교통량'].sum()
print('groupDay:\n',df)

# groypDay결과에서 20230201만 가져오기
groupDay_reset_index = groupDay.reset_index()
groupDay_day = groupDay_reset_index.loc[df['집계일자'] == 20230201]
print('df:\n',groupDay_day)
print()
# 인덱스로만 가져오기
print(groupDay.loc[20230201, 8])
print()

print("-----------------------------")
# 집계일자별로 총교통량의 합계가 800000이 넘는 데이터 조회
# df = df.groupby('집계일자')['총교통량'].sum().reset_index()
# cond = df[df['총교통량']>= 800000]
# print(len(cond)) # 0

groupDay = df.groupby('집계일자')['총교통량'].sum()
groupOver = groupDay[groupDay > 800000]
print('groupOver:\n',groupOver)
print()