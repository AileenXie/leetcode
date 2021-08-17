#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/17 8:31 PM
# @Author : aileen
# @File : 03.py
# @Software: PyCharm
"""
2
5 5
2 2
1 5 25 125
ooooo
oxxxo
oxooo
oxxxo
ooooo
5 5
2 2
0 0 0 0
ooooo
oxxxo
oxoxo
oxxxo
ooooo

560
-1
"""
import functools


def func(n,m,x,y,cost,matrix):
    # print(matrix)
    s,e=(0,0),(x,y)
    @functools.lru_cache(None)
    def dfs(i,j):
        if (i,j)==e:
            return 0
        if i>=n or i<0 or j>=m or j<0:
            return float('inf')
        if matrix[i][j]=="x" or matrix[i][j]=="V":
            return float('inf')
        ori=matrix[i][j]
        matrix[i][j]="V"
        min_cost=min(dfs(i+1,j)+cost[1],dfs(i-1,j)+cost[0],dfs(i,j+1)+cost[3],dfs(i,j-1)+cost[2])
        matrix[i][j]=ori
        return min_cost
    ans = dfs(s[0], s[1])
    return ans if ans!=float("inf") else -1


t=int(input().strip())
for _ in range(t):
    matrix=[]
    n,m=map(int,input().strip().split())
    x,y=map(int,input().strip().split())
    abcd=list(map(int,input().strip().split()))
    for i in range(n):
        row=list(input().strip())
        matrix.append(row)
    print(func(n,m,x,y,abcd,matrix))



