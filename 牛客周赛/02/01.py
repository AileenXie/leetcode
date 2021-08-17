#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/11 9:00 PM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm
class Solution:
    def Orderofpoker(self , x ):
        # write code here
        def judge(num):
            if num in [1,2,3,5,7]:
                return True
            elif num in [4,6,8,9,10]:
                return False
        n = len(x)//2
        ans = ""
        i,j=0,len(x)-1
        while i<j:
            if judge(n):
                ans+=x[i:i+2]
                i+=2
            else:
                ans += x[j-1:j+1]
                j-=2
            n=(j-i+1)//2
        return ans

if __name__ == "__main__":
    x = "8S8S8S8S8S8S8S"
    x = "3C8D6H3D"
    x = "3D"
    print(Solution().Orderofpoker(x))