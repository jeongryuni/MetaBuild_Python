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

plt.plot(x1,y1,label ="first line" ,color = 'red')
plt.plot(x2,y2,label ="second line" ,color = 'green', linestyle = 'dotted', marker = 'D')
plt.ylim(y_min-1,y_max+1)

plt.xlabel('x축')
plt.ylabel('y축')
plt.title("예제")
plt.legend() # 범례
plt.annotate('annotate',
             xy=(1.5, 5),
             xytext=(2,4), # 화살표 길이
             arrowprops={"color":'green'}
             ) #두 그래프 선이 만나는 지점
filename = 'brokenLines.png'
plt.savefig(filename)
print(filename+'에 저장했습니다.')
plt.show()

