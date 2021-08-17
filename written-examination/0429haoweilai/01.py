#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/29 6:45 PM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm
"""
最长回文子串
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
给定一个字符串 s，找到 s 中最长的回文子串。 s 的最大长度为 1000。（回文串：是说一个从左边读和从右度边读的结果是一模一样的，比如12321）

输入
输入: "babad"

输出
输出: "bab"。(注意: "aba" 也是一个有效答案)


样例输入
abcca
样例输出
cc
"""

def func(s):
    n = len(s)
    if n < 2:
        return s
    if n == 2:
        return s if s[0]==s[1] else s[0]
    s2 = list(s)
    s2.reverse()
    s2 = "".join(s2)
    max_len = -float('inf')
    end = 0

    dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end = i
    return s[end-max_len:end]

s = input().strip()
print(func(s))