#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/15 10:15 AM
# @Author : aileen
# @File : test.py
# @Software: PyCharm


# visited = [[0]*4]*5
# visited=[[0,0,0],[0,0,0]]
# visited=[[0 for col in range(4)] for row in range(5)]
# visited = [0]*4
# visited[0]=1
# print(visited)


a = [1,2,3,4]
b = [a[i]+1 for i in range(len(a))]
print(b)

print(min(1,2))
print(sum(a))
print(a+[3,4])
print(1e9 + 7 == 10**9+7)


print(583438149971672%(1e9+7))