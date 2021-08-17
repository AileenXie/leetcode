#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 10:29 AM
# @Author : aileen
# @File : 02.py
# @Software: PyCharm

class Solution:
    def func(self,n,k,a):
        if k==1: return 1
        if n<2: return 1+n
        ans = [set()]
        for i,num in enumerate(a):
            cur = num%k
            cur_res = k-cur
            for j in range(len(ans)):
                res_set = ans[j].copy()
                if cur not in ans[j]:
                    res_set.add(cur_res)
                    ans.append(res_set)
        return len(ans)

print(Solution().func(4,3,[1,2,3,4]))