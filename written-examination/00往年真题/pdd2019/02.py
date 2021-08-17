#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 11:11 AM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm
"""
小多想在美化一下自己的庄园。他的庄园毗邻一条小河，他希望在河边种一排树，共 M 棵。小多采购了 N 个品种的树，每个品种的数量是 Ai (树的总数量恰好为 M)。但是他希望任意两棵相邻的树不是同一品种的。小多请你帮忙设计一种满足要求的种树方案。

输入描述:
第一行包含一个正整数 N，表示树的品种数量。
第二行包含 N 个正整数，第 i (1 <= i <= N) 个数表示第 i 个品种的树的数量。
数据范围：
1 <= N <= 1000
1 <= M <= 2000

输出描述:
输出一行，包含 M 个正整数，分别表示第 i 棵树的品种编号 (品种编号从1到 N)。若存在多种可行方案，则输出字典序最小的方案。若不存在满足条件的方案，则输出"-"。

输入例子1:
3
4 2 1

输出例子1:
1 2 1 2 1 3 1
"""

n = int(input().strip())
A = list(map(int,input().strip().split()))

def func(n,A):
    m = sum(A)
    # 排序后的品种对应编号
    index = [i for i,_ in sorted(enumerate(A),key=lambda x:(x[1],x[0]),reverse=True)]
    numbers = sorted(A,reverse=True)
    dic = {i:numbers for i,numbers in zip(index,numbers)}
    # 判断可行性
    if numbers[0] > numbers[1:]+1:
        return "-"
    # def dfs(res,path):

