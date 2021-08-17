#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/25 9:28 AM
# @Author : aileen
# @File : 03多重背包问题i.py
# @Software: PyCharm

"""
小Q最近遇到了一个难题：把一个字符串的大写字母放到字符串的后面，各个字符的相对位置不变，且不能申请额外的空间。
你能帮帮小Q吗？


输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.



输出描述:

对于每组数据，输出移位后的字符串。


输入例子1:
AkleBiCeilD

输出例子1:
kleieilABCD
"""

import sys

def func(s):
    n = len(s)
    s_list = [c for c in s]
    if n < 2:
        return s
    for i in range(n):
        flag = False
        for j in range(n-i-1):
            if not s_list[j].islower() and s_list[j+1].islower():
                flag = True
                s_list[j],s_list[j+1]=s_list[j+1],s_list[j]
        if not flag:
            break
    s = "".join(s_list)
    return s

s = sys.stdin.readline().strip()
print(func(s))
