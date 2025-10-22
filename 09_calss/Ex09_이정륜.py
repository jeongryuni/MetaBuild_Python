# 제품
from itertools import product


class Product:

    def __init__(self, fruit, price):
        self.fruit = fruit
        self.price = price

    def printProduct(self):
        print(self.fruit, self.price)
        return f"{self.fruit}, {self.price}"


# 장바구니
class Cart() :
    def __init__(self):
        self.items = [] # p1,3  p2,4  /  p2,2 p3,5

# 고객
class Customer():
    def __init__(self, name):
        self.name = name
        self.cart = Cart()

    def addCart(self, product, qty):
        self.cart.items.append((product, qty))

    def checkout(self):
        print(f"{self.name}의 결제정보")
        for prod, qty in self.cart.items:
            print(f"{prod.fruit} : {prod.price} * {qty} = {prod.price * qty}")
            print(f"총합 : {prod.price * qty}원")

p1 = Product("사과", 1000)
p2 = Product("포도", 2000)
p3 = Product("딸기", 3000)

print("------------printProduct------------")
p1.printProduct()  # 사과/1000원(name, price)
p2.printProduct()
p3.printProduct()

c1 = Customer("수영") # name, cart/ cart = cart()
c2 = Customer("정국") # name, cart/ cart = cart()

c1.addCart(p2, 3)
c1.addCart(p3, 8)
c2.addCart(p3, 5)


print("------------checkout------------")
c1.checkout()
c2.checkout()
