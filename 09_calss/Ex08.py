class Address:
    def __init__(self):
        self.city = ""
        self.street = ""

    def setAddress(self, city, street):
        self.city = city
        self.street = street

    def showAddress(self):
        return f"{self.city}, {self.street}"


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.address = Address() # Student 생성시 ==> 새로 만들어진 Address주소가 Student에 들어옴

    def setAddress(self, city, street):
        # self.address.city = city
        # self.address.street = street

        # Address 객체를 포함 (학생 한 명이 자신의 주소를 가짐 — '포함 관계(Composition)')
        self.address.setAddress(city, street) #Address클래스의 setAddress 메서드를 이용

    def showStudent(self):
        print(f"이름 :{self.name}")
        print(f"나이 :{self.age}")
        print(f"주소 :{self.address.showAddress()}")

s1 = Student("정륜", 27)
s1.setAddress("서울", "서초구")

s1.showStudent()