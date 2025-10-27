import re

class Member:
    def __init__(self, name, email):
        self.name = name
        self.email = email


class Employee(Member):
    def __init__(self, name, email, salary):
        super().__init__(name, email)
        self.salary = salary

    def __str__(self):
        return f"이름: {self.name}\t| 이메일: {self.email}\t| 급여: {self.salary}"


class MemberManager:
    def __init__(self):
        self.member_list = []

    def __str__(self):
        if not self.member_list:
            return "등록된 정보가 없습니다."
        result = ""
        for mem in self.member_list:
            result += f"이름: {mem['name']}\t| 이메일: {mem['email']}\t| 급여: {mem['salary']}\n"
        return result

    # 직원 등록
    def add_mem(self):
        while True:
            try:
                name = input("이름 입력: ")
                if len(name) < 2:
                    raise IndexError
            except IndexError:
                print("이름은 2자리 이상 입력해주세요.")
                continue
            break

        while True:
            try:
                email = input("이메일 입력 (아이디@도메인.com 또는 .net): ")
                pattern = re.compile(r"^[A-Za-z0-9]+@[A-Za-z0-9]+\.(com|net)$")
                if not pattern.match(email):
                    raise ValueError
            except ValueError:
                print("잘못된 이메일 형식입니다.")
                continue
            break

        while True:
            try:
                salary = int(input("급여 입력: "))
                if salary <= 0:
                    raise ValueError
            except ValueError:
                print("급여를 다시 입력해주세요 (양의 정수).")
                continue
            else:
                self.member_list.append({"name": name, "email": email, "salary": salary})
                print(f"{name}의 정보가 등록되었습니다.")
                break

    # 전체 직원 보기
    def show_all(self):
        print(self)

    # 직원 검색
    def show_mem(self):
        if not self.member_list:
            print("등록된 정보가 없습니다.")
            return

        keyword = input("검색할 직원의 이름을 입력하세요: ")
        print(f"\n'{keyword}'의 검색 결과:")
        flag = False
        for mem in self.member_list:
            if keyword in mem["name"]:
                print(f"이름: {mem['name']}\t| 이메일: {mem['email']}\t| 급여: {mem['salary']}")
                flag = True

        if not flag:
            print("존재하지 않는 직원입니다.")

    # 직원 삭제
    def remove_mem(self):
        if not self.member_list:
            print("등록된 정보가 없습니다.")
            return

        keyword = input("삭제할 직원의 이름을 입력하세요: ")
        flag = False
        for mem in self.member_list:
            if keyword in mem["name"]:
                self.member_list.remove(mem)
                print(f"{keyword}의 정보를 삭제했습니다.")
                flag = True
                break

        if not flag:
            print("존재하지 않는 직원입니다.")

    # 급여 수정
    def modify_mem(self):
        if not self.member_list:
            print("등록된 정보가 없습니다.")
            return

        keyword = input("수정할 직원의 이름을 입력하세요: ")
        flag = False
        for mem in self.member_list:
            if keyword == mem["name"]:
                while True:
                    try:
                        new_salary = input("새로운 급여 입력 (3~5자리 숫자): ")
                        pattern = re.compile(r"^[0-9]{3,5}$")
                        if not pattern.fullmatch(new_salary):
                            raise ValueError
                    except ValueError:
                        print("다시 입력해주세요. (3~5자리 숫자만 입력 가능)")
                        continue
                    else:
                        mem["salary"] = int(new_salary)
                        print(f"{keyword}의 급여가 {new_salary}로 수정되었습니다!")
                        flag = True
                        break
                break

        if not flag:
            print("존재하지 않는 직원입니다.")

    # 파일 저장
    def save_file(self):
        if not self.member_list:
            print("등록된 정보가 없습니다.")
            return
        try:
            with open("member.txt", "w", encoding="UTF-8") as f:
                for mem in self.member_list:
                    f.write(f'{mem["name"]}/{mem["email"]}/{mem["salary"]}\n')
            print("저장 완료 (member.txt)")
        except Exception as e:
            print("파일 저장 중 오류:", e)

    # 파일 로드
    def read_file(self):
        self.member_list.clear()
        try:
            with open("member.txt", "r", encoding="UTF-8") as f:
                for line in f:
                    if not line.strip():
                        continue
                    name, email, salary = line.strip().split("/")
                    self.member_list.append({"name": name, "email": email, "salary": int(salary)})
            print("파일 로드 완료\n")
        except FileNotFoundError:
            print("member.txt 파일이 없습니다. 새 파일로 시작합니다.\n")


def main():
    mem = MemberManager()
    mem.read_file()

    while True:
        print("\n[직원 관리 시스템]")
        print("1. 직원 등록")
        print("2. 전체 직원 보기")
        print("3. 직원 검색")
        print("4. 직원 삭제")
        print("5. 급여 수정")
        print("6. 파일 저장")
        print("7. 종료")

        try:
            menu = int(input("메뉴 선택 (1~7): "))
            if menu not in range(1, 8):
                raise ValueError
        except ValueError:
            print("숫자 1~7 사이로 입력해주세요.")
            continue

        if menu == 1:
            mem.add_mem()
        elif menu == 2:
            mem.show_all()
        elif menu == 3:
            mem.show_mem()
        elif menu == 4:
            mem.remove_mem()
        elif menu == 5:
            mem.modify_mem()
        elif menu == 6:
            mem.save_file()
        elif menu == 7:
            print("시스템 종료!")
            break


if __name__ == "__main__":
    main()
