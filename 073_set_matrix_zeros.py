#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/1 1:00 PM
# @Author : aileen
# @File : 073_set_matrix_zeros.py
# @Software: PyCharm

"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:

Input:
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output:
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]
Example 2:

Input:
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output:
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]
Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""


class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        record_x =[]
        record_y =[]
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    if i not in record_x:
                        record_x.append(i)
                    if j not in record_y:
                        record_y.append(j)
        for i in record_x:
            matrix[i] = [0 for _ in range(n)]
        for i in record_y:  # 注意list读列的方法
            for x in matrix:
                x[i] = 0


if __name__ == '__main__':
    matrix=[
  [0,1,2,0],
  [3,4,5,2],
  [1,1,1,5]
]
    result = Solution().setZeroes(matrix)
    print(matrix)
