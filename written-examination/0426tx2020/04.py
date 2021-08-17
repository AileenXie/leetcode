#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 8:52 PM
# @Author : aileen
# @File : 04多重背包问题ii.py
# @Software: PyCharm
# a= [1,2,3]
# b = [3,4,5]
# print([i+j for i,j in zip(a,b)])
"""
有n个物体{a1,a2...an}，每个物体k维特征(a11,a12,...a1k)
若两个物体每维特征相加都相等（ai1+aj1 = ai2+aj2 = ...）
则称这两个物体对称
问有多少对称

testcase通过30%

输入
4 5
1 2 3 4 5
5 4 3 2 1
4 3 2 1 0
1 3 5 7 9

输出
2
"""
def func(n, k, A):
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if len(set([i + j for i, j in zip(A[i], A[j])])) == 1:
                count += 1
    return count


n, k = map(int, input().strip().split())
A = []
for _ in range(n):
    a = list(map(int, input().strip().split()))
    A.append(a)
print(func(n, k, A))