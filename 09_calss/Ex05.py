# Ex04.py
import Ex04
s1 = Ex04.Service("맹구")
s1.show()

import Ex04 as ex
s2 = ex.Service("조이")
s2.show()

from Ex04 import *
s3 = Service("고양이")
s3.show()

from Ex02 import *
s4 = Student(17)
s4.show()
print(s4.name, s4.age)




