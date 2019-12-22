#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/15 3:57 PM
# @Author : aileen
# @File : 076_minimum_window_substring_.py
# @Software: PyCharm

"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:

Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"
Note:

If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        dic = {}
        for key in t:
            dic[key]= 0
        flag = False  # 判断t是否齐了
        for index, key in enumerate(s):
            if key in dic.keys():
                dic[key] += 1


