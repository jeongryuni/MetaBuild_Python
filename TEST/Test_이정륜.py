import re

class Movie:
    def __init__(self, title, director, grade):
        self.title = title
        self.director = director
        self.grade = grade

    def __str__(self):
        return f"영화명 :{self.title}\t| 감독명 :{self.director}\t| 영화등급 :{self.grade}"

class MovieManager:
    def __init__(self):
        self.movies = []
    # 추가
    def add_movie(self):
        while True:
                title = input("영화 제목 입력")
                director = input("영화 감독 입력")
                while True:
                    try:
                        grade = input("영화 등급 입력")
                        pattern = re.compile(r'^[0-9]{1,2}$|^[A-Za-z]+$')
                        if not pattern.search(grade):
                            raise ValueError
                    except ValueError:
                        print("숫자 1~2자리 입력가능")
                        continue
                    else:
                        movie = Movie(title, director, str(grade))
                        self.movies.append(movie)
                        print(f"'{title}'이 등록 되었습니다.")
                    break
                break

    # 전체조회
    def show_all(self):
        if not self.movies:
            print("등록된 영화가 없습니다.")
            return

        for movie in self.movies:
            print(movie)

    # 영화찾기
    def find_movie(self):

        if not self.movies:
            print("등록된 영화가 없습니다.")
            return

        flag = False
        input_title = input("찾을 영화제목 입력 :")
        print(f"{input_title} 검색결과")
        for movie in self.movies:
            if input_title.lower() in movie.title.lower():
                print(movie)
                flag = True

        if not flag:
            print(f"{input_title}찾을 수 없음")


    def remove_movie(self):
        flag = False
        if not self.movies:
            print("등록된 영화가 없습니다.")
            return

        delete_title = input("삭제할 영화 제목 입력 :")
        for movie in self.movies:
            if movie.title == delete_title:
                self.movies.remove(movie)
                print(f"'{delete_title}' 영화가 삭제 되었습니다.")
                flag = True

        if not flag:
            print(f"'{delete_title}' 영화를 찾을 수 없습니다.")

    # 영화 수정
    def modify_movie(self):
        if not self.movies:
            print("등록된 영화가 없습니다.")
            return

        flag = False
        modify_title = input("수정할 영화제목 입력 :")
        for movie in self.movies:
            if modify_title == movie.title:
                while True:
                    try:
                        grade = input("영화 등급 입력")
                        pattern = re.compile(r'^[0-9]{1,2}$|^[A-Za-z]+$')
                        if not pattern.search(grade):
                            raise ValueError
                    except ValueError:
                        print("숫자 1~2자리 입력가능")
                        continue
                    else:
                        movie.grade = str(grade)
                        print("수정됨")
                        flag = True
                        break

        if not flag:
            print(f"'{modify_title}'을 찾지못했습니다.")

    # 파일 저장
    def save_file(self):
        flag = False
        if not self.movies:
            print("등록된 영화가 없습니다.")
            return

        with open("test.txt", "w", encoding="utf-8") as f:
            for movie in self.movies:
                f.write(movie.title + "\t" + movie.director + "\t" + movie.grade + "\n")
        print("저장됨")

    # 파일 로드
    def load_file(self):
        self.movies.clear()
        try:
            with open("test.txt", "r", encoding="utf-8") as f:
                for line in f:
                    movie = line.split("\t")
                    self.movies.append(Movie(movie[0], movie[1], movie[2]))
        except FileNotFoundError:
            print("새로 시작함")



def main():
    mm = MovieManager()
    mm.load_file()


    while True:
        print("영화 관리 시스템")
        print(
                "1. 영화 등록\n",
                "2. 전체 영화 보기\n",
                "3. 영화 검색\n",
                "4. 영화 삭제\n",
                "5. 영화 등급 수정\n",
                "6. 파일 저장\n",
                "7. 종료"
        )
        try:
            menu = int(input("메뉴 선택 1~7"))
        except ValueError:
            print("1~7사이 입력")
            continue

        if menu == 1:
            mm.add_movie()

        elif menu == 2:
            mm.show_all()

        elif menu == 3:
            mm.find_movie()

        elif menu == 4:
            mm.remove_movie()

        elif menu == 5:
            mm.modify_movie()

        elif menu == 6:
            mm.save_file()

        elif menu == 7:
            print("시스템 종료")
            break


if __name__ == "__main__":
    main()
