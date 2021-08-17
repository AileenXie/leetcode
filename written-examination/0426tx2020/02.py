#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 9:42 PM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm
"""
计算 x^2=2Ay 与 x=By+C 闭区间的面积，不闭合返回0
case 过了0%（可能提交的时候没写b==0的判断）

输入
2
1 1 -7
1 0 3

输出
38.72983346207417
0
"""
import math


def func(a, b, c):
    if b * c > 0 or b == 0:  # b=0是一条x=C的竖线
        return 0
    xx = math.sqrt(4 * a * (a - 2 * b * c) / (b * b))
    x1 = (2 * a / b + xx) / 2
    x2 = (2 * a / b - xx) / 2
    y1 = x1 * x1 / (2 * a)
    y2 = x2 * x2 / (2 * a)

    S1 = 0.5 * abs(x1 - x2) * (y1 + y2)
    t = max(x1, x2)
    d = min(x1, x2)
    S2 = (t ** 3 - d ** 3) / (6 * a)
    return S1 - S2


n = int(input().strip())
for _ in range(n):
    a, b, c = map(int, input().strip().split())
    print(func(a, b, c))
