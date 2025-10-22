class Student():
    name = "철수"

    # 생성자
    def __init__(self, age):
        # print("init : ", self, age)
        self.age = age

    def show(self):
        print(self.name , " ", self.age)

if __name__=="__main__":
    s1 = Student(11)
    s2 = Student(22)
    print(s1.name, s1.age)
    print(s2.name, s2.age)