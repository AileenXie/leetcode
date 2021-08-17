#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/8 8:07 PM
# @Author : aileen
# @File : 02.py
# @Software: PyCharm

s1 = input()
s2 = input()


def func(s1, s2):
    if s1 + s2 != s2 + s1:
        return ""
    l1 = len(s1)
    l2 = len(s2)
    if l1 == l2:
        return s1  # 必定相等
    elif l1 > l2:
        s1=s1[l2:]
    else:
        s2=s2[l1:]
    return func(s1,s2)

print(func(s1,s2))
