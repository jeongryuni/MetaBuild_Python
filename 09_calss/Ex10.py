# 다중상속
class Lion:
    def __init__(self):
        print("Lion 생성자")
    def bite(self):
        print("Lion bite")
    def cry(self):
        print("Lion Cry")

class Tiger:
    def __init__(self):
        print("Tiger 생성자")
    def jump(self):
        print("Tiger jump")
    def cry(self):
        print("Tiger cry")

# Liger 클래스: Tiger와 Lion을 동시에 상속받음 (다중 상속)
class Liger(Tiger, Lion):
    def play(self):
        print("Liger play")

# Liger는 생성자가 따로 정의되어 있지 않음.
# 따라서 상속받은 클래스 중 '첫 번째 클래스(Tiger)'의 생성자가 자동 호출됨.
l = Liger() # → 출력: "Tiger 생성자"
l.play()
l.jump()
l.bite()
l.cry() # 부모가 같은 메서드를 가지고있으면 먼저 상속받은 메서드 호출

