import pprint
import re
L = ['ab123', 'cd456', 'xy789', '12ef345qw', 'abc12']

# 문자열2개 + 숫자3개
#  ^            : 문자열의 시작을 의미
#  [a-zA-Z]{2}  : 알파벳 대소문자 2개 (예: ab, CD)
#  \d{3}        : 숫자 3개 (예: 123, 456)
#  $            : 문자열의 끝을 의미
regex = '^[a-zA-Z]{2}'+'\d{3}$'
pattern = re.compile(regex)


print("="*10,"match","="*10)
#  match : 문자열의 처음부터 정규식 패턴이 일치해야 매치됨.
for item in L:
    if pattern.match(item):
        print(f"패턴 일치: {item}")
        print(pattern.match(item).start(), pattern.match(item).end())
    else:
        print(f"패턴 불일치: {item}")


print("="*10,"search","="*10)
# search : 문자열 전체에 패턴이 한 번이라도 등장하면 매치됨.
for item in L:
    if pattern.search(item):
        print(f"패턴 일치: {item}")
        print(pattern.search(item).start(), pattern.search(item).end())
    else:
        print(f"패턴 불일치: {item}")


print("="*10, "a 숫자 3개 이상인.txt","="*10)
# a 숫자 3개 이상인.txt
L = ['a.txt', 'a12.txt', 'a123.txt', 'a12345.txt']

# a 숫자 3개 이상인.txt
regex = '^[a]'+'\d{3,}.txt$'
pattern = re.compile(regex)

for item in L:
    if pattern.search(item):
        print(f"패턴 일치: {item}")
    else:
        print(f"패턴 불일치: {item}")


print("="*10, "fullmatch","="*10)
# + : 1 ~ 무한대 일치
# ? : 없거나 하나 일치
# * : 0 ~ 무한대 일치

L = ['hello!', 'hello안녕~', '하하하', '안녕^^', '반갑습니다.', '또 만나요', '파이썬', 'grape#*']
regex = '^[가-힣]+$'
result = [word for word in L if re.fullmatch(regex, word)]
print(result)

print("="*30)
print(re.findall('[가-힣]+', '안녕123 하세요!!! hello~~~'))
print(re.sub('\s+', ' ', '   안녕        하세옹~~~ 까꿍   ')) # \s 공백 여러개를 만나면 하나로 공백 한칸으로 바꾸기

print("="*30)
mailList = ['abc@naver.com', 'xya@daum.net', 'qwer@google.com']
# @ 기준 앞 아이디 뒤 메일
userList = []
for mail in mailList:
    user, domain = re.split("@", mail)
    userList.append(f"아이디:{user}, 도메인:{domain}")

for info in userList:
    print(info)

print("="*30)

text = '홍길동, 30세'
pattern = re.compile('(.+),\s(\d+)세')
match = pattern.fullmatch(text)
if match:
    print(f"이름 : {match.group(1)}")
    print(f"나이 : {match.group(2)}")

print("="*30)
address = "서울특별시 강남구 역삼동 123-45"
pattern = re.compile(r'(.+시)\s(.+구)\s(.+동)\s(\d{3}-\d{2})')
match = pattern.fullmatch(address)
if match:
    print(f"{match.group(0)}\n"
          f"시 :{match.group(1)}\n"
          f"구 :{match.group(2)}\n"
          f"동 :{match.group(3)}\n"
          f"번지: {match.group(4)}")


print("="*30)
text = "오늘은 2025-10-23 입니다."
pattern = re.compile(r'(.+)\s(\d{4})-(\d{1,2})-(\d{1,2})\s(.+)')
match = pattern.search(text)
if match:
        today=match.group(1)
        year=match.group(2)
        month=match.group(3)
        day=match.group(4)
        string=match.group(5)

        print(f"{today} {year}년 {month}월 {day}일 {string}")

print("="*30)
# 전지현 - 합계 : 253
# 김혜수 - 합계 : 174
# 공유 - 합계 : 277

fr = open("a.txt", encoding="utf-8", mode="r")
lines = fr.readlines()

for line in lines:
    pattern = re.compile(r'(.+)\s(\d{2})\s(\d{0,})\s(\d{0,})')
    match = pattern.search(line.strip())

    if match:
        sum1 = int(match.group(2))
        sum2 = int(match.group(3))
        sum3 = int(match.group(4))

        total = sum1 + sum2 + sum3

        print(f"{match.group(1)}:{total}")


