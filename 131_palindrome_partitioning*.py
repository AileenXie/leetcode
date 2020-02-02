#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/1 2:49 PM
# @Author : aileen
# @File : 131_palindrome_partitioning*.py
# @Software: PyCharm

"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:

Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]
"""


class Solution:
    """
    遍历递归：前1个+剩下的，前2个+剩下的，...
    cur: 记录当前路径
    result: 汇总所有成功路径
    成功路径: s为空(走到底了)且cur不为空的路径
    """
    def partition(self, s: str):
        l = len(s)
        if l == 0:
            return []
        if l == 1:
            return [s]
        result = []
        cur = []
        self.do_partition(result, cur, s)
        return result

    def do_partition(self, result, cur, string):
        if string:
            for i in range(1, len(string)+1):
                if string[:i] == string[:i][::-1]:  # !!!正序=逆序 就是回文
                    self.do_partition(result, cur+[string[:i]], string[i:])  # 不能改变当前cur的值
        elif cur:  # 走到底的才可以把路径加入result
            result.append(cur)


if __name__ == "__main__":
    s = "aab"
    result = Solution().partition(s)
    print(result)