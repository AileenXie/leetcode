# Time: O(log n)
# Space: O(1)
#
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# If the target is not found in the array, return [-1, -1].
#
# Example 1:
#
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:
#
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]


class Solution:
    def searchRange(self, nums, target: int):
        l = len(nums)
        if l == 0:
            return [-1, -1]
        start = 0
        end = len(nums) - 1
        return self.search(nums, target, start, end)

    def search(self, nums, target, start, end):
        if start >= end:
            return [start, start] if target == nums[start] else [-1, -1]
        mid = (start + end) // 2
        if target == nums[mid]:
            s, e = mid, mid
            if mid - 1 >= start and nums[mid - 1] == target:  # 不是第一个
                new_end = mid - 1
                [s, _] = self.search(nums, target, start, new_end)
            if mid + 1 <= end and nums[mid + 1] == target:  # 不是最后一个
                start = mid + 1
                [_, e] = self.search(nums, target, start, end)
            return [s, e]
        elif target > nums[mid]:
            start = mid + 1
            return self.search(nums, target, start, end)
        else:
            end = mid - 1
            return self.search(nums, target, start, end)


if __name__ == '__main__':
    # result = Solution().searchRange([5,7,7,8,8,10],10)
    result = Solution().searchRange([3,3,3],3)
    print(result)