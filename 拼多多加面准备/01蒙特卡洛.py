#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/15 7:44 AM
# @Author : aileen
# @File : 01蒙特卡洛.py
# @Software: PyCharm
"""
蒙特卡罗方法(Monte Carlo method)也称统计模拟方法
一种以概率统计理论为指导的数值计算方法。是指使用随机数（或更常见的伪随机数）来解决很多计算问题的方法

通常蒙特卡罗方法可以粗略地分成两类：
一类是所求解的问题本身具有内在的随机性，借助计算机的运算能力可以直接模拟这种随机的过程
另一种类型是所求解问题可以转化为某种随机分布的特征数，比如随机事件出现的概率，或者随机变量的期望值。
通过随机抽样的方法，以随机事件出现的频率估计其概率，或者以抽样的数字特征估算随机变量的数字特征，并将其作为问题的解。
————  这种方法多用于求解复杂的多维积分问题。
"""
import random

"""
蒙特卡洛求π
"""
def calpai():
    n = 1000000
    r = 1.0
    a, b = (0.0, 0.0)
    x_neg, x_pos = a - r, a + r
    y_neg, y_pos = b - r, b + r

    count = 0
    for i in range(0, n):  # 随机在单位元外切正方形（2x2）区域内撒点
        x = random.uniform(x_neg, x_pos)
        y = random.uniform(y_neg, y_pos)
        if x*x + y*y <= 1.0:  # 在圆内的点数
            count += 1

    return (count / n) * 4


def func(a,b):
    """
    求∫_a^b x^2 dx的值
    """
    n=1000000
    x,y=0,0
    count=0
    for i in range(n):
        x=random.uniform(a,b)
        y=x**2
        count+=y
    return (count/n)*(b-a)


def func0(a,b):
    """
    精确解法
    """
    aa=1/3
    bb=aa*(b**3)-aa*(a**3)
    return bb


# print(calpai())
print(func(0,1))
print(func0(0,1))