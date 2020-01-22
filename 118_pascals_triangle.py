#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/01/19 14:46 PM
# @Author : aileen
# @File : 118_pascals_triangle.py
# @Software: PyCharm

"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution:
    """
    思路一：上一行两个值相加
    """
    # def generate(self, numRows: int):
    #     if numRows == 0:
    #         return []
    #     if numRows == 1:
    #         return [[1]]
    #     result = [[1]]
    #     for k in range(1, numRows):
    #         self.generate_line(result, k)
    #     return result
    # def generate_line(self, result, n):
    #     cur_line = []
    #     pre_line = result[n-1]
    #     for i in range(n+1):
    #         a, b = i-1, i
    #         left = 0 if a < 0 else pre_line[a]
    #         right = 0 if b >= n else pre_line[b]
    #         cur_line.append(left+right)
    #     result.append(cur_line)
    """
    思路二：
    explanation: Any row can be constructed using the offset sum of the previous row. Example:
        1 3 3 1 0 
     +  0 1 3 3 1
     =  1 4 6 4 1
    """
    def generate(self, numRows):
        res = [[1]]
        for i in range(1, numRows):
            # res += [map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])]  # python2
            res += [list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))]
            # print(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1]))  # map object
            # print(list(map(lambda x, y: x + y, res[-1] + [0], [0] + res[-1])))  # list
        return res[:numRows]

if __name__ == "__main__":
    result = Solution().generate(5)
    print(result)