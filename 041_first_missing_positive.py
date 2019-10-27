# Given an unsorted integer array, find the smallest missing positive integer.
#
# Example 1:
#
# Input: [1,2,0]
# Output: 3
# Example 2:
#
# Input: [3,4,-1,1]
# Output: 2
# Example 3:
#
# Input: [7,8,9,11,12]
# Output: 1
# Note:
#
# Your algorithm should run in O(n) time and uses constant extra space.



class Solution:
    def firstMissingPositive(self, nums) -> int:
        length = len(nums)
        for i in range(length):
            if nums[i] != i+1:  # 不是当前位置
                while length >= nums[i] >= 1 and nums[i] != nums[nums[i]-1]:  # 是正整数、没有超出范围，进行置换
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i]-1]
                    # nums[i], nums[nums[i] - 1] = nums[nums[i]-1],nums[i]  # 这样写不行！，更改了nums[i]的值会对nums[nums[i]-1]有影响
        for i in range(length):
            if nums[i] != i + 1:  # 缺失的正整数
                return i + 1
        return length + 1


if __name__ == '__main__':
    # result = Solution().firstMissingPositive([3,4,-1,1,-4])
    # result = Solution().firstMissingPositive([1])
    # result = Solution().firstMissingPositive([1,1])
    result = Solution().firstMissingPositive([2,1])
    print(result)