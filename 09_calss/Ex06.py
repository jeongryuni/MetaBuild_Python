# 상속
class Super:
    def __init__(self):
        print("Super 생성자")

    def show(self):
        print("Super show")

class Sub:
    def __init__(self):
        print("Sub 생성자")

    def show(self):
        Super.show(self)  # 상속받지 않아도 show 호출 가능
        #super().show() # 호출 불가능
        print("Sub show")

class Sub2(Super): # class sub extends Super (Super 상속)
    def __init__(self):
        #Super.__init__(self) # 부모(Super)의 생성자를 명시적으로 호출 → 부모의 클래스명으로 호출할땐 주소 명시
                             # → 상속받았다고 해서 자동 호출되지 않음
                             # → 반드시 직접 호출해야 부모 초기화 가능
        super().__init__() # 부모의 생성자 호출 (주소 넘기지않기, 자동으로 넘어감)
        print("Sub2 생성자")

    def show(self):
        # Super().show(self)
        super().show() # 부모 show 호출
        print("Sub2 show")

# java와 달리 상속받은 자손이 부모생성자를 들리지않음
sp1 = Super()
print("------------------")
sb1 = Sub()
print("------------------")
sb2 = Sub2()


print("--------sp1.show()----------")
sp1.show()
print("--------sb1.show()----------")
sb1.show()
print("--------sb2.show()----------")
sb2.show()
