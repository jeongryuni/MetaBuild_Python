import pandas as pd
import numpy as np

data = [100, 200, 300, 400]
columns = ['국어', '영어', '수학', '과학']
score = pd.Series(data, index=columns)
print(score)


# 수정/추가
score['과학'] = 450
score['미술'] = 250
print("수정/추가")
print(score)
print()

# 300이상 출력
cond = score[score>=300]
print("300이상 출력")
print(cond)
print()
# 200 ~ 400
cond = score[(200<=score) & (score<=400)]
print("200 ~ 400")
print(cond)
print()

# 인덱스 기준 정렬
index_sort = score.sort_index()
print("index_sort")
print(index_sort)
print()

# value 내림차순 정렬
sort_value = score.sort_values(ascending=False)
print("sort_value")
print(sort_value)

subject = ['국어', '영어', '체육']
s2 = score.reindex(subject, fill_value=0) #nan값 0으로 채우기
print(s2)
print()

# 최대값, 최소값, 합계, 평균
print("최대값:", np.max(score))
print("최소값:", np.min(score))
print("합계", np.sum(score))
print("평균", np.mean(score))
print()

print(score.ndim, score.shape)

