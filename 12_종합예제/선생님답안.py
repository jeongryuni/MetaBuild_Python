import re


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"😊제목: {self.title} 🍟저자:{self.author} 가격:{self.price}"


class BookManager:

    def __init__(self):
        self.books = []

    def add_book(self, title, author, price):
        self.books.append(Book(title, author, price))
        print('도서 등록 되었습니다.')
        # print(self.books)

    def show_all(self):
        if not self.books:
            print('등록된 도서가 없습니다.\n')
            return

        for book in self.books:
            # print(book.title,book.author,book.price)
            # print(book.__str__())
            print(book)

    def remove_book(self, remove_title):
        flag = False
        for book in self.books:
            if book.title == remove_title:
                self.books.remove(book)
                print(f"{remove_title} 삭제되었습니다.")
                flag = True

        if flag == False:
            print(f"{remove_title} 찾지 못했습니다.")

    def find_book(self, search_title):  # jAvA
        # foundList = [[java,kim,1000],[python,choi,2000]]
        foundList = []
        for book in self.books:  # book:title,author,price
            if search_title.lower() in book.title.lower():
                foundList.append(book)

        if foundList:
            for book in foundList:
                print(book)
        else:
            print(f"{search_title} 도서 검색 못함")

    def update_book(self, update_title):
        flag = False
        for book in self.books:
            if update_title.lower() in book.title.lower():
                flag = True

        if not flag:
            print(f"{update_title} 도서 검색 못함")
            return

        try:
            new_price = input("새 가격을 입력하세요:")
            pattern = re.compile('[0-9]{3,5}')
            if not pattern.match(new_price):
                raise ValueError("가격은 3자리에서 5자리 숫자만 입력가능합니다.")

            for book in self.books:
                if book.title == update_title:
                    book.price = new_price
                    print(f"{update_title} 도서 가격 수정함")

        except ValueError as e:
            print(e)

    def file_write(self):
        with open("books.txt", "w", encoding="utf-8") as f:
            for book in self.books:
                f.write(f"{book.title},{book.author},{book.price}\n")
        print('파일에 저장이 되었습니다.')

    def file_read(self):
        try:
            with open("books.txt", "r", encoding="utf-8") as f:
                for line in f:  # a,aa,11\n
                    line = line.strip()  # a,aa,11
                    if not line:
                        continue
                    title, author, price = line.split(',')
                    self.books.append(Book(title, author, price))
            print('파일의 내용을 로드했습니다.')

        except FileNotFoundError:
            print('파일이 없습니다. 새로 시작합니다.')


def main():
    manager = BookManager()
    manager.file_read()

    while True:
        print('\n[도서 관리 시스템]')
        print('1. 도서 등록')
        print('2. 전체 도서 보기')
        print('3. 도서 검색')
        print('4. 도서 삭제')
        print('5. 도서 가격 수정')
        print('6. 파일 저장')
        print('7. 종료')

        menu = input('메뉴 선택 (1~7):')
        if menu == '1':
            title = input('제목:')
            author = input('저자:')
            while True:
                try:
                    price = int(input("가격(숫자만): "))
                    manager.add_book(title, author, price)
                    break
                except ValueError:
                    print("가격은 숫자로 입력하세요")

        elif menu == '2':
            manager.show_all()

        elif menu == '3':
            searchTitle = input('검색할 도서 제목 : ')
            manager.find_book(searchTitle)

        elif menu == '4':
            deleteTitle = input('삭제할 도서 제목 : ')
            manager.remove_book(deleteTitle)

        elif menu == '5':
            updateTitle = input('수정할 도서 제목 : ')
            manager.update_book(updateTitle)

        elif menu == '6':
            manager.file_write()

        elif menu == '7':
            print('프로그램 종료')
            break
        else:
            print("1~7만 가능")


if __name__ == '__main__':
    main()
