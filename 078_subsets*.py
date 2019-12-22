#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/15 6:25 PM
# @Author : aileen
# @File : 078_subsets*.py
# @Software: PyCharm

"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    """Time Limit"""
    # def subsets(self, nums):
    #     ll = len(nums)
    #     if nums == []:
    #         return [[]]
    #     result =[[], nums]
    #     for n in range(1, ll):
    #         self.res_subsets(nums, n, result)
    #     return result
    #
    # def res_subsets(self, nums, n, result):
    #     ll = len(nums)
    #     if ll == 0:
    #         return
    #     if ll == 1:
    #         if nums not in result:
    #             result.append(nums)
    #     for i in range(ll):
    #         copystr=nums.copy()
    #         del copystr[i]
    #         if copystr not in result:
    #             result.append(copystr)
    #         self.res_subsets(copystr, result)

    # 把每个值放到现有的所有项后面
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [i + [num] for i in result]
        return result


if __name__=="__main__":
    # result = Solution().subsets([1,2,3,4,5,6,7,8,10,0])
    result = Solution().subsets([1,2,3])
    print(result)
