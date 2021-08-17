#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/24 8:41 AM
# @Author : aileen
# @File : 03多重背包问题i.py
# @Software: PyCharm
import sys
"""
问从S位置到X位置能否在限定时间t内走到
遇到C，1格/s
遇到.，2格/s
遇到O，过不去

能在规定时间内走到：输出YES并输出所花费的时间
不能再规定时间内走道：输出NO

第一行：T-testcase个数
第二行：n-表格维数nxn,t-限定时间
后n行：表格内容

case 过了0%，提示超时【line72速度写成2了，其实是0.5】

输入：
3
2 3
.X
S.
2 3
.X
SC
2 4
.X
S.

输出：
NO
YES
3
YES
4
"""


def S_to_X(grid,n,start,end,t):
    if start is None or end is None:
        print("NO")
        return
    print(start,end)
    stack = [(start,0,[])]
    cost_time = []
    while stack:
        (i,j),time,visited = stack.pop()
        print(f'{i},{j}')
        if i < 0 or i >=n or j <0 or j>=n:
            print("出界")
            continue
        if time > t:
            print("超时，当前用时{}".format(time))
            continue
        if (i,j) in visited:
            print("已访问")
            continue
        if (i,j)==end:
            print("到达！~，耗时{}".format(time))
            cost_time.append(time)
            continue
        if grid[i][j] == "O":
            print("此路不通")
            continue
        new_visited=visited.copy()
        new_visited.append((i,j))
        cost = 1 if grid[i][j]=="C" else 0.5  # !!!用时写错了，2格/s->1格是0.5秒啊！
        stack.append(((i + 1, j), time + cost, new_visited))
        stack.append(((i - 1, j), time + cost, new_visited))
        stack.append(((i, j + 1), time + cost, new_visited))
        stack.append(((i, j - 1), time + cost, new_visited))
    if not cost_time:
        print("NO")
    else:
        print("YES")
        print(min(cost_time))
    return 0

T = int(input())
for _ in range(T):
    n, t = map(int, input().split())
    grid = []
    start = None
    end = None
    for i in range(n):
        row = input()
        # print(row)
        for j,s in enumerate(row):
            if s == "S":
                start = (i,j)
            if s == "X":
                end = (i,j)
        grid.append(row)
    # print(grid)
    S_to_X(grid,n,start,end,t)
