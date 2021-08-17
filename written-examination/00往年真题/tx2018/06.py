#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 3:27 PM
# @Author : aileen
# @File : 06.py
# @Software: PyCharm

"""
画家小Q又开始他的艺术创作。小Q拿出了一块有NxM像素格的画板, 画板初始状态是空白的,用'X'表示。
小Q有他独特的绘画技巧,每次小Q会选择一条斜线,
如果斜线的方向形如'/',即斜率为1,小Q会选择这条斜线中的一段格子,都涂画为蓝色,用'B'表示;
如果对角线的方向形如'\',即斜率为-1,小Q会选择这条斜线中的一段格子,都涂画为黄色,用'Y'表示。
如果一个格子既被蓝色涂画过又被黄色涂画过,那么这个格子就会变成绿色,用'G'表示。
小Q已经有想画出的作品的样子, 请你帮他计算一下他最少需要多少次操作完成这幅画。

输入描述:
每个输入包含一个测试用例。
每个测试用例的第一行包含两个正整数N和M(1 <= N, M <= 50), 表示画板的长宽。
接下来的N行包含N个长度为M的字符串, 其中包含字符'B','Y','G','X',分别表示蓝色,黄色,绿色,空白。整个表示小Q要完成的作品。

输出描述:
输出一个正整数, 表示小Q最少需要多少次操作完成绘画。

输入例子1:
4 4
YXXB
XYGX
XBYY
BXXY

输出例子1:
3

例子说明1:
XXXX
XXXX
XXXX
XXXX
->
YXXX
XYXX
XXYX
XXXY
->
YXXB
XYBX
XBYX
BXXY
->
YXXB
XYGX
XBYY
BXXY
"""
import sys


def func(grid,n,m):
    count = 0

    def draw_y(p,q):
        while p < n and q < m and (grid[p][q] == "Y" or grid[p][q] == "G"):
            if grid[p][q] == "Y":
                grid[p][q] = "X"  # 逆向画回去
            if grid[p][q] == "G":
                grid[p][q] = "B"  # 逆向画回去
            p += 1
            q += 1

    def draw_b(p,q):
        while p < n and q >= 0 and (grid[p][q] == "B" or grid[p][q] == "G"):
            if grid[p][q] == "B":
                grid[p][q] = "X"  # 逆向画回去
            if grid[p][q] == "G":
                grid[p][q] = "Y"  # 逆向画回去
            p += 1
            q -= 1
    for i in range(n):
        for j in range(m):
            # 遇到Y就向右下方画，直到遇到X或B
            if grid[i][j]=="Y":
                draw_y(i,j)
                count += 1
            # 遇到B就向右下方画，直到遇到X或Y
            if grid[i][j]=="B":
                draw_b(i,j)
                count += 1
            # 遇到G就向右下方画一次，再向左下方画一次
            if grid[i][j] == "G":
                draw_b(i,j)
                draw_y(i,j)
                count += 2
    return count


n,m = map(int,sys.stdin.readline().split())
grid = []
for _ in range(n):
    row = [i for i in sys.stdin.readline().strip()]
    grid.append(row)
print(func(grid,n,m))