
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#请定义一个函数quadratic(a, b, c)，接收3个参数，返回一元二次方程：
#ax2 + bx + c = 0的两个解。

import math

def quadratic(a, b, c):
    x1 = x2 = 0
    if(4 * a * c >= 0):
        x1 = (-b + math.sqrt(4 * a * c)) / 2 * a
        x2 = (-b - math.sqrt(4 * a * c)) / 2 * a
    elif(4 * a * c < 0):
        x1 = x2 = "wujie"
    if (x1 == "wujie"):
        print("wujie")
    elif (x1 == x2):
        print("x = %.4f" % x1)
    else:
        print("\n")
        print("x1 = %.4f" % x1 +"    x2 = %.4f" % x2)


print("Please input a:")
a = input()
a = int(a)

print("Please input b:")
b = input()
b = int(b)

print("Please input c:")
c = input()
c = int(c)

quadratic(a,b,c)