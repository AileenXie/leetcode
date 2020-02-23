#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/17 8:24 PM
# @Author : aileen
# @File : 136_single_number.py
# @Software: PyCharm

"""
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
"""


# 位操作：异或(xor)操作 x ^ 0 = x; x ^ x = 0
class Solution:
    def singleNumber(self, nums):
        ans = 0
        for i in nums:
            ans ^= i
        return ans


if __name__ == "__main__":
    # nums = [4,1,2,1,2]
    nums = [41,1,3,3,1,1,2,1,2]
    result = Solution().singleNumber(nums)
    print(result)
