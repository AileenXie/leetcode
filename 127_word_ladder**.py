#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/1 10:03 AM
# @Author : aileen
# @File : 127_word_ladder**.py
# @Software: PyCharm

"""
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
"""

# 从begin到end，一次只能变一个字母，找出最短变化路径长度。
class Solution:
    """
    BFS： Time: O(L*N), Space: O(L*N)
    L: length of word
    N: number of word in wordList
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        if endWord not in wordList:
            return 0
        L = len(beginWord)
        # 构建 wordDict（如：{"hit":["*it", "h*t", "hi*"]}）
        wordDict = {}
        for word in wordList:
            for i in range(L):
                match = word[:i]+"*"+word[i+1:]
                wordDict.setdefault(match,[]).append(word)
        # 构建路径list (如：{1:["hit"], 2:["hot", "hio",..]， 3:[...]})
        path_dict = {1: [beginWord]}
        step = 1
        while len(path_dict) == step:
            pre_word_list = path_dict[step]
            cur_step = step + 1
            # 遍历当前层所有词
            for pre_word in pre_word_list:
                for j in range(L):
                    cur_match = pre_word[:j]+"*"+pre_word[j+1:]
                    # 没有下一个匹配词了
                    if cur_match not in wordDict.keys():
                        continue
                    for w in wordDict[cur_match]:
                        # 下一个匹配词正好等于endWord
                        if w == endWord:
                            return step + 1
                        # 未完，加入path_dict
                        else:
                            path_dict.setdefault(cur_step, []).append(w)
                    # 当前匹配项用过了，删除（同一词的不同匹配式不会出现在同一路径下！！！）
                    wordDict.pop(cur_match)
            step = cur_step
        return 0


if __name__ == "__main__":
    # beginWord = "hit"
    # endWord = "cog"
    # wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log"]
    result = Solution().ladderLength(beginWord, endWord, wordList)
    print(result)