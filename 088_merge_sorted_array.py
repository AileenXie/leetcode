#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/22 10:18 PM
# @Author : aileen
# @File : 088_merge_sorted_array.py
# @Software: PyCharm
"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

Note:

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
"""

class Solution:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            nums1[:n] = nums2[:n]
        elif n == 0:
            return
        else:
            i, j = 0, 0
            while i < m and j < n:
                if nums1[i] > nums2[j]:
                    nums1[i+1:m+1] = nums1[i:m]  # 整个向后移
                    nums1[i] = nums2[j]
                    m += 1
                    i += 1
                    j += 1
                else:
                    i += 1
            if j < n:
                nums1[i:i+n-j] = nums2[j:n]  # 仔细写，把多于的nums2（n-j个）放到nums1后面
                m += n-j




if __name__ == "__main__":
    # nums1 = [1, 2, 3, 0, 0, 0]
    # nums2 = [2, 5, 6]
    # m, n = 3, 3
    # nums1 = [0]
    # nums2 = [1]
    # m, n = 1, 0

    nums1 = [4, 0, 0, 0, 0, 0]
    m = 1
    nums2 = [1, 2, 3, 5, 6]
    n = 5
    Solution().merge(nums1, m, nums2, n)
    print(nums1)