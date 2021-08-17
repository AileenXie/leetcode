#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 2:22 PM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm

"""
木棍拼正方形，能不能拼？
输入：
T: 用例数目
T行，每行：n l1,l2,...ln

3
4 1 1 1 1
5 1 1 1 1 2
8 1 1 1 1 2 2 4 4

YES
NO
YES

2
5 3 3 3 3 4
12 5 5 5 5 4 4 4 4 3 3 3 3

NO
YEW

0%


"""

def func(n, L):
    if n < 4:
        return "NO"
    total = sum(L)
    print(total)
    if total%4:  # 不能整除
        return "NO"
    a = total // 4  # 边长
    dic = {}
    for l in L:
        dic.setdefault(l,0)
        dic[l] += 1
    exist = list(dic.keys())
    exist.sort(reverse=True)
    total_a = 4

    for index,key in enumerate(exist):  # 从大到小
        if dic[key]==0:
            continue
        if key > a:
            return "NO"
        if key==a:
            while dic[key]:
                total_a -=1  # 构成一条边
                dic[key]-=1
            continue
        if key < a:  # 需要补边
            # group(a-key, index)
            while dic[key]:
                dic[key]-=1
                rest = a - key
                start = index
                while rest:
                    if start >= len(exist):
                        return "NO"
                    cur_l = exist[start]
                    need = rest//cur_l
                    if need<=dic[cur_l]:
                        rest=rest%cur_l
                        dic[cur_l]-=need
                    else:
                        rest -= dic[cur_l]*cur_l
                        dic[cur_l]=0
                    start+=1
                total_a -= 1
    if total_a == 0:
        return "YES"
    else:
        return "NO"



T = int(input().strip())
for _ in range(T):
    line = list(map(int, input().strip().split()))
    n = line[0]
    L = line[1:]
    print(func(n, L))









