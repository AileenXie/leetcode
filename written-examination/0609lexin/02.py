#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/9 7:30 PM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm

n = int(input().strip())

import math
def is_prime(num):
    for i in range(2,int(math.sqrt(num))):
        if num % i == 0: return False
    return True


def func(n):
    prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    num = 1
    for i in range(n):
        num *= prime[i]
    num += 1
    if is_prime(num):
        print("{} is a prime".format(num))
    else:
        print("{} is not a prime".format(num))


func(n)