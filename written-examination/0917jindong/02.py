#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/17 7:58 PM
# @Author : aileen
# @File : 02.py
# @Software: PyCharm
"""
用例数t
行列n,m
格子值： S-开始 E-结束 #-障碍 .-通行

返回能不能从S到E

2
2 2
.E
S.
2 2
#E
S#

YES
NO
"""

def func(n,m,matrix):
    # print(matrix)
    s,e=None,None

    for i in range(n):
        for j in range(m):
            # print(i,j)
            if matrix[i][j]=="S":
                s=(i,j)
            elif matrix[i][j]=="E":
                e=(i,j)
    if not s or not e: return "NO"
    def dfs(i,j):
        if (i,j)==e:
            return True
        if i>=n or i<0 or j>=m or j<0:
            return False
        if matrix[i][j]=="#" or matrix[i][j]=="V":
            return False
        ori=matrix[i][j]
        matrix[i][j]="V"
        if dfs(i+1,j): return True
        if dfs(i-1,j): return True
        if dfs(i,j+1): return True
        if dfs(i,j-1): return True
        matrix[i][j]=ori
        return False
    return "YES" if dfs(s[0],s[1]) else "NO"


t=int(input().strip())
for _ in range(t):
    matrix=[]
    n,m=map(int,input().strip().split())
    for i in range(n):
        row=list(input().strip())
        matrix.append(row)
    print(func(n,m,matrix))