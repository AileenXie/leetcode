#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 9:17 AM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm

"""
小Q的父母要出差N天，走之前给小Q留下了M块巧克力。小Q决定每天吃的巧克力数量不少于前一天吃的一半，但是他又不想在父母回来之前的某一天没有巧克力吃，请问他第一天最多能吃多少块巧克力

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数，表示父母出差的天数N(N<=50000)和巧克力的数量M(N<=M<=100000)。

输出描述:
输出一个数表示小Q第一天最多能吃多少块巧克力。

输入例子1:
3 7

输出例子1:
4
"""


def func(n, m):
    valid = []

    def get_num(l, r):  # 二分判断
        if l > r:
            return
        mid = (l + r) // 2
        total = 0
        for i in range(n):
            cur = -int(-mid * (0.5) ** i // 1)  # 向上取整，//操作是向下取整返回float，int是向0化分为整
            total += cur if cur > 1 else 1
            if total > m:  # 吃太多了
                get_num(l, mid - 1)
                return
        valid.append(mid)
        get_num(mid + 1, r)

    get_num(0, m)
    return max(valid)


n, m = map(int, input().strip().split())
print(func(n, m))