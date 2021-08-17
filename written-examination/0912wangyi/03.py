#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/12 2:53 PM
# @Author : aileen
# @File : 03.py
# @Software: PyCharm
"""
最长子串长度，子串中abcxyz个数都是偶数个（包括0）
amabc

3
"""
s = input().strip()
def func(s):
    dic = {"a":5,"b":4,"c":3,"x":2,"y":1,"z":0}
    n=len(s)
    sta=0
    prex=[0]*(n+1)
    for i in range(n):
        if s[i] in dic:
            sta^=(1<<dic[s[i]])
        prex[i+1]=sta
    max_len=1
    # print(prex)
    visited={}  # O(n)的方法
    for i in range(n+1):  # 从0-n
        if prex[i] in visited:
            max_len=max(max_len, i-visited[prex[i]])
        else:
            visited[prex[i]]=i
        # for j in range(i+1,n+1):  # O(n^2)的方法
            # cur_len=j-i
            # if prex[j]^prex[i]==0:
            #     max_len=max(cur_len,max_len)
            #     # print(cur_len,i,j)
    return max_len
print(func(s))