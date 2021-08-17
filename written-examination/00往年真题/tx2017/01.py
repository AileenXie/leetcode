#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/25 7:58 AM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm

"""
给定一个字符串s，你可以从中删除一些字符，使得剩下的串是一个回文串。如何删除才能使得回文串最长呢？
输出需要删除的字符个数。

输入描述:

输入数据有多组，每组包含一个字符串s，且保证:1<=s.length<=1000.



输出描述:

对于每组数据，输出一个整数，代表最少需要删除的字符个数。


输入例子1:
abcda
google

输出例子1:
2
2
"""
import sys
def func(s):
    n = len(s)
    if n<2:
        return 0
    s2=s[::-1]
    dp = [[0 for _ in range(n+1)] for _ in range(2)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if s[i-1] == s2[j-1]:
                dp[i%2][j] = dp[(i-1)%2][j-1]+1
            else:
                dp[i%2][j] = max(dp[(i-1)%2][j], dp[i%2][j-1])
    return n-dp[i%2][-1]


# OK
for line in sys.stdin:
    s = line.strip()
    print(func(s))

# # OK
# import sys
# s = sys.stdin.readline().strip()
# while s != "":  # while not s 也不行
#     print(func(s))
#     s = sys.stdin.readline().strip()

# # NOT OK
# while True:
#     s = input()
#     if not s:
#         break
#     print(func(s))
