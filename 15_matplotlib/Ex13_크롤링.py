from Tools.scripts.dutree import display
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager
from matplotlib.lines import lineStyles

font_location = 'c:/Windows/fonts/malgun.ttf'
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
plt.rcParams['axes.unicode_minus'] = False # '-' 깨짐방지
from bs4 import BeautifulSoup
import urllib.request

url= 'https://search.naver.com/search.naver?where=nexearch&sm=tab_etc&qvt=0&query=%EB%B0%95%EC%8A%A4%EC%98%A4%ED%94%BC%EC%8A%A4'
soup = BeautifulSoup(urllib.request.urlopen(url).read(), 'html.parser')
movieList = [] #영화 제목
gradeList =[] # 평점

name = soup.find_all('strong', 'name')
for item in name:
    movieList.append(item.get_text())

print(movieList)
# sub_text
sub_text = soup.find_all("span", class_="sub_text")

# 내부 텍스트 중 숫자만 가져오기
for g in sub_text:
    if '명' not in g.get_text():
        gradeList.append(float(g.get_text()))


movie = dict(zip(movieList[:5], gradeList[:5]))
plt.figure(figsize=(15, 5))
plt.bar(movie.keys(), movie.values(), width=0.8, align='center', alpha=0.7)
plt.ylim(min(movie.values())-0.05, max(movie.values())+0.02)
plt.xticks(rotation=20, ha='right')   # 글자를 20도 기울이고 오른쪽 정렬
plt.tight_layout()                    # 여백 자동 조정

plt.show()


