# Time: O(n)
# Space: O(1)
#
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
# n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines,
#  which together with x-axis forms a container, such that the container contains the most water.
#
# Example:
#
# Input: [1,8,6,2,5,4,8,3,7]
# Output: 49


class Solution:
    def maxArea(self, height) -> int:
        # max[(aj-ai)*min(ai,aj)]
        water = 0
        i = 0
        j = len(height) - 1
        while (i < j):
            cur_water = (j - i) * min(height[j], height[i])
            water = max(cur_water, water)
            if (height[i] < height[j]):
                i += 1
            else:
                j -= 1
        return water


if __name__ == '__main__':
    result = Solution().maxArea([1, 1])
    print(result)
