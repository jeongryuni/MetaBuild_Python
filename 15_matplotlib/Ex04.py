import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

x = [[1, 2, 3, 4, 5], [30, 25, 20, 15, 10], [2005, 2010, 2015, 2020, 2025]]
y = [2, 3, 5, 7, 11]
x_labels = ['방개수', '위치(도보 시간)', '신축 년도']
y_label = '가격'

colors = ['r', 'g', 'b']

plt.figure(figsize=(15, 4))
for i in range(len(x)):
    plt.subplot(1, len(x), i + 1)
    plt.plot(x[i], y, color=colors[i], marker='o')
    plt.xlabel(x_labels[i])
    plt.ylabel(y_label)
    y_max = max(y)
    y_min = min(y)
    plt.ylim(y_min-1, y_max+1)
    plt.title(f"{x_labels[i]}와 {y_label}")

plt.savefig('Ex04_house_price.png')
plt.show()