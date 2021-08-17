#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 9:09 PM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm
"""
最长金字塔数组
"""
class Solution:
    def getMaxLength(self , n , num ):
        # write code here
        if n<3: return 0
        l,r=0,1
        max_len = 0
        top_flag=False
        while r<n:
            top_flag=False
            if num[r]==num[r-1]:
                r+=1
                l+=1
                continue
            while r<n and num[r]>num[r-1]:  # up
                r+=1
            if r>=n: break
            top_flag=True
            while r<n and num[r]<num[r-1]:
                r+=1
            cur_len = r-l
            # print(cur_len)
            max_len = max(cur_len,max_len)
            l=r-1
        if top_flag:
            cur_len = r-l
            max_len = max(cur_len,max_len)
        return max_len

if __name__ == "__main__":
    print(Solution().getMaxLength(4,[1,2,3,1]))
    print(Solution().getMaxLength(5,[1,5,3,3,1]))
    print(Solution().getMaxLength(5,[1,1,1,1,1]))
    print(Solution().getMaxLength(5,[1,1,1,1,2]))