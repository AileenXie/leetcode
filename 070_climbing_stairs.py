#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/1 12:34 PM
# @Author : aileen
# @File : 070_climbing_stairs.py
# @Software: PyCharm

"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

# 计算叶子节点+记忆搜索
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1
        sum = [None for _ in range(n+1)]
        return self._climbstairs(n, sum)

    def _climbstairs(self, n, sum):
        if n == 0 or n == 1:
            return 1
        if sum[n] is None:
            sum[n] = self._climbstairs(n - 1, sum) + self._climbstairs(n - 2, sum)
        return sum[n]


if __name__ == '__main__':
    result = Solution().climbStairs(200)
    print(result)
