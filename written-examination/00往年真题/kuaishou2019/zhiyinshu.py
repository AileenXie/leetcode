#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/22 4:56 PM
# @Author : aileen
# @File : zhiyinshu.py
# @Software: PyCharm


def count_zhiyinshu(n):
    def count(x):
        if x in zhi:
            return 1
        if x in mem.keys():
            print("---{}".format(x))
            return mem[x]
        for i in zhi:
            if x % i == 0:
                mem.setdefault(x, 1+count(x//i))
                return mem[x]
        else:
            zhi.append(x)
            return 1
    zhi = [2,3]
    mem = {}
    ans = 0
    for i in range(2,n+1):
        ans += count(i)
    print(mem)
    return ans


n = int(input())
print(count_zhiyinshu(n))


