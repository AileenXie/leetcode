#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/6 2:10 PM
# @Author : aileen
# @File : 面试题57 - II. 和为s的连续正数序列.py
# @Software: PyCharm
"""
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。

序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

 

示例 1：

输入：target = 9
输出：[[2,3,4],[4,5]]
示例 2：

输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]
 

限制：

1 <= target <= 10^5

"""


# 数学法：等差数列
# class Solution:
#     def findContinuousSequence(self, target: int):
#         result = []
#         if target < 3:
#             return result
#         num = int(pow(2*target,0.5))  # 由几个数字组成，由mid-num//2 >0得到
#         while num > 1:
#             mid = target//num
#             half = num // 2
#             res = num % 2
#             total = 0
#             cur_ans = []
#             if res == 1:
#                 for i in range(-half,half+1):  # 奇数个数，就中位数往两边扩展
#                     total += i+mid
#                     cur_ans.append(mid+i)
#             else:
#                 for i in range(-(half-1),half+1):  # 偶数个个数，就中位数位于中间偏左
#                     total += i+mid
#                     cur_ans.append(mid+i)
#             print(cur_ans)
#             if total == target:
#                 result.append(cur_ans)
#             num -= 1  # 为了得到从小到大的组合，num要由大到小
#         return result


"""
滑动窗口：
# 🧠里要有一个区间的概念，这里的区间是(1, 2, 3, ..., target - 1)
# 套滑动窗口模板，l是窗口左边界，r是窗口右边界，窗口中的值一定是连续值。
# 当窗口中数字和小于target时，r右移; 大于target时，l右移; 等于target时就获得了一个解
"""
class Solution:
    def findContinuousSequence(self, target: int):
        result = []
        l, r = 1, 1
        sum = 0

        while r < target:
            sum += r
            while sum > target:  # 大于target时，l右移
                sum -= l
                l += 1
            if sum == target:
                temp = []
                for num in range(l, r+1):
                    temp.append(num)
                result.append(temp)
            r += 1
        return result


if __name__ == "__main__":
    # target = 3
    # target = 0
    # target = 15
    target = 100
    print(Solution().findContinuousSequence(target=target))
