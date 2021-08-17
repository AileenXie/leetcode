#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/12 4:30 PM
# @Author : aileen
# @File : 04.py
# @Software: PyCharm
"""
男女配对，最多几对
第一行是男生编号
第二行是女生编号
第三行是已初步配对的个数n
后面n行是配对情况
每人最多约会1次，最多几对约会
0 1 2
3 4 5
6
0 4
0 3
1 3
1 4
2 5
2 4

3
"""
male = list(map(int, input().strip().split()))
female = list(map(int, input().strip().split()))
n = int(input().strip())
pair = []  # 记录配对
dic = {}  # 记录每个人的可选对象
count = {}  # 记录每个人的可选对象个数
for _ in range(n):
    a, b = map(int, input().split())
    pair.append((a, b))
    dic.setdefault(a, []).append(b)
    dic.setdefault(b, []).append(a)
for i in dic:
    count[i] = len(dic[i])


def func(pair, count):
    c=0
    # print(pair)
    # print(count)
    while pair:
        pair.sort(key=lambda x: (min(count[x[0]],count[x[1]]),count[x[0]]+count[x[1]]))
        cur=pair[0]
        count[cur[0]]-=1
        count[cur[1]]-=1
        new_pair=[]
        for p in pair:  # 更新剩余配对
            if p[0]==cur[0] or p[0]==cur[1] or  p[1]==cur[0] or p[1]==cur[1]:
                continue
            new_pair.append(p)
        pair=new_pair
        c+=1
    return c

print(func(pair,count))