#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/2 2:58 PM
# @Author : aileen
# @File : 132_palindrome_partition_II**.py
# @Software: PyCharm
"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

class Solution:
    """
    简单按照131的思路改
    会TimeLimit!
    而且不好加记忆搜索
    """
    # def minCut(self, s: str) -> int:
    #     if len(s) < 2:
    #         return 0
    #     path_count = []
    #     cur_path = -1
    #     self.do_partition(path_count, cur_path, s)
    #     # print(path_count)
    #     return min(path_count)
    #
    # def do_partition(self, path_count, cur_path, s):
    #     if s:
    #         for i in range(1, len(s)+1):
    #             if s[:i] == s[:i][::-1]:
    #                 self.do_partition(path_count, cur_path+1, s[i:])
    #     elif cur_path != -1:
    #         path_count.append(cur_path)

    """
    递归 + 记忆搜索mem[s]=minCut
    """
    def minCut(self, s: str) -> int:
        mem = {}  # 记录字符串的最小切割数
        ans = self.cut(mem, s)
        return ans

    def cut(self, mem, s):
        # 单独处理0次和1次cut的情况
        if s in mem.keys():
            return mem[s]
        if s == s[::-1]:
            return 0
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1
        # 递归
        ans = len(s)-1
        for i in range(1, len(s)):
            if s[:i] == s[:i][::-1]:
                ans = min(ans, self.cut(mem, s[i:]))  # 边遍历边更新!!!
        mem[s] = ans + 1
        return ans + 1


if __name__ == "__main__":
    # s = "aab"
    # s = "ababababababababababababcbabababababababababababa"
    # s = "leet"
    s = "leetaaa"
    s = "ababbbabbaba"
    result = Solution().minCut(s)
    print(result)