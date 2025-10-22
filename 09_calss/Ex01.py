class Person:
    # 자바의 스태틱변수도 클래스명으로 접근 가능함, 클래스 변수라고도 함
    lastname = "김" # ==> 클래스 변수

    # 클래스 안에 있는 함수는 매개변수가 1개이상 필수 (self)를 많이씀
    def set_name(self, x):
        self.fullname = self.lastname + x #클래스 안에서 생성된 변수만 작성 가능

    def set_age(self, age):
        self.age = age

    def display(self):
        print(self.fullname, "/", self.age)

# 객체 생성
p1 = Person()
p2 = Person()
print(p1)
print(p2)
print(p1.lastname)
print(p2.lastname)
print(Person.lastname)
print("========p1,p2 setname========")
p1.set_name('윤아')
p2.set_name('정국')

print("========p1,p2 fullname========")
print(p1.fullname)
print(p2.fullname)

print("========p1,p2 age========")
p1.set_age(30)
p1.display()

p2.set_age(50)
p2.display()