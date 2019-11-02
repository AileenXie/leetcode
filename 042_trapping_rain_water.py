# Given n non-negative integers representing an elevation map where the width of each bar is 1,
# compute how much water it is able to trap after raining.
# The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
# In this case, 6 units of rain water (blue section) are being trapped.
# Thanks Marcos for contributing this image!
#
# Example:
#
# Input: [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6


class Solution:
    def trap(self, height) -> int:
        l = len(height)
        if l == 0 or l == 1:
            return 0
        pre = height[0]
        left = pre
        sum = 0
        bar_list = [pre]
        for i in range(1, l):
            if height[i] < pre and pre >= left:  # pre是上一个容器的右边，新容器的左边
                sum += self.save_water(bar_list, 1)
                bar_list = [pre, height[i]]
                left = pre

            else:  # bar还在升高，当前bar_list增加
                bar_list.append(height[i])
            pre = height[i]

        sum += self.save_water(bar_list, 2)

        return sum

    def save_water(self, bar, flag):
        if len(bar) <= 2:
            return 0
        if flag == 1 or bar[-1] >= bar[0]:
            edge = min(bar[0], bar[-1])
            sum = 0
            for i in range(1, len(bar) - 1):
                if bar[i] < edge:
                    sum = sum + (edge - bar[i])
            return sum
        else:  # 有左边没右边， 找右边(且已知左边是最大的)
            edge_left = 0
            edge_right = 1
            for i in range(1, len(bar)):
                if bar[i] > bar[edge_right]:
                    edge_right = i
            edge = min(bar[edge_left], bar[edge_right])
            sum = 0  # 左右边之间计算积水量
            for i in range(edge_left + 1, edge_right):
                if bar[i] < edge:
                    sum = sum + (edge - bar[i])
            sum += self.save_water(bar[edge_right:], 2)
            return sum


if __name__ == '__main__':
    # result = Solution().trap([5,4,1,2])  # 1
    # result = Solution().trap([4,9,4,5,3,2])  # 1
    # result = Solution().trap([9,6,8,8,5,6,3])  # 3
    # result = Solution().trap([2,1,0,2])  # 3
    # result = Solution().trap([5,2,1,2,1,5])  # 14
    result = Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])  # 6
    print(result)
