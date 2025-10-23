title_dict = {}

while True:
    try:
        title = input("제목 입력:")
        if len(title) <3:
            raise ValueError
    except ValueError:
        print('제목은 3~5글자로 입력하세요')
        title = input("제목 입력:")

    while True:
        try:
            price = int(input("가격 입력:"))
        except ValueError:
            print('숫자로만 입력하세요')
        else:
            title_dict[title] = price
            break
    go = input("y/n")
    if go == "n":
        break


print(title_dict)