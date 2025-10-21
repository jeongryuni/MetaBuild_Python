import math
print(math.pi)
print(math.factorial(5))
print("----------math import------------")
import math as m
print("m.sqrt(5) :",m.sqrt(5))
print("----------------------")
from math import *
print("sqrt(5) :", sqrt(5))
from math import factorial as fac
print("print(fac(5)) :", fac(5))

print("----------------------")
print("max: ", max(10,30,50,60,70,100))
print("min::", min(10,30,50,60,70,100))
print("abs: ", abs(-10))
print("pow: ", pow(10,20))
print("round: :", round(5,43))
print("sumb :", sum((10,20)))

print("-----------import datatime-----------")
import datetime
print(datetime.datetime.now())
print(datetime.datetime.today())

from datetime import *
now = datetime.now()
print(now)
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)
print(now.weekday())

print('%s년 %s월 %s일' % (now.year,now.month,now.day))
print('%d년 %d월 %d일' % (now.year,now.month,now.day))
print(datetime.weekday(now)) # 월요일 : 0

print("-----------today-----------")
def weekday_today():
    year = now.year
    month = now.month
    day = now.day
    weekday = now.weekday()
    week = ['월', '화', '수', '목', '금', '토', '일']
    return f"{year}년 {month}월 {day}일은 {week[weekday]}요일입니다."

print(weekday_today())
