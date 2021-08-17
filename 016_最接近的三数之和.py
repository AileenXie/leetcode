#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/22 12:12 PM
# @Author : aileen
# @File : 016_最接近的三数之和.py
# @Software: PyCharm

class Solution:
    def threeSumClosest(self, nums, target: int) -> int:
        nums.sort()
        n = len(nums)
        min_dis = float('inf')
        ans_sum = None
        i = 0
        while i < n-2:
            # while 0<i<n-2 and nums[i]==nums[i-1]: i+=1
            res = target-nums[i]
            p,q=i+1,n-1
            while p<q:
                while i+1<p<q-1 and nums[p]==nums[p-1]: p+=1
                while p+1<q<n-2 and nums[q]==nums[q+1]: q-=1
                cur_dis = abs(res-nums[p]-nums[q])
                if cur_dis<min_dis:
                    min_dis = cur_dis
                    ans_sum = nums[i]+nums[p]+nums[q]
                if nums[p]+nums[q]==res:
                    return target
                elif nums[p]+nums[q]<res:
                    p+=1
                else:
                    q-=1
            i+=1
        return ans_sum


# class Solution:
#     def threeSumClosest(self, nums, target: int) -> int:
#         nums_len = len(nums)
#         nums.sort()
#         ans_sum = nums[0] + nums[1] + nums[2];
#         for i in range(nums_len):
#             left, right = i + 1 , nums_len - 1
#             while left < right:
#                 curr_sum = nums[i] + nums[left] + nums[right]
#                 if abs(curr_sum - target) < abs(ans_sum - target):
#                     ans_sum = curr_sum
#                 if curr_sum > target: right -= 1
#                 elif curr_sum < target: left += 1
#                 else: return target
#         return ans_sum

if __name__ == "__main__":
    nums = [13,2,0,-14,-20,19,8,-5,-13,-3,20,15,20,5,13,14,-17,-7,12,-6,0,20,-19,-1,-15,-2,8,-2,-9,13,0,-3,-18,-9,-9,-19,17,-14,-19,-4,-16,2,0,9,5,-7,-4,20,18,9,0,12,-1,10,-17,-11,16,-13,-14,-3,0,2,-18,2,8,20,-15,3,-13,-12,-2,-19,11,11,-10,1,1,-10,-2,12,0,17,-19,-7,8,-19,-17,5,-5,-10,8,0,-12,4,19,2,0,12,14,-9,15,7,0,-16,-5,16,-12,0,2,-16,14,18,12,13,5,0,5,6]
    target =-59
    print(Solution().threeSumClosest(nums,target))