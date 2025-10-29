import random

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib import font_manager
from matplotlib import colormaps
from matplotlib.lines import lineStyles
import seaborn as sns

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False # '-' 깨짐방지
print(colormaps)

data = np.array([
            [1,5,10],
            [2,6,12],
            [3,7,15]
        ])
plt.figure(figsize=(6,4))
sns.heatmap(data=data, annot=True, cmap='RdYlGn')
plt.title('Heatmap Chart')
plt.show()

print("-----------------")
# 0 ~ 99 정수 5행 5열
arr = np.random.randint(0,100, (5,5))
plt.figure(figsize=(6,4))
sns.heatmap(data=arr, annot=True, cmap='YlGn')
plt.title('Heatmap Chart')
plt.show()

print("-----------------")
col = ['국어', '영어', '수학', '과학']
arr2 = np.random.randint(0,100, (4,4))
idx = ['홍길동', '김나비', '이영희', '김춘배']
df = pd.DataFrame(arr2, index=idx, columns=col)
plt.figure(figsize=(6,4))
sns.heatmap(data=df, annot=True, cmap='magma')
plt.title('Heatmap Chart')
plt.show()

print("-----------------")
plt.figure(figsize=(6,4))
sns.heatmap(data=arr2, annot=True, cmap='winter', linewidths=.5, cbar_kws={'label':'점수'})
plt.title('Heatmap Chart')
plt.show()