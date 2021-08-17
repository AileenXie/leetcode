#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 3:07 PM
# @Author : aileen
# @File : 03多重背包问题i.py
# @Software: PyCharm

"""
f(0)=A
f(1)=B
f(i)=f(i-1)+f(i-2)
问第n个数能不能被3整除

输入：
T：用例数
T行，每行：A,B,n

3
1 1 3
1 1 4
7 11 2

YES
NO
YES

50%
"""


def func(a,b,n):
    dp=[0,a,b]
    for i in range(1,n):
        dp[0],dp[1]=dp[1],dp[2]
        dp[2]=dp[0]+dp[1]
    if dp[2]%3:
        return "NO"
    else:
        return "YES"



T = int(input().strip())
for _ in range(T):
    a,b,n = map(int, input().strip().split())
    print(func(a,b,n))