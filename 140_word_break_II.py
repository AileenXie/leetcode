#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/22 4:48 PM
# @Author : aileen
# @File : 140_word_break_II.py
# @Software: PyCharm

"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]
Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.
"""


# DFS + 记忆搜索
class Solution:
    def __init__(self):
        self.path = []

    def wordBreak(self, s: str, wordDict):
        dic = {}
        for word in wordDict:
            if word not in s:
                continue
            dic.setdefault(word[0], []).append(word)  # 按首字母建字典
        mem = [True]*len(s)  # 记忆搜索（DFS所以记录每个层次的结果，记录死路）
        cur_path = ""
        self.judgeWord(s, dic, mem, cur_path)
        return self.path

    def judgeWord(self, s, dic, mem, cur_path):
        ls = len(s)
        if not ls:
            if cur_path != "":
                self.path.append(cur_path)
            return cur_path
        elif mem[ls-1]:  # 没被定为死路的路
            if s[0] in dic.keys():
                bak_words = dic[s[0]]
                befor_l = len(self.path)
                for word in bak_words:
                    if len(word) <= ls and s.startswith(word):
                        if cur_path == "":
                            new_path = word
                        else:
                            new_path = cur_path +" "+word
                        self.judgeWord(s[len(word):], dic, mem, new_path)
                if len(self.path) == befor_l:
                    mem[ls-1] = False
            else:
                mem[ls-1] = False


if __name__ == "__main__":
    s = "applepenapple"
    wordDict = ["apple", "pen"]
    # s = "pineapplepenapple"
    # wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
    # s = "catsandog"
    # wordDict = ["cats", "dog", "sand", "and", "cat"]
    # s = "cars"
    # wordDict = ["car", "ca", "rs"]
    # s = "aaaaaaaa"
    # wordDict = ["aaaa", "aa", 'a']
    # s = "cbca"
    # wordDict = ["bc", "ca"]
    print(Solution().wordBreak(s, wordDict))