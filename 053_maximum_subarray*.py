"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""


class Solution:
    def maxSubArray(self, nums):
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]  # *滚雪球，只把前一个非负的雪球滚过来
        return max(nums)


if __name__ == '__main__':
    # result = Solution().maxSubArray([-1])
    # result = Solution().maxSubArray([-2,1])
    result = Solution().maxSubArray([8,-19,5,-4,20])
    # result = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    print(result)
