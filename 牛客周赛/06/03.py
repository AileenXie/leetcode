#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/30 10:02 PM
# @Author : aileen
# @File : 03多重背包问题i.py
# @Software: PyCharm

class Solution:
    def nthElement(self , n , b , c ):
        # write code here
        i=2
        dp=[0]*(n+1)
        dp[1]=1
        while i<=n:
            dp[i]=b*dp[i-1]+c*dp[i-2]
            i+=1
        print(dp)
        return dp[-1]%(10**9+7)

print(Solution().nthElement(5,1,2))