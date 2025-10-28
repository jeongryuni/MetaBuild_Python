import matplotlib
import matplotlib.pyplot as plt
from matplotlib import font_manager

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)

# 1. 그래프를 그릴 도화지 생성 (가로5, 세로4)
fig = plt.figure(figsize=(5, 4))

# 2. 좌표 입력
# alpha = 투명도 0에 가까울수록 투명해짐
plt.plot([1,2,3,4], [5,6,3,8], linewidth=2.5, linestyle='-', marker='o', alpha=0.5)

# 3. 그래프 출력
plt.xlabel('x축')
plt.ylabel('y축')
plt.title('matplotlib 예제')
plt.show()

