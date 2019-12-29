#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/26 3:03 PM
# @Author : aileen
# @File : 091_decode_ways.py
# @Software: PyCharm
"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"122321"
1+4+
"""


class Solution:
    """
    递归+记忆搜索：算叶子节点数
    例如：      1203
               /  \
         1 203    12 03
          / \        \
      2 03 20 3      X
       /      \
      X       √           ---> 1种
    """
    def numDecodings(self, s: str) -> int:
        mem = [None for _ in range(len(s)+1)]
        n = self.num_decodings(s, mem)
        return n

    def num_decodings(self, s, mem):
        ll = len(s)
        if mem[ll] is not None:  # 记忆搜索
            return mem[ll]

        if ll == 0:  # 到底了，叶子+1
            return 1
        if int(s[0]) == 0:  # 第一位是0，这个分支不成立X
             return 0
        if ll == 1:  # 除了0以外任何一位数都可以被被编码 +1
            return 1
        n = self.num_decodings(s[1:], mem)  # 除第一位外，递归
        if int(s[:2]) <= 26:  # 除前两位外，递归
            n += self.num_decodings(s[2:], mem)
        mem[ll] = n
        return n


if __name__ == "__main__":
    s = "220"
    s = "020"
    s = "1012"
    s = "230"
    s = "26"
    result = Solution().numDecodings(s)
    print(result)