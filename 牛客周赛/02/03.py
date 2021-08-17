#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 9:47 PM
# @Author : aileen
# @File : 03多重背包问题i.py
# @Software: PyCharm
class Solution:
    def solve(self , n , m , k ):
        # write code here
        if not k or m*n<k: return 0
        def C(n,x):
            if not x: return 1
            if x>n: return 0
            a,b=n,x
            while (x-1):
                a*=(n-1)
                b*=(x-1)
                n,x=n-1,x-1
            return a//b
        if k<2: return 0
        ans = C(m*n,k)-2*C(m*n-m,k)-2*C(m*n-n,k)
        return ans%(10**9+7)

if __name__ == "__main__":
    print(Solution().solve(2,3,1))
    print(Solution().solve(2,2,2))
    print(Solution().solve(100,4,2))