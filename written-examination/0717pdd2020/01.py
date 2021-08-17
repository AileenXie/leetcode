#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/2 7:14 PM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm

def func(k,n,nums):
    if not k: return "paradox"
    cur = k
    back = 0
    for i,num in enumerate(nums):
        cur-=num
        if cur==0:
            if i<n-1:
                return "paradox"
        elif cur<0:
            cur=-cur
            back+=1
    return str(cur)+" "+str(back)

k,n,nums = 10,4,[6, 3, 3, 3]
k,n,nums = 6,3,[4,2,6]
k,n,nums = 10,2,[6,3]
k,n,nums = 0,2,[6,3]
ans = func(k,n,nums)
print(ans)
