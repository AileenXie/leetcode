#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/25 2:50 PM
# @Author : aileen
# @File : 03-1.py
# @Software: PyCharm
import sys


def qSort(lst, start, end):
    """快速排序"""
    if start >= end:
        return
    i = start;
    j = end
    r = lst[i]  # 将lst[i]选做枢轴元素
    while i < j:
        while i < j and lst[j] >= r:
            j -= 1
        if i < j:
            lst[i] = lst[j]
            i += 1
        while i < j and lst[i] <= r:
            i += 1
        if i < j:
            lst[j] = lst[i]
            j -= 1
    lst[i] = r
    qSort(lst, start, i - 1)
    qSort(lst, i + 1, end)


def getMaxPair(lst, n):
    # 数组中所有数字都相等，那么差最大的对就是它们两两组合
    if lst[0] == lst[n - 1]:
        return n * (n - 1) // 2
    # 找出最小的数有多少个
    for i in range(1, n - 1):
        if lst[i] != lst[0]:
            break
    # 找出最大的数有多少个
    for j in range(1, n - 1):
        if lst[n - 1 - j] != lst[n - 1]:
            break
    return i * j


def getMinPair(lst, n):
    # 数组中所有数字都相等，那么差最小的对就是它们两两组合
    if lst[0] == lst[n - 1]:
        return n * (n - 1) // 2
    mincount = 0
    mindiff = lst[1] - lst[0]
    count = 1
    for i in range(1, n - 1):
        # 差为0时对数的计算方法是不一样的，所以跳出
        if mindiff == 0:
            break
        if lst[i + 1] - lst[i] == mindiff:
            count += 1
        elif lst[i + 1] - lst[i] < mindiff:
            mindiff = lst[i + 1] - lst[i]
            count = 1
    if mindiff == 0:
        for i in range(0, n - 1):
            # 找出差为0的段的起始点
            if lst[i + 1] - lst[i] == 0 and (i == 0 or lst[i] - lst[i - 1] > 0):
                start = i
            # 找出差为0的段的终点
            if lst[i + 1] - lst[i] == 0 and (i + 1 == n - 1 or lst[i + 2] - lst[i + 1] > 0):
                end = i + 1
                equalnum = end - start + 1
                # 可能存在多个差为0的子序列，故应分段计算，再把它们相加
                mincount = mincount + equalnum * (equalnum - 1) // 2
        return mincount
    else:
        return count


if __name__ == '__main__':
    while True:
        num = sys.stdin.readline().strip()
        if not num:
            break
        n = int(num)
        line = sys.stdin.readline().strip()
        if not line:
            break  # 这一步不能少，否则退出时会报错
        strlst = line.split(' ')
        lst = list(map(int, strlst))
        qSort(lst, 0, n - 1)
        print(str(getMinPair(lst, n)) + ' ' + str(getMaxPair(lst, n)))
