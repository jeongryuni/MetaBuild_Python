from wordcloud import WordCloud
import matplotlib.pyplot as plt

test = "구름 구름 파이썬 파이썬 테스트 테스트 데이터 데이터 데이터 데이터 "
wc = WordCloud(
    width=800,
    height=600,
    background_color='white',
    font_path="c:\Windows\Fonts\malgun.ttf",
).generate(test)

plt.imshow(wc)
# plt.axis("off") # 작성하지 않으면 눈금나옴
plt.show()