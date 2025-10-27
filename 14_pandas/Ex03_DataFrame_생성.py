import numpy as np
import pandas as pd
from Tools.scripts.dutree import display

'''
Series : 1차원
DataFrame : 2차원(행/열) 자료 구조
'''

arr = np.array([[1,2,3], [4,5,6]])
print("arr: \n", arr)
# 6출력
print(arr[1][-1])
print(arr[1][2])
print(arr[1,2])

print("-----------DataFrame-----------")
df1 = pd.DataFrame(arr)
print("df1: \n", df1)
print(type(df1),"/", df1.ndim,"/", df1.shape)
print(df1[2][1]) # df[칼럼명][인덱스명]

print("-----------DataFrame2-----------")
s1 = pd.Series([10,20,30,40])
s2 = pd.Series(['A','B','C','D'])
df2 = pd.DataFrame([s1,s2])
print("df2: \n", df2)
print()

print("-----------DataFrame3-----------")
d = {'a':[1,3], 'b':[4,7], 'c':[5,2]}
df3 = pd.DataFrame(d)
print("df3: \n", df3)

print("-----------DataFrame4-----------")
df4 = pd.DataFrame(data=[[4,5,6,7],[1,2,3,4]],
                   index=["man", "woman"],
                   columns=["A", "B", "C", "D"])
print("df4: \n", df4)
print("3 출력하기 : ",df4.loc["woman","C"])
print("3 출력하기",df4.iloc[1]["C"])
print()
print("-----------DataFrame5-----------")
data = [
    ["윤아", "영업", 5000, 2],
    ["민호", "개발", 6000, 5],
    ["혜수", "개발", 5500, 3],
    ["찬열", "영업", 5800, 4],
    ["소영", "인사", 4800, 1],
]
col = ["이름", "부서", "급여", "근속연수"]
df5 = pd.DataFrame(data, columns=col)
print("df5: \n", df5)


print("-----------DataFrame6-----------")
dict_arr={
       "이름":['윤아', '민호', '혜수', '찬열', '소영'],
        "부서": ['영업','개발', '개발', '영업', '인사'],
        "급여":[5000,6000,5500,5800,4800],
        "근속연수":[2,5,3,5,1]
}

df6 = pd.DataFrame(dict_arr)
print("df6: \n", df6)

# 연봉 계산
df6["연봉"] = df6["급여"] * 12
print("df6: \n", df6)
print()
# 이름 연봉 출력
print(df6[["이름","연봉"]])
print()
# index변경
df6.index = range(1,6)
print("df6: \n", df6)
print()
# three, 혜수 , 개발
# print(df6.iloc[2])
# print(df6[df6.index==3])
print(df6.loc[3])

# 상여금 추가
# df6["상여금"] = [300, 500, 400, 450, 200]

#인덱스를 변경했다면 시리즈로 값을 넣을떄 인덱스 지정
bonus = pd.Series([300, 500, 400, 450, 200], index=range(1,6))
df6["상여금"] = bonus

print("df6: \n", df6)
print()

# 총연봉
df6["총연봉"] = df6["연봉"] + df6["상여금"]
print("df6: \n", df6)

# 상여금이 급여의 비율 = 상여금/급여
df6["비율(상여금/급여)"] = (df6["상여금"]/df6["급여"]).round(2)
print("df6: \n", df6)

# 칼럼과 인덱스 바꾸기
# df6 = df6.transpose()
df6 = df6.T
print("df6: \n", df6)

print()
print("========================================")

# df.index = ["one", "two", "three", "four", "five"]
# df_drop = df.drop(1)
# df_drop = df.drop("two")
# print("df_drop: \n", df_drop) # 원본변경 x

df = df6.T
df = df.reset_index()
print("df: \n", df)


# 여러행 삭제
df_drop = df.drop([0,4])
print("df_drop: \n", df_drop)

# 컬럼 삭제
df_col_drop = df.drop("급여", axis=1)
print("df_col_drop: \n", df_col_drop)

# 컬럼: 급여와 근속연수 삭제
df_col_drop2 = df.drop(['급여', '근속연수'],axis=1)
print("df_col_drop2: \n", df_col_drop2)

# 1,3행 삭제, 급여컬럼 삭제
df_drop3 = df.drop(index=[1, 3], columns=["급여"])
print("df_drop3:\n", df_drop3)

# df_iloc = df.drop(index=[1,3])
# print(df_iloc)
print("------------------------------")
dict_arr={
       "이름":['윤아', '민호', '혜수', '찬열', '소영'],
        "부서": ['영업','개발', '개발', '영업', '인사'],
        "급여":[5000,6000,5500,5800,4800],
        "근속연수":[2,5,3,5,1]
}

df = pd.DataFrame(dict_arr)
print("df6: \n", df6)

# reindex
df_reindex = df.reindex([4,2,0,1,3])
print("df_reindex: \n", df_reindex)
print()

df = df.reindex(columns = ['이름', '근속연수', '급여', '부서'])
print("df_reindex: \n", df)
#
# 인사부 행 삭제
df_drop = df[df["부서"] != "인사"]
print("df_drop: \n", df_drop)

df_drop = df[df["부서"] != "개발"].reset_index(drop=True)
print("df_drop: \n", df_drop)

# 급여가 5500이상인 데이터
price_5000 = df[df["급여"]>= 5500].reset_index(drop=True)
print("price_5000: \n", price_5000)

# 근속연수 기준 내림차순 정렬
df_sort = df.sort_values(by="근속연수", ascending=False).reset_index(drop=True)
print("근속연수 기준 내림차순 정렬")
print("df_sort: \n", df_sort)

# 부서 기준 오름차순 정렬 / 급여 기준 내림차순 (중복부서가 있을경우)
df_sort = df.sort_values(by=["부서", "급여"], ascending=[True, False]).reset_index(drop=True)
print("부서 기준 내림차순 정렬")
print("df_sort: \n", df_sort)


dict_arr={
       "이름":['윤아', '민호', '혜수', '찬열', '소영'],
        "부서": ['영업','개발', '개발', '영업', '인사'],
        "급여":[5000,6000,5500,5800,4800],
        "근속연수":[2,5,3,5,1]
}


