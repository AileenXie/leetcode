#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/2 8:25 PM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm
"""
输入n个骰子
每个骰子有【上，下，左，右，前，后】6个值 ∈ {1,2,3,4,5,6}

输出总共有多少种骰子，每种骰子有多少个（降序排列）

如：
n = 3
rows=[[1,2,3,4,5,6],  # A
      [1,2,6,5,3,4],  # A
      [1,2,6,5,4,3]]  # B

输出：
2
2 1
"""


def func(n, rows):

    def match(a, b):
        base = (a[0], a[1])
        base2 = [(b[0], b[1]), (b[2], b[3]), (b[4], b[5])]
        base2_r = [(b[1], b[0]), (b[3], b[2]), (b[5], b[4])]
        re = None
        for j in range(3):
            if base == base2[j]:
                re=(j,1)  # 正向匹配
            elif base == base2_r[j]:
                re=(j,0)  # 反向匹配

        if not re: return False
        j,flag = re
        if j == 0:
            if not flag:
                to_com = [b[2],b[3],b[5],b[4]]
            else:
                to_com = b[2:]
        elif j==1:
            if not flag:
                to_com = [b[0],b[1],b[4],b[5]]
            else:
                to_com = [b[1],b[0],b[4],b[5]]
        else:
            if not flag:
                to_com = [b[2],b[3],b[0],b[1]]
            else:
                to_com = [b[2],b[3],b[1],b[0]]
        com = a[2:]

        # 左右前后 ——> 左前右后
        com = [com[0],com[2],com[1],com[3]]
        to_com = [to_com[0],to_com[2],to_com[1],to_com[3]]
        p,q=0,0
        while to_com[q]!=com[p]:
            q+=1
        step=0
        while step<4:
            if com[p]==to_com[q]:
                p = p+1 if p+1<4 else 0
                q = q+1 if q+1<4 else 0
                step+=1
            else: return False
        return True
    count = [1]
    kind = [rows[0]]
    for i in range(1,n):
        flag = False
        for j in range(len(kind)):
            if match(kind[j],rows[i]):
                count[j]+=1
                flag =True
                break
        if not flag:
            kind.append(rows[i])
            count.append(1)

    count.sort(reverse=True)
    return len(count),count

# n = 2
# rows=[[1,2,3,4,5,6],[1,2,6,5,3,4]]
n = 3
rows=[[1,2,3,4,5,6],
      [1,2,6,5,3,4],
      [1,2,6,5,4,3]]

k,count = func(n,rows)
print(k)
print(" ".join(list(map(str,count))))


