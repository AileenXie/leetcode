#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/23 1:18 PM
# @Author : aileen
# @Software: PyCharm

n = int(input())

def func(n):
    if n < 10:
        return 0
    def get_count(n,c):
        cur = 1
        for i in str(n):
            cur *= int(i)
        if cur < 10:
            return c
        else:
            return get_count(cur, c+1)

    return get_count(n,1)

print(func(n))
