# 02.py

def apple():
    print("apple")
apple()


print("__name__ :",__name__)

print("------------------")
import Ex01
Ex01.abc()
Ex01.xyz()

print("------------------")
import Ex01 as e
e.abc()
e.xyz()

print("------------------")
#from Ex01 import abc, xyz
from Ex01 import *
abc()
xyz()

print("------------------")
import myPkg.Ex01
print(myPkg.Ex01.add(2,5))
print(myPkg.Ex01.mul(2,5))

import myPkg.Ex01 as m
print(m.add(2,5))
print(m.mul(2,5))

from myPkg.Ex01 import *
print(add(2,5))
print(mul(2,5))