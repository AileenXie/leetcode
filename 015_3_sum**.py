# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
#
# Note:
#
# The solution set must not contain duplicate triplets.
#
# Example:
#
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


# class Solution:
# ——————————————————————————————————————————————————————————
# 思路： 先排序，确定第一个值，在之后的数应用2sum思想（字典）
# 问题： 不好处理去重复问题
# ——————————————————————————————————————————————————————————
#     def threeSum(self, nums):
#         nums=sorted(nums)
#         l = len(nums)
#         result = []
#         for i in range(l-1):
#             dir = dict()
#             for j in range(i+1,l):
#                 res = 0-nums[i]-nums[j]
#                 if res in dir:
#                     if dir[res]<i:
#                         result.append([res, nums[i], nums[j]])
#                     elif dir[res]>j:
#                         result.append([nums[i], nums[j], res])
#                     else:
#                         result.append([ nums[i], res, nums[j]])
#                 else:
#                     dir[nums[j]] = j
#         return result

class Solution:
    # ——————————————————————————————————————————————————————————
    # 思路： 先排序，确定第一个值，在之后的数从两头往中间找
    # 难点：去重复（第一个值去重复，后两个组合去重复）
    # ——————————————————————————————————————————————————————————
    def threeSum(self, nums):
        nums = sorted(nums)
        l = len(nums)
        ans = []
        i = 0
        while i < l - 2:
            # 避免重复1
            while 0 < i < l - 2 and nums[i] == nums[i - 1]:
                i += 1
            # 从两头向中间找
            left, right = i + 1, l - 1
            res = 0 - nums[i]
            flag = 0
            over = 0
            while left < right:
                # 避免重复2
                if flag == 1:
                    while nums[left] == nums[left - 1] and nums[right] == nums[right + 1]:
                        left += 1
                        right -= 1
                        if left >= right:
                            over = 1
                            break
                    if over == 1:
                        break
                    flag = 0

                sum = nums[left] + nums[right]
                if sum < res:
                    left += 1
                elif sum > res:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    flag = 1
            i += 1
        return ans


if __name__ == '__main__':
    result = Solution().threeSum([-1, 0, 1, 2, -1, -4])
    # result = Solution().threeSum([-2,0,0,2,2])
    # result = Solution().threeSum([0, 0, 0, 0])
    # result = Solution().threeSum([-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6])
    # result = Solution().threeSum([0, -4, -1, -4, -2, -3, 2])
    # result = Solution().threeSum([-2, 0, 0, 2, 2])
    # result = Solution().threeSum([2,-3,0,-2,-5,-5,-4,1,2,-2,2,0,2,-4])
    print(result)
