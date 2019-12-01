#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/29 10:58 PM
# @Author : aileen
# @File : 069_sqrt.py
# @Software: PyCharm

"""
Implement int sqrt(int x).

Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since
             the decimal part is truncated, 2 is returned.
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1:
            return 1
        left = 1
        right = x
        return self._mysqrt(left, right, x)

    def _mysqrt(self,left,right,x):
        mid = (left + right)//2
        cur = mid*mid
        if cur == x or (cur<x and (mid+1)*(mid+1)>x):
            return mid
        if cur < x:
            return self._mysqrt(mid, right, x)
        else:
            return self._mysqrt(left, mid, x)


if __name__ == '__main__':
    result = Solution().mySqrt(403)
    print(result)