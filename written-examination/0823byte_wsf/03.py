#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 11:10 AM
# @Author : aileen
# @File : 03.py
# @Software: PyCharm

class Solution:
    def func(self,n,t,m,w):
        if not n or not m: return 0
        if m > t-1: return -1
        count = m
        stop=[w[0]-ii+t for ii in range(m,0,-1)]
        for i,now in enumerate(w[1:],1):
            early_stop=stop[0]
            if now<=early_stop:
                continue
            else:
                later=0
                for k in stop:
                    if now<=k: break
                    later+=1
                count+=later
                if later<=m:
                    stop=stop[later:]
                else:
                    stop=[]
                stop = stop+[now - ii + t for ii in range(later, 0, -1)]
        return count


print(Solution().func(2,5,2,[1,2]))
print(Solution().func(1,1,10,[1]))
print(Solution().func(3,5,3,[1,3,6]))
print(Solution().func(3,5,3,[1,4,6]))
print(Solution().func(3,5,3,[1,5,7]))
