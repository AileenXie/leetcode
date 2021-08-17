#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 3:30 PM
# @Author : aileen
# @File : 04多重背包问题ii.py
# @Software: PyCharm

"""
求子串中公约数（gcd）和元素个数最大乘积

输入：
n：数组元素个数
A：数组

输入：
5
3 6 2 2 2
输出：
8   ([6 2 2 2]公约数2*个数4=8)

0%
"""


def gcd(numbers):
    n = len(numbers)
    if n == 2:
        if numbers[0]>numbers[1]:
            a, b = numbers[0], numbers[1]  # a>b
        else:
            b, a = numbers[0], numbers[1]  # a>b
        return gcd([b,a%b])
    else:
        return gcd([gcd(numbers[:-1]),numbers[-1]])

def func(n,A):
    l,r = 0,n-1
    cur_gcd = gcd(A)
    cur_ans = cur_gcd*n

    max_ans = cur_ans

