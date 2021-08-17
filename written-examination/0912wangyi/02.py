#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/12 2:53 PM
# @Author : aileen
# @File : 02.py
# @Software: PyCharm
"""
长度大于1的回文子串个数

abbcbb

4
"""
s=input()
def func(s):
    n=len(s)
    count=0
    if n<=1: return 0
    dp=[[0 for _ in range(n)]for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(i,n):
            if i==j:  # 长度为1
                dp[i][j]=1
            elif i+1==j:  # 长度为2
                if s[i]==s[j]:
                    dp[i][j]=1
                    count+=1
            elif s[i]==s[j] and dp[i+1][j-1]:  # 长度>2
                dp[i][j]=1
                count+=1
    return count

print(func(s))