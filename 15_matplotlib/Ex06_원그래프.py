import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

slices = [1, 2, 3, 4]
hobbies = ["공부", "게임", "영화 감상", "운동"]
colors = ["#FFB6B9", "#FAE3D9", "#BBDED6", "#8AC6D1"]
plt.title("취미 비율")

# startangle : 각도 틀기
# explode : 수치만큼 파이에서 나오게 하기
plt.pie(slices,
        labels=hobbies,
        colors=colors,
        startangle=90,
        shadow=True,
        explode=(0.2,0,0,0),
        autopct='%1.2f%%',
        )
plt.legend(loc=1)
# 1:우상 2:좌상 3:좌하 4:우하 10:정중앙 0:bset
plt.show()