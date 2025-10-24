book_list=[]
try:
    fr = open("Book.txt", "r", encoding="utf-8")
    lines = fr.readlines()
    if len(lines) == 0:
        raise FileNotFoundError
    fr.close()
except FileNotFoundError:
    fw = open("Book.txt", "w", encoding="utf-8")
    print("저장된 파일이 없습니다. 새로 시작합니다.")
    print()

while True:
    print("[도서 관리 시스템]")
    print(""
          "1. 도서 등록\n"
          "2. 전체 도서 보기\n"
          "3. 도서 검색\n"
          "4. 도서 삭제\n"
          "5. 도서 가격 수정\n"
          "6. 파일 저장\n"
          "7. 종료"
          )
    try:
        menu = int(input("메뉴 선택 (1~7) :"))

        if menu not in range(1, 8):
            raise IndexError
    except ValueError:
        print("숫자를 입력해주세요!!\n")
        print()
    except IndexError:
        print("1 ~ 7사이 입력!!\n")
    else:
        # 1. 도서 등록
        if menu == 1:
            print("도서 등록")
            title = input("도서 제목 : ")
            author = input("저자 : ")
            while True:
                try:
                    price = int(input("가격 :"))
                except ValueError:
                    print("가격은 숫자로 입력해야 합니다.")
                else:
                    book_list.append({"제목" :title, "저자" :author, "가격" :price})
                    print(f"도서 {title} 등록!!\n")
                    break

        # 2. 전체 도서 보기
        elif menu == 2:
            try:
                if len(book_list) == 0:
                    raise ValueError
            except ValueError:
                print("조회할 도서가 없습니다.\n")
                continue

            else:
                print("----------도서 전체 조회----------")
                for book in book_list:
                    print(f'제목:{book["제목"]}\t| 저자:{book["저자"]}\t| 가격:{book["가격"]}')
                print("--------------------------------")

        # 3. 도서 검색
        elif menu == 3:
            found = False
            print("도서 검색")
            try:
                if len(book_list) == 0:
                    raise ValueError
            except ValueError:
                print("조회할 도서가 없습니다.\n")
                continue
            else:
                keyword_book = input("검색할 도서 제목 키워드 :")
                print(f"-----------'{keyword_book}'검색 결과-----------")
                for book in book_list:
                    if keyword_book in book["제목"] :
                        print(f'제목:{book["제목"]}\t| 저자:{book["저자"]}\t| 가격:{book["가격"]}')
                        found = True
                if not found:
                        print(f"'{keyword_book}'을 찾을 수 없습니다.\n")
                        found = False
                print("-------------------------------")
        # 4. 도서 삭제
        elif menu == 4:
            found = False
            print("도서 삭제")
            try:
                if len(book_list) == 0:
                    raise ValueError
            except ValueError:
                print("삭제할 도서가 없습니다.\n")
                continue

            while True:
                try:
                    delete_book = input("삭제할 도서 제목 :")
                    if len(delete_book) == 0:
                        raise ValueError
                except ValueError:
                    print("다시 입력해주세요")
                    continue
                else:
                    for book in book_list:
                        if book["제목"] == delete_book:
                            book_list.remove(book)
                            print(f"{delete_book}이 삭제되었습니다.")
                            found=True
                    if not found:
                            print(f"'{delete_book}'을 찾을 수 없습니다.\n")
                    break



        # 5. 도서 수정
        elif menu == 5:
            found = False
            try:
                if len(book_list) == 0:
                    raise ValueError
            except ValueError:
                print("수정할 도서가 없습니다.\n")
                continue

            modify_book = input("수정할 도서 제목 :")
            for book in book_list:
                if book["제목"] == modify_book:
                    while True:
                        try:
                            modify_price = int(input("수정할 가격 입력 3~5자리 숫자입력 :"))
                            if 3 > len(str(modify_price)) or  len(str(modify_price)) >6:
                                raise ValueError
                        except ValueError:
                            print("숫자 3~5자리를 입력해주세요!!")
                        else:
                            book["가격"] = modify_price
                            print(f"{modify_book}의 가격이 수정되었습니다.")
                            found = True
                            break

            if not found:
                print(f"'{modify_book}'을 찾을 수 없습니다.\n")

        # 6. 파일 저장
        elif menu == 6:
            try:
                if len(book_list) == 0:
                    raise ValueError
            except ValueError:
                print("저장할 내용이 없습니다.\n")
                continue

            fw = open("Book.txt", "w", encoding="utf-8")
            for book in book_list:
                for key, value in book.items():
                    fw.write(f'{key} :{value}\t')
                fw.write('\n')
            fw.close()
            print("파일 저장 완료!!\n")

        elif menu == 7:
            print("시스템 종료!!")
            break
