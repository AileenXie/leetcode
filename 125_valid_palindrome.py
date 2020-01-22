#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/22 3:59 PM
# @Author : aileen
# @File : 125_valid_palindrome.py
# @Software: PyCharm
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
"""


# Definition for a binary tree node.
class Solution:
    """
    比较慢
    """
    # def isPalindrome(self, s: str) -> bool:
    #     ll = len(s)
    #     if ll < 2:
    #         return True
    #     i, j = 0, ll-1
    #     while i < j:
    #         if not s[i].isalnum():  # 可优化
    #             i += 1
    #             continue
    #         if not s[j].isalnum():
    #             j -= 1
    #             continue
    #         # print("{} <-> {}\n".format(s[i], s[j]))
    #         if s[i].lower() == s[j].lower():
    #             i += 1
    #             j -= 1
    #         else:
    #             return False
    #     return True
    """
    优化
    """
    def isPalindrome(self, s: str) -> bool:
        ll = len(s)
        if ll < 2:
            return True
        i, j = 0, ll-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            # print("{} <-> {}\n".format(s[i], s[j]))
            if s[i].lower() == s[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"
    s = "race a car"
    s = ""
    s = "0P"
    ans = Solution().isPalindrome(s)
    print(ans)