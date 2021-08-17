#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/6 9:28 PM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm

import functools

# class Solution:
#     def solve(self, n, m, a):
#         # write code here
#         max_len = 0
#         cur_len = 0
#         black=0
#         for c in a:
#             if c==1:
#                 cur_len+=1
#             else:
#                 black+=1
#                 max_len=max(max_len,cur_len)
#                 cur_len=0
#
#         if black <= m:
#             return n
#         if not m: return max_len
#
#         self.max = 0
#         @functools.lru_cache(None)
#         def dfs(i,res,count):
#             # print(i,res,count)
#             if not res or i>=n:
#                 self.max=max(self.max,count)
#                 return
#             if a[i]==1:  # 当前是白色
#                 dfs(i+1,res,count+1)
#             else:
#                 dfs(i+1,res-1,count+1)
#                 dfs(i+1,res,1)
#                 # self.max=max(self.max,count)
#         dfs(0,m,0)
#         return self.max

#
#
# @param n int整型
# @param m int整型
# @param a int整型一维数组
# @return int整型
#
class Solution:
    def solve(self , n , K , A ):
        # write code here
        i = 0
        for j in range(len(A)):
            K -= 1 - A[j]
            if K < 0:
                K += 1 - A[i]
                i += 1
        return j - i + 1

# n,m,a = 0, 0, []
n,m,a = 6,1, [1,0,0,1,1,1]
# n,m,a = 6,2, [1,0,0,1,1,1]
# n,m,a = 6,2, [1,0,0,1,0,1]
# n,m,a = 6,0, [1,0,0,1,0,1]
print(Solution().solve(n,m,a))