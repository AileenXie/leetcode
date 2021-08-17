#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/8 8:15 PM
# @Author : aileen
# @File : 03.py
# @Software: PyCharm

# print(ord("a"))
# print(ord("z"))
# print(ord("A"))
# print(ord("Z"))
# print(ord("0"))
# print(ord("9"))


s=input()

def func(s):
    total = []
    result = 0
    aa,bb=len(s)//5,len(s)%5  # aa个5+bb
    def encode(c):
        cur = ord(c)
        if ord("0") <= cur <= ord("9"):  # 0-9
            ans = cur + 5
        elif ord("A") <= cur <= ord("Z"):  # A-Z
            ans = cur - 38
        elif ord("a") <= cur <= ord("z"):  # a-z
            ans = cur - 96
        else:
            ans = 0
        return ans
    for i in range(aa):
        for c in s[5*i:(i+1)*5]:
            ans=encode(c)
            result=(result<<6)+ans
        total.append(result)
    result=0
    if bb:  # 有余数
        for c in s[-bb:]:
            ans=encode(c)
            result=(result<<6)+ans
        total.append(result)
    return ' '.join([str(a) for a in total])

print(func(s))