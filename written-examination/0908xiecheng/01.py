#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/8 7:00 PM
# @Author : aileen
# @File : 01.py
# @Software: PyCharm

m, n = map(int, input().strip().split())


def func(m, n):
    if not m or not n: return []
    if m==1:
        ans=[i for i in range(1,n+1)]
        return [ans]
    if n==1:
        ans=[[i] for i in range(1,m+1)]
        return ans
    ans = [[0 for _ in range(n)]for _ in range(m)]
    # 斜向上走
    def go(i,j,num):
        # print(i,j,num)
        ans[i][j]=num
        last_num=num
        if i>0 and j<n-1:
            last_num = go(i-1,j+1,num+1)
        return last_num
    last_num=0
    for i in range(m):
        # print(f"____{i},0")
        last_num = go(i,0,last_num+1)
    for j in range(1,n):
        # print(f"____{m-1},{j}")
        last_num = go(m-1,j,last_num+1)
    return ans

print(func(m,n))




