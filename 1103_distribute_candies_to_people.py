#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/5 8:33 AM
# @Author : aileen
# @File : 1103_distribute_candies_to_people.py
# @Software: PyCharm

"""
We distribute some number of candies, to a row of n = num_people people in the following way:

We then give 1 candy to the first person, 2 candies to the second person,
and so on until we give n candies to the last person.

Then, we go back to the start of the row, giving n + 1 candies to the first person,
n + 2 candies to the second person, and so on until we give 2 * n candies to the last person.

This process repeats (with us giving one more candy each time,
and moving to the start of the row after we reach the end) until we run out of candies. 
The last person will receive all of our remaining candies (not necessarily one more than the previous gift).

Return an array (of length num_people and sum candies) that represents the final distribution of candies.

 

Example 1:

Input: candies = 7, num_people = 4
Output: [1,2,3,1]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0,0].
On the third turn, ans[2] += 3, and the array is [1,2,3,0].
On the fourth turn, ans[3] += 1 (because there is only one candy left), and the final array is [1,2,3,1].
Example 2:

Input: candies = 10, num_people = 3
Output: [5,2,3]
Explanation:
On the first turn, ans[0] += 1, and the array is [1,0,0].
On the second turn, ans[1] += 2, and the array is [1,2,0].
On the third turn, ans[2] += 3, and the array is [1,2,3].
On the fourth turn, ans[0] += 4, and the final array is [5,2,3].
 

Constraints:

1 <= candies <= 10^9
1 <= num_people <= 1000
"""


# 暴力求解法
# Time: O(max(√C,N))  Space: O(1)
class Solution:
    def distributeCandies(self, candies: int, num_people: int):
        if num_people == 0:
            return []
        ans = [0] * num_people
        cur_num = 1
        basic = 0
        while candies > 0:
            should_num = cur_num + (basic * num_people)
            if candies <= should_num:  # 糖果不够
                ans[cur_num - 1] += candies
                candies = 0
            else:  # 糖果充足
                ans[cur_num - 1] += should_num
                candies -= should_num
                cur_num += 1
                if cur_num >= num_people:
                    cur_num -= num_people
                    basic += 1
        return ans


# # 等差数列法，num_people不能为0。
# # Time: O(N)  Space: O(1)
# class Solution:
#     def distributeCandies(self, candies: int, num_people: int):
#         n = num_people
#         # how many people received complete gifts
#         p = int((2 * candies + 0.25) ** 0.5 - 0.5)  # p是等差数列最后一个元素，candies - sum(1,...p) < p+1
#         remaining = int(candies - (p + 1) * p * 0.5)  # 最后剩余的 candies - sum(1,...p)
#         rows, cols = p // n, p % n  # rows发了几个整轮， cols剩余几个人
#
#         d = [0] * n
#         for i in range(n):
#             # complete rows
#             d[i] = (i + 1) * rows + int(rows * (rows - 1) * 0.5) * n  # 完整轮中 i 获得的糖果数
#             # cols in the last row
#             if i < cols:
#                 d[i] += i + 1 + rows * n  # 不完整轮中 i 获得的糖果数
#         # remaining candies
#         d[cols] += remaining  # 最后一个人获得剩余零头糖果
#         return d


if __name__ == "__main__":
    candies, num_people = 7, 3
    candies, num_people = 0, 3
    candies, num_people = 2, 3
    print(Solution().distributeCandies(candies, num_people))
