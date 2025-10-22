class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f"이름:{self.name} / 나이:{self.age} / ", end="")

class Employee(Person):

    def __init__(self, name, age, position, salary):
        # 1) 부모 생성자 받기
        #super().__init__(name, age)
        # 2) 부모 생성자 받기 (클래스 + self 필수)
        Person.__init__(self, name, age)
        self.position = position
        self.salary = salary

    def show(self):
        # 1) 부모의 show 받기 (클래스 + self 필수)
        #Person.show(self)
        # 2) 부모의 show
        super().show()
        print(f"직급:{self.position} / 연봉:{self.salary}")


p1 = Person('보검', 30) #name, age
p2 = Person('아이유', 40)

e1 = Employee('태연', 50, "대리", 300) #name, age, position, salary
e2 = Employee('수영', 20, "사원", 200)

print("----------p1.show()------------")
p1.show()
print()
print("----------p2.show()--------------")
p2.show()
print()
print("----------e1.show()------------")
e1.show()
print("----------e2.show()------------")
e2.show()