#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/1 9:59 PM
# @Author : aileen
# @File : 03多重背包问题i.py
# @Software: PyCharm

#
# 把所有询问的答案按询问顺序放入vector里
# @param arr int整型一维数组 要查询坐标的数组
# @return int整型一维数组
#
class Solution:
    def MinimumTimes(self, arr):
        # write code here
        choice = [3,7,11]
        max_target = max(arr)
        dp = [float('inf')]*(max_target+12)
        queue = [(0,0)]
        to_do = set(arr)
        while queue:
            cur,step = queue.pop(0)
            # print(cur,step)
            if cur<0 or cur>max_target+11:
                # print("out of range")
                continue
            if not to_do:
                # print("find all")
                break
            if dp[cur]==float('inf'):
                dp[cur]=step
            else:
                # print("visited")
                continue  # 走过了
            if cur in to_do:
                to_do.remove(cur)
            for x in choice:
                queue.append((cur+x,step+1))
                queue.append((cur-x,step+1))
        ans = [dp[a] for a in arr]
        return ans

arr = [1,4,14]
arr = [6,25]
print(Solution().MinimumTimes(arr))
