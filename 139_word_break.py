#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/22 2:37 PM
# @Author : aileen
# @File : 139_word_break.py
# @Software: PyCharm

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


# DFS + 记忆搜索
class Solution:
    def wordBreak(self, s: str, wordDict):
        dic = {}
        for word in wordDict:
            if word not in s:
                continue
            dic.setdefault(word[0], []).append(word)  # 按首字母建字典
        visited = [False]*len(s)  # 记忆搜索（DFS所以记录每个层次的结果）
        return self.judgeWord(s, dic, visited)

    def judgeWord(self, s, dic, visited):
        ls = len(s)
        if not ls:
            return True
        if s[0] in dic.keys():
            bak_words = dic[s[0]]
        else:
            return False
        if visited[ls-1]:
            return False
        visited[ls-1] = True
        for word in bak_words:
            if len(word) <= ls and s.startswith(word):
                result = self.judgeWord(s[len(word):], dic, visited)
                if result:  # 只要一条路走通就行
                    break
            else:
                result = False
        return result



if __name__ == "__main__":
    # s = "applepenapple"
    # wordDict = ["apple", "pen"]
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "cars"
    # wordDict = ["car", "ca", "rs"]
    # s = "aaaaaaa"
    # wordDict = ["aaaa", "aa"]
    # s = "cbca"
    # wordDict = ["bc", "ca"]
    print(Solution().wordBreak(s, wordDict))
