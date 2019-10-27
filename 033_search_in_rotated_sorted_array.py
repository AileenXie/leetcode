# Time: O(log n)
# Space: O(1)
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
#
# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).
#
# You are given a target value to search. If found in the array return its index, otherwise return -1.
#
# You may assume no duplicate exists in the array.
#
# Your algorithm's runtime complexity must be in the order of O(log n).
#
# Example 1:
#
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
#
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1


# 依然是二分法，问题变成：判断找左右哪一边
# 思路： 只判断顺序的一边，在范围内就找这边，不在就找另一边
class Solution:
    def search(self, nums, target: int) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                return mid

            if (nums[low] <= nums[mid]):
                if (nums[low] <= target <= nums[mid]):
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if (nums[mid] <= target <= nums[high]):
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

if __name__ == '__main__':
    # result = Solution().search([4,5,6,7,0,1,2],7)
    # result = Solution().search([1,3],2)
    # result = Solution().search([4,5,6,7,8,1,2,3],8)
    # result = Solution().search([4,5,6,7,0,1,2],0)
    result = Solution().search([1,3,5],1)
    print(result)