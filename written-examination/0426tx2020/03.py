#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 7:54 PM
# @Author : aileen
# @File : 03多重背包问题i.py
# @Software: PyCharm
"""
n个房间，每个房间一个人
每个人从[1,m]选数字，相邻房间的人若选择相同数字，则产生冲突
问所有产生冲突的情况有多少种
结果对10003取余

case通过 30%

输入
2 3

输出
6
"""
def func(m, n):
    # m 数字范围，n 房间数
    total = m ** n
    not_conflit = m*(m - 1)**(n-1)
    ans = total - not_conflit
    return ans % 100003


m, n = map(int, input().strip().split())
print(func(m, n))
