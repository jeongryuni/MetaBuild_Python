import re

try:
    fr =open("Book.txt", "r", encoding="utf-8")
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
          "4. 도서삭제\n"
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
                fw = open("Book.txt", "a", encoding="utf-8")
                title = input("도서 제목 : ")
                author = input("저자 : ")
                while True:
                    try:
                        price = int(input("가격 :"))
                    except ValueError:
                        print("가격은 숫자로 입력해야 합니다.")
                    else:
                        fw.write(f"{title} {author} {price}\n")
                        print(f"도서 {title} 등록!!\n")
                        fw.close()
                        break

        # 2. 전체 도서 보기
        elif menu == 2:
            try:
                fr = open("Book.txt", "r", encoding="utf-8")
                lines = fr.readlines()
                if len(lines) == 0:
                    raise FileNotFoundError
                fr.close()
            except FileNotFoundError:
                print("등록된 도서가 없습니다.\n")

            fr = open("Book.txt", "r", encoding="utf-8")
            lines = fr.readlines()
            print("=" * 15, "도서조회" ,"=" * 15)
            for lines in lines:
                line = lines.strip()
                match = re.match(r"(.+)\s(.+)\s(\d+)", line)
                if match:
                    title = match.group(1)
                    author = match.group(2)
                    price = int(match.group(3))
                    print(f"제목 :{title}\t| 저자 :{author}\t | 가격 :{price}")
            print("="*40)


        # 도서 검색
        elif menu == 3:

            # 등록된 도서가 없을 경우
            try:
                fr = open("Book.txt", "r", encoding="utf-8")
                lines = fr.readlines()
                if len(lines) == 0:
                    raise FileNotFoundError
                fr.close()
            except FileNotFoundError:

                print("등록된 도서가 없습니다.\n")
                fr = open("Book.txt", "r", encoding="utf-8")
                lines = fr.readlines()
                


            print("도서 검색")
            keyword_book = input("검색할 도서 제목 키워드 :")

            pass
        elif menu == 4:
            pass
        elif menu == 5:
            pass
        elif menu == 6:
            pass
        elif menu == 7:
            print("시스템 종료!!")
            break