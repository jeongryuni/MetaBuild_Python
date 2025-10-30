from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re

# 형태소별로 분석
# 만약 konlpy가 에러가 날 경우
# 1. JAVA_HOME 환경변수 설정
# 2. VC_redist.x64 설치

from konlpy.tag import Okt

with open('file/news.txt', encoding='utf-8') as f:
    text = f.read()

# 한글만 가져오기 (한글이 아닌것 공백)
text = re.sub('[^가-힣\s]','',text) # 정규표현식 작성, 바꿀문자, 대상문자열

#객체생성 (행태소분석)
okt = Okt(jvmpath="C:/Program Files/Java/jdk-17/bin/server/jvm.dll")
# print(okt.pos('이날 오전 9시 24분 기준 코스피는 전장보다 79.57포인트(2.02%) 오른 4,021.16이다.'))

nouns = okt.nouns(text)
print('nouns:')
print(nouns)

wc = WordCloud(
    width=800,
    height=600,
    background_color='white',
    font_path="c:\Windows\Fonts\malgun.ttf",
    ).generate(text)

plt.imshow(wc)
plt.axis('off')
plt.show()

