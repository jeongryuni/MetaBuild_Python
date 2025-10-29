import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager
from pandas import DataFrame
import numpy as np

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

mycolumn = ['집계일자', '집계시', '영업소코드', '입출구구분코드', \
            'TCS하이패스구분코드', '1종교통량', '2종교통량', \
            '3종교통량', '4종교통량', '5종교통량', '6종교통량', '총교통량']

filename = "file/capital_area.csv"
df = pd.read_csv(filename, sep='|', header=None, names=mycolumn, index_col=False)

df = df.groupby('영업소코드')[['2종교통량', '3종교통량', '4종교통량', '5종교통량', '6종교통량']].sum()
df.plot(kind='bar')
plt.title('영업소 코드별 교통량 합계')
plt.xlabel('종류별 교통량')
plt.ylabel('합계', rotation=90)
plt.xticks(rotation=0)
plt.show()
