#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 10:03 AM
# @Author : aileen
# @File : 04多重背包问题ii.py
# @Software: PyCharm

"""
小Q有X首长度为A的不同的歌和Y首长度为B的不同的歌，现在小Q想用这些歌组成一个总长度正好为K的歌单，每首歌最多只能在歌单中出现一次，在不考虑歌单内歌曲的先后顺序的情况下，请问有多少种组成歌单的方法。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含一个整数，表示歌单的总长度K(1<=K<=1000)。
接下来的一行包含四个正整数，分别表示歌的第一种长度A(A<=10)和数量X(X<=100)以及歌的第二种长度B(B<=10)和数量Y(Y<=100)。保证A不等于B。

输出描述:
输出一个整数,表示组成歌单的方法取模。因为答案可能会很大,输出对1000000007取模的结果。

输入例子1:
5
2 3 3 3

输出例子1:
9
"""


def func(k,a,x,b,y):
    # 先计算出a,b对k的所有组合
    groups = []  # 记录可能的搭配
    visited = set()

    def get_group(k,count_a, count_b):
        if k == 0:
            groups.append((count_a,count_b))
            return
        if (count_a,count_b) in visited:
            return
        if k < 0:
            return
        get_group(k-a,count_a+1,count_b)
        get_group(k-b,count_a,count_b+1)
        visited.add((count_a,count_b))  # 避免重复操作

    def C(m,n):  # 计算组合数
        if not n or m==n:
            return 1
        a,b=1,1
        for i in range(n):
            a*=(m-i)
            b*=(i+1)
        return a//b

    get_group(k,0,0)
    # print(groups)  # 所有可能组合
    total = 0
    for count_a, count_b in set(groups):
        # C(x,count_a)*C(y,count_b)
        if count_a>x or count_b >y:
            continue
        total += C(x,count_a)*C(y,count_b)
    return total % 1000000007

k = int(input().strip())
a,x,b,y = map(int, input().strip().split())
print(func(k,a,x,b,y))