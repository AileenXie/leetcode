#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/20 3:05 PM
# @Author : aileen
# @File : 01conv.py
# @Software: PyCharm

# 4 5 3 3
# h(i,j)=i*j mod 10。(1<=i<=n,1<=j<=m)
"""
滑动窗口
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
在机器学习中有一种流行的池化操作，而在池化操作中，3*3极大值池化应用十分广泛。什么是3*3极大值池化呢？设原矩阵是n*m的，则3*3极大值池化就是枚举矩阵中的所有3*3的子矩阵,分别求最大值并顺次拼接而成，处理过后的矩阵是(n-2)*(m-2)。

例如，原矩阵是[[1,2,3,4],[5,6,7,8],[9,10,11,12]],经过池化之后就变成[[11,12]]。

为了提高难度，选择的滑动窗口并不是3*3的，而是a*b的，由于输入可能是非常大的，原n*m的矩阵权值由以下公式计算得到，h(i,j)=i*j mod 10。(1<=i<=n,1<=j<=m)

由于输出矩阵也是一个很麻烦的事情，因此你只需输出经过a*b池化处理后的矩阵的元素之和即可。

输入
输入第一行包含四个正整数，n,m,a,b，分别表示原矩阵的行列数量和滑动窗口的行列数量。(1<=n,m,a,b<=1000)

输出
输出仅包含一个整数，即新矩阵的元素之和。


样例输入
4 5 3 3
样例输出
54
"""

def conv(n, m, a, b):
    def get_max(start):
        x,y = start
        cur_max = -float('inf')
        for p in range(a):
            for q in range(b):
                cur_max = max(grid[x+p][y+q],cur_max)
        return cur_max
    box = [(0,0),(0,b-1),(a-1,0),(a-1, b-1)]
    grid = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(b):
            grid[i][j] = (i+1)*(j+1)%10
    print(grid)
    ans = 0
    ans_n = n-a+1
    ans_m = m-b+1
    for i in range(ans_n):
        for j in range(ans_m):
            ans += get_max((i,j))
    return ans

print(conv(4,5,3,3))

