import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
from pandas import DataFrame

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

col = ['국어','영어','수학']
idx = ['웬디','슬기','조이']
data =[
    [40,50,50],[70,50,20],[20,20,20]
]
df = DataFrame(data, index=idx, columns=col)

# 1. 막대그래프
# df.plot(kind='bar')
# df.plot.bar()
df.T.plot.bar() # 칼람, 인덱스 전치

# 2. 가로막대 그래프
# df.plot.barh()
# df.plot.barh(stacked=True) # 누적막대그래프
#
plt.xticks(rotation=0) # x축 각도 돌리기
plt.show()
