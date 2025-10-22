class Bank():
    rate = 0.03

    def __init__(self,money):
        self.money = money

    def calculate(self):
        self.money = int(self.money + (Bank.rate * self.money))

    def show(self):
        self.calculate()
        print(f"{self.money}원")

b1 = Bank(10000)
b2 = Bank(30000)

b1.show()
b2.show()