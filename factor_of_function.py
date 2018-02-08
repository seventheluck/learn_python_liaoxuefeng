#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#函数的默认参数
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def power2(n=2):
    nv= n - 1
    return n

def add_end(L=[]):
    L.append('END')
    return L

print(power(3))
print(power(3,2))
print(power(3,3))

print('=============================')

print(add_end())
print(add_end())
print(add_end())


print('=============================')

print(power2())
print(power2())
print(power2())