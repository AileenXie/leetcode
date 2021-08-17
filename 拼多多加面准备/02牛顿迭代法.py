#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/15 8:13 AM
# @Author : aileen
# @File : 02牛顿迭代法.py
# @Software: PyCharm
"""
牛顿迭代法是一种可以用来快速求解函数零点的方法。
牛顿迭代法的本质是借助泰勒级数，从初始值开始快速向零点逼近。

递推式：
x(n+1)=x(n)－f(x(n))/f'(x(n))
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        l, r, ans = 0, x, -1
        while l <= r:
            mid = (l + r) // 2
            if mid * mid <= x:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    def mySqrt2(self,num):
        """
        求根号sqrt(num)实际上是求函数：
        f(x)=x ^ 2 -num = 0 时的x取值
        f'(x)=2x
        x(n+1)=x(n)－f(x(n))/2x
        """
        x=num
        while True:
            xx=x-(x*x-num)/(2*x)
            if abs(xx - x) < 1e-7: break
            x=xx
        return x

print(Solution().mySqrt(8))
print(Solution().mySqrt2(8))