from book_class import *

def main():
    manager = BookManager()
    manager.file_read()

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
                manager.add_book()

            # 2. 전체 도서 보기
            elif menu == 2:
                manager.show_all()

            # 3. 도서 검색
            elif menu == 3:
                manager.find_book()

            # 4. 도서 삭제
            elif menu == 4:
                manager.remove_book()

            # 5. 도서 수정
            elif menu == 5:
                manager.modify_book()

            # 6. 파일 저장
            elif menu == 6:
                manager.file_write()

            elif menu == 7:
                print("시스템 종료!!")
                break

if __name__ == "__main__":
     main()