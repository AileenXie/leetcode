#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/12 5:12 PM
# @Author : aileen
# @File : 面试题56.py
# @Software: PyCharm
import functools

class Solution:
    def singleNumbers(self, nums):
        ret = functools.reduce(lambda x, y: x ^ y, nums)  # 全部异或
        div = 1
        while div & ret == 0:  # 按位与，找到ret中为1的位置N，如第三位为1则div=100
            div <<= 1  # div向左移一位
        a, b = 0, 0
        for n in nums:  # 进行分组，把a,b分到两组，异或结果就是a,b本身
            if n & div:  # 第N位是1的
                a ^= n
            else:  # 第N位是0的
                b ^= n
        return [a, b]

if __name__ == "__main__":
    nums = [1,2,4,6,4,1]
    nums = [13,14,16,12,21,13,16,14]
    print(Solution().singleNumbers(nums))