import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

x1 = [1,2,3,4]
y1 = [3,7,6,4]
x2 = [1,2,3,4]
y2 = [4,6,8,5]

y_max = max(max(y1), max(y2)) #8
y_min = min(min(y1), min(y2)) #3

plt.subplot(2,1,1) # 2행1열 1번쨰칸
plt.plot(x1, y1, 'yo-') # 선 색상:yellow/실선/마커o
plt.xlabel('x1축')
plt.ylabel('y1축')
plt.title('그래프 예제')

plt.subplot(2,1,2) # 2행1열,2번쨰칸
plt.plot(x2, y2, 'r.--') # 선 색상:red/점선/마커 점
plt.xlabel('x2축')
plt.ylabel('y2축')
plt.ylim(y_min-1,y_max+1)
plt.show()
