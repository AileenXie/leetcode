#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/15 3:43 PM
# @Author : aileen
# @File : 075_sort_colors.py
# @Software: PyCharm

"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

"""

# 冒泡
class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ll = len(nums)
        for i in range(ll - 1):
            flag = 0
            for j in range(ll - 1 - i):
                if nums[j] > nums[j + 1]:
                    flag = 1
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
            if flag == 0:
                break


if __name__ == '__main__':
    nums = [2, 0, 2, 1, 1, 0]
    result = Solution().sortColors(nums)
    print(nums)
