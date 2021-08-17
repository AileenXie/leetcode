#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/22 5:21 PM
# @Author : aileen
# @File : LSC.py
# @Software: PyCharm

str1 = input()
str2 = input()

def min_modify(str1,str2):
    m = len(str1)
    n = len(str2)
    dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
    for i in range(0, m):
        for j in range(0, n):
            if str1[i] == str2[j]:
                dp[i+1][j+1] = dp[i][j]+1
            else:
                dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
    same_num = dp[-1][-1]
    print(same_num)
    return max(m,n)-same_num

print(min_modify(str1, str2))
