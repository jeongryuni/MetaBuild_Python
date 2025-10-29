import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.lines import lineStyles

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False # '-' 깨짐방지

y1_value = (21.6, 23.6, 45.8, 77.0, 102.2, 133.3, 327.9, 348.0, 137.6, 49.3, 53.0, 24.9) # 강수량
y2_value = (1.6, 4.1, 10.2, 17.6, 22.8, 26.9, 28.8, 29.5, 25.6, 19.7, 11.5, 4.2) #기온

x_value = np.arange(1, 13)

# 막대그래프 (강수량)
plt.bar(x_value, y1_value, width=0.5, align='center', alpha=0.7)
plt.ylabel('평균 강수량')
plt.title('Weather Chart')

plt.twinx()
# 꺾은선그래프 (기온)
plt.plot(x_value, y2_value, color='r',alpha=0.5 ,linestyle="solid", marker="o", markersize=3)
plt.ylabel('평균 기온')
plt.ylim(-40, 35)

plt.show()
