#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/24 8:40 AM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm
"""
n个数a1,a2,..an，选其中一些数求和并对m取余，
得到的结果中最大的组合结果是什么

第一行：n-数组长度，m-取余基数
输出：取余最大的结果

输入：
5 6
1 3 6 5 7

输出：
5

输入
4 7
1 3 4 3

输出
6   用DP这里只会输出5

输入：
6 11
4 12 3 7 6 2
输出：
10
"""
n,m = map(int, input().split())
a = list(map(int, input().split()))

# def get_max_result(n,m,a):
#     """
#     case 通过 5%
#     """
#     if n == 1:
#         return a[0] % m
#     dp= [0 for _ in range(n)]
#     dp[0] = a[0] % m
#     for i in range(n):
#         for j in range(i):
#             dp[i] = max([dp[j], (dp[j]+a[i])%m, dp[i]])
#     print(dp)
#     return dp[-1]


# 这道题用dp不行，前面取模较小的数可能和后面数组合成更大的数，不能直接抛弃
def get_max_result(n,m,a):
    """
    DFS
    """
    max_ans = a[0] % m
    if n == 1:
        return max_ans
    stack = [(a[0],a[1:])]
    while stack:
        cur_sum,available=stack.pop()
        cur_ans = cur_sum % m
        if cur_ans> max_ans:
            max_ans = cur_ans
        for num in available:
            new_available = available.copy()
            new_available.remove(num)
            stack.append(cur_sum+num,new_available)



print(get_max_result(n,m,a))