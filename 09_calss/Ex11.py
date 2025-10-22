class Box:
    def __init__(self, num):
        self.num1 = num
        self.num2 = num

    def __add__(self, num):
        self.num1 += num
        return "더하기(__add__):" + str(self.num1)

    def __radd__(self, num):
        self.num1 += num
        return "더하기(__add__):" + str(self.num1)

    def __sub__(self, num):
        self.num1 -= num
        return "빼기(__sub__):" + str(self.num1)

    def __rsub__(self, num):
        self.num1 -= num
        return "빼기(__sub__):" + str(self.num1)


b1 = Box(10)
print(b1.num1)
print(b1.num2)

print(b1.num1 + b1.num2)

# 연산자 오버로딩
print(b1 + 10) # b1로 self로 들어감 + 30(num) // num1 = self + num  20 = 10 + 10
print(20 + b1) # 40 = 20 + 20

print(b1 - 1) # 39 = 40 - 1
print(20 - b1) # 39 - 20 = 19
