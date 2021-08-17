#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/9 9:50 PM
# @Author : aileen
# @File : real01.py
# @Software: PyCharm

"""
判断[0,a]内，二进制表示中有连续1的数的个数

"""
class Solution:
    def find(self , a):
        count = 0
        for cur in range(1,a+1):
            cur_bak = cur
            bit = cur&(-cur)  # 获得最右一个1
            while bit<=cur_bak:
                cur = cur^bit  # 去掉最右1
                if cur == 0: break
                next_bit = cur&(-cur)
                if next_bit == 2*bit:
                    count += 1
                    break
        return count

