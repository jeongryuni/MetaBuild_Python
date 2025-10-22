import json
from datetime import datetime

fr = open("humans.json", "r", encoding="utf-8")
readString = fr.read()
data = json.loads(readString)

# 튜플에 담기
totalList = []
for human in data:
    blood = "O형"
    if human["blood"] == "A":
        blood = "A형"
    elif human["blood"] == "B":
        blood = "B형"
    elif human["blood"] == "AB":
        blood = "AB형"

    print(human["ssn"].split("-")[0][:2])
    now_year = datetime.now().year
    year = int(human["ssn"].split("-")[0][:2])
    age = 0
    if  year >= 50:
        age = now_year - int("19" + str(int(year)))
    elif year < 50:
        age = now_year - int("20" + str(int(year)))

    if human["ssn"].split("-")[1][:1] == "1" or "3":
        gender = "남자"
    else:
        gender = "여자"

    t = (
        human["name"],
        age,
        human["hobby"],
        human["address"],
        blood,
        human["ssn"],
        gender,
    )
    totalList.append(t)
    print(totalList)

