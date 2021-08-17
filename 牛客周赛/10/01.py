#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/13 9:07 PM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm


class Solution:
    def solve(self, str):
        # write code here
        if not str: return ""
        ans=""
        for s in str:
            # print(s, ans)
            ans += s
            if not ans:
                continue
            # print(f"+{ans[-2:]}")
            while len(ans)>=2 and ans[-2:]=="00" or ans[-2:]=="11":
                # print(f"++{ans[-2:]}")
                if ans[-2:]=="00":
                    ans = ans[:-2] + "1"
                else:
                    ans=ans[:-2]

        return ans


print(Solution().solve("00110001"))