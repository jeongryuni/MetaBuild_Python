import json

import pandas as pd

d = {
    "name": "아이유",
    "age": 40,
    "address":
        {"city" : "서울", "gu" : "종로구"}
}

print("name:",d['name'])
print("age:",d['age'])
print("address:",d['address'])
print("city:",d['address']['city'])
print("gu:",d['address']['gu'])
print("-------------------------------------")

fr = open("jumsu.json","r",encoding="utf-8")
readString = fr.read()
print(readString)
print(type(type(readString))) #str
fr.close()
print("-------------------------------------")

# 문자열 ==> dict로 변환 (josn.loads)
jsonData = json.loads(readString)
print(jsonData)
print(type(jsonData)) # list

print("----------------jsonData 전체 출력------------------")
for person in jsonData:
    # print(person)
    for i in person:
        print(i, ":", person[i])
print("----------------jsonData key, value 출력------------------")
for person in jsonData:
    for key,value in person.items():
        print(key,":",value)
    print()

print("-------------------------------------")
totalList = []
for person in jsonData:
    total_score = int(float(person['kor']) + float(person['eng']) + float(person['math']))

    gender = "남자"
    if person["gender"] == "F":
        gender = "여자"

    t = (
        person['name'],
        person['kor'],
        person['eng'],
        person['math'],
        total_score,
        gender
    )

    totalList.append(t)
print(totalList)

