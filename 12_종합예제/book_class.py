import re


class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"제목 :{self.title}\t 저자 :{self.author}\t 가격: {self.price}"


class BookManager:
    def __init__(self):
        self.book_list = []

    def add_book(self):
        while True:
            try:
                title = input("제목 입력: ")
                for book in self.book_list:
                    if title.lower() in book.title.lower():
                        raise ValueError
            except ValueError:
                print("중복되는 제목입니다.")
                continue
            else:
                    while True:
                        author = input("저자 : ")
                        try:
                            price = int(input("가격 입력:"))
                        except ValueError:
                            print("가격은 숫자로 입력해야 합니다.")
                        else:
                            self.book_list.append(Book(title, author, price))
                            print(f"도서 {title} 등록!!\n")
                            break

            break

    def remove_book(self):

        if not self.book_list:
            print("등록된 도서가 없습니다.\b")
            return

        flag = False
        delete_book = input("삭제할 도서 입력")
        for book in self.book_list:
            if book.title == delete_book:
                self.book_list.remove(book)
                flag = True

        if flag == False:
            print(f"{delete_book}을 찾을 수 없습니다.")
            return


    def show_all(self):
        if not self.book_list:
            print("등록된 도서가 없습니다.\b")

        else:
            print("----------도서 전체 조회----------")
            for book in self.book_list:
                print(book)
            print("--------------------------------")
            return


    def find_book(self):

        if not self.book_list:
            print("등록된 도서가 없습니다.\b")
            return
        found_list = []

        keyword = input("조회할 도서 입력")
        for book in self.book_list:
            if keyword.lower() in book.title.lower():
                found_list.append(book)

        if found_list:
            print(f"-----------'{keyword}'검색 결과-----------")
            for book in found_list:
                print(book)
        print("-------------------------------")

        if not found_list:
            print(f"'{keyword}'을(를) 찾을 수 없습니다.\n")
            return

    def modify_book(self):
        found = False
        if not self.book_list:
            print("등록된 도서가 없습니다.\b")
            return

        modify_book = input("수정할 도서 제목 :")
        for book in self.book_list:
            if book.title == modify_book:
                while True:
                    try:
                        modify_price = input("수정할 가격 입력 3~5자리 숫자입력 :")
                        pattern = re.compile('[0-9]{3,5}')
                        if not pattern.match(modify_price):
                            raise ValueError("가격은 3자리에서 5자리 숫자만 입력가능합니다.")
                        for book in self.books:
                            if book.title == modify_book:
                                book.price = modify_price
                                print(f"{modify_book}도서 가격을 수정했습니다!")

                    except ValueError as e:
                        print(e)
                        print("숫자 3~5자리를 입력해주세요!!")


        if not found:
            print(f"'{modify_book}'을 찾을 수 없습니다.\n")

    def file_write(self):
        if not self.book_list:
            print("등록된 도서가 없습니다.\b")
            return

        fw = open("Book.txt", "w", encoding="utf-8")
        for book in self.book_list:
            for key, value in book.items():
                fw.write(f'{key} :{value}\t')
            fw.write('\n')
        fw.close()
        print("파일 저장 완료!!\n")

    def file_read(self):
        try:
            with open("Book.txt", "r", encoding="utf-8") as f:
                for line in f:
                    if not line:
                        continue
                    title, author, price = line.split(",")
                    self.book_list.append(Book(title, author, price))
            print("파일의 내용을 로드했습니다.")
        except FileNotFoundError:
            print('파일이 없습니다. 새로 시작합니다.')


def main():
    manager = BookManager()
    manager.file_read()

