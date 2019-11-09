"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum
             jump length is 0, which makes it impossible to reach the last index.
"""

#  当前数字代表向后跳的最大步长，判断是否能跳到最后
class Solution:
    """
      思路一：从前往后递归+记忆搜索（但是会TimeLimit）❎
    """
    # def canJump(self, nums) -> bool:
    #     result = [None]*len(nums)
    #     return self._canJump(nums, result)
    #
    # def _canJump(self, nums, result):
    #     l = len(nums)-1
    #     if result[l] != None:
    #         return result[l]
    #
    #     if len(nums) < 2:
    #         result[l]=True
    #         return result[l]
    #     else:
    #         if not nums[0]:
    #             result[l] = False
    #             return result[l]
    #
    #     cur_step = nums[0]
    #     while cur_step > 0:
    #         if self._canJump(nums[cur_step:], result):
    #             return True
    #         else:
    #             cur_step -= 1
    #     return False
    """
     思路二：从后往前 ✅
    """
    def canJump(self, nums):
        length = len(nums)
        cur_end = length-1
        i = cur_end -1
        while i >= 0:
            if i + nums[i] >= cur_end:
                cur_end = i
                i -= 1
            else:
                i -= 1
        return cur_end == 0


if __name__ == '__main__':
    # result = Solution().canJump([3,2,1,0,4])
    # result = Solution().canJump([3,2,1,1,4])
    # result = Solution().canJump([5,9,3,2,1,0,2,3,3,1,0,0])
    result = Solution().canJump([2,0,6,9,8,4,5,0,8,9,1,2,9,6,8,8,0,6,3,1,2,2,1,2,6,5,3,1,2,2,6,4,2,4,3,0,0,0,3,8,2,4,0,1,2,0,1,4,6,5,8,0,7,9,3,4,6,6,5,8,9,3,4,3,7,0,4,9,0,9,8,4,3,0,7,7,1,9,1,9,4,9,0,1,9,5,7,7,1,5,8,2,8,2,6,8,2,2,7,5,1,7,9,6])
    print(result)
