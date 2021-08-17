#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 7:54 PM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm
"""
有n个怪，每个怪消耗ci的血量，打完获得wi的金币。
每个金币能买m个血
问买血策略使得打怪获得最多金币，返回最多金币数（净收入）

case 过了100%

输入
5 2
1 3
2 3
4 5
1 6
2 1

输出
13（打前4个怪）
"""

def func(n,m,c,w):
    dp = [0 for _ in range(n+1)]
    for i in range(n):
        a = -int(-sum(c[:i+1])//m)  # 需要花的金币数，向上取整
        win = sum(w[:i+1])
        dp[i]= win-a
    return max(dp)

import sys
n,m = map(int,sys.stdin.readline().strip().split())
c = []
w = []
for _ in range(n):
    cur_c,cur_w = map(int,sys.stdin.readline().strip().split())
    c.append(cur_c)
    w.append(cur_w)
print(func(n,m,c,w))



