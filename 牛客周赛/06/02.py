#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/30 9:42 PM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm
import functools
class Solution:
    def icecream(self, n, m, t, c):
        # write code here
        c.sort()
        total,count = 0,0
        i=0
        @functools.lru_cache()
        def dfs(i,time,count):
            print(i,time,count)
            if i>=m:  # 送完了
                print("over")
                return time,count
            min_time = time+c[i]+2*t
            min_count = count+1
            print(min_time,min_count)
            for j in range(1,n):  # 送几个
                if i+j>=m:
                    continue
                print(i+j)
                cur_time,cur_count = dfs(i+j+1,time+c[i+j]+2*t,count+1)
                if cur_time<min_time:
                    min_time=cur_time
                    min_count=cur_count
            return min_time,min_count
        ans_t,ans_c=dfs(0,0,0)
        return [ans_t,ans_c]


if __name__ == "__main__":
    n,m,t,c=2,3,10,[10,30,40]
    print(Solution().icecream(n,m,t,c))