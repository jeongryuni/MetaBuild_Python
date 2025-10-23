title_dict = {}
while True:
    print("----- Menu Select -----")
    print(
        "1. 전체 조회\n"
        "2. 추가\n"
        "3. 수정\n"
        "4. 삭제\n"
        "0. 종료\n"
    )
    try:
        choice_num = int(input("번호 선택 :"))
        if choice_num not in (0, 1, 2, 3, 4):
            raise IndexError
    except ValueError:
        print("다시 입력하세요.")
    except IndexError:
        print("0 ~ 4사이 입력하세요")
    else:
        # 전체조회
        if choice_num == 1:
            try:
                if len(title_dict) == 0:
                    raise IndexError
            except IndexError:
                print("추가된 내용이 없습니다.")
                print()
            else:
                print("----- 전체 조회 -----")
                print("제목\t:\t 가격")
                for t, p in title_dict.items():
                    print(f"{t}\t:\t {p}")
                print("--------------------")
                print()

        # 추가
        if choice_num == 2:
            print("2. 추가")
            while True:
                try:
                    title = input("제목 :")
                    if len(title) < 3 or len(title) >6 :
                        raise ValueError
                except ValueError:
                    print("3~5글자 입력하세요")
                    continue
                else:
                    while True:
                        try:
                            price = int(input("가격 :"))
                        except ValueError:
                            print("가격은 숫자로 입력하세요")
                            continue
                        else:
                            title_dict[title] = price
                            print("추가가 완료되었습니다.")
                            print()
                            break
                    break

        # 수정
        if choice_num == 3:
            print("3. 수정")
            while True:
                try:
                    target_title = input("수정할 제목 입력 :")
                    if len(target_title) < 3 or len(target_title) >6:
                        raise ValueError
                    if target_title not in title_dict:
                        raise IndexError
                except ValueError:
                    print("제목은 5글자 미만 작성")
                except IndexError:
                    print("존재하지 않는 제목입니다")
                else:
                    print("찾음!!")
                    break
            while True:
                try:
                    modify_price = int(input("가격 수정 :"))
                except ValueError:
                    print("숫자로만 입력하세요")
                else:
                    title_dict[target_title] = modify_price
                    print("가격 수정 완료!!")
                    print()
                    break

        # 삭제
        if choice_num == 4:
            print("4. 삭제")
            while True:
                try:
                    if len(title_dict) == 0:
                        raise IndexError
                except IndexError:
                    print("삭제할 내용이 없습니다.")
                    print()
                    break

                try:
                    del_title = input("삭제할 제목 입력 : ")
                    if del_title not in title_dict:
                        raise ValueError
                except ValueError:
                    print("존재하지 않는 제목입니다. 다시 입력해주세요")
                else:
                    del title_dict[del_title]

                    print(f"{del_title}가 삭제 되었습니다.")
                    print()
                    break

        # 종료
        if choice_num == 0:
            print("종료합니다")
            break

