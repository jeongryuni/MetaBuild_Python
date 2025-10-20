person = {
            "kim": {"나이":20, "주소":"서울",},
            "hong": {"나이":30, "주소":"부산"}
          }
print(person)

for k,v in person.items():
    for i,j in v.items():
        print(k,i,j)