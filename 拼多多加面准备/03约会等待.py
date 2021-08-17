#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/15 11:11 AM
# @Author : aileen
# @File : 03约会等待.py
# @Software: PyCharm

def fun():
    a = 0
    b = 0
    for x in range(0, 60+1):
        for y in range(0, 60+1):
            z = x - y
            if z >= -10 and z <= 10:
                a += 1
            b += 1
    print(a,b)
    return a / b

print(fun())
print()