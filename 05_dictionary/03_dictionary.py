person = {}
while True:
    name = input("이름 입력 :")
    name = name.lower()
    if name == "quit":
        break
    age = int(input("나이 입력 :"))
    person[name] = age
print(person)

# 나이 합계
age_sum = sum(person.values())
print(age_sum)

# 이름 검색 : bb
# 찾는 나이 33

while True:
    find_name = input("이름 입력 : ")
    if(find_name == "stop"):
        break
    find_name = find_name.lower()
    if find_name in person:
        print(f"{find_name}의 나이는 {person[find_name]} 입니다.")
    else:
        print("존재하지 않는 사람")
