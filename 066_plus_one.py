#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/11/27 10:35 PM
# @Author : aileen
# @File : 066_plus_one.py
# @Software: PyCharm
"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""


class Solution:
    def plusOne(self, digits):
        n = len(digits) - 1
        plus = 1
        result = []
        while n >= 0:
            cur, plus = self.subPlus(digits[n], plus)
            n -= 1
            result.append(cur)
        if plus > 0:
            result.append(plus)
        result.reverse()
        return result

    def subPlus(self, cur, plus):
        if plus == 0:
            add = 0
        else:
            cur = cur + plus
            if cur >= 10:
                cur = cur - 10
                add = 1
            else:
                add = 0
        return cur, add


if __name__ == '__main__':
    # result = Solution().plusOne([1,2,3,9,9])
    result = Solution().plusOne([9,9,9])
    print(result)