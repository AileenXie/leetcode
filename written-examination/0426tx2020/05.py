#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 9:11 PM
# @Author : aileen
# @File : 05混合背包问题.py
# @Software: PyCharm
"""
T个test case
n对关系（x,y）表示x,y属于同一集合，若有（z,x）则x,y,z都属于同一集合
输出集合最大包含元素数

2
4
1 3
2 4
4 5
2 6
4
1 2
3 4
5 7
4 6

输出
4
3

"""
def func(n, relation):
    relation.sort()
    relation2 = sorted(relation,key=lambda x:x[1])
    print(relation)
    print(relation2)
    start, end = relation[0]
    cur_group = set()
    cur_group.add(start)
    cur_group.add(end)
    groups = [cur_group]
    group_num = [2]
    for i, j in relation[1:]:
        flag = False
        for g,cur_group in enumerate(groups):
            if i in cur_group or j in cur_group:  # 与当前范围有交集
                flag = True
                if i not in cur_group:
                    cur_group.add(i)
                    group_num[g]+=1
                if j not in cur_group:
                    cur_group.add(j)
                    group_num[g] += 1
                break
        if not flag:  # 无交集
            cur_group = set()
            cur_group.add(i)
            cur_group.add(j)
            groups.append(cur_group)
            group_num.append(2)
    return max(group_num)


T = int(input().strip())
for _ in range(T):
    n = int(input().strip())  # n对关系
    relation = []
    for i in range(n):
        x, y = map(int, input().strip().split())
        if x < y:
            relation.append((x, y))  # 小的放前面
        else:
            relation.append((y, x))
    print(func(n, relation))


