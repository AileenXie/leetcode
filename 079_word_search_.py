#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/15 10:50 PM
# @Author : aileen
# @File : 079_word_search_.py
# @Software: PyCharm

"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""


class Solution:
    def exist(self, board, word):
        for index, row in enumerate(board):
            if word[0] in row:
                cur = [index,row.index(word[0])]
                if not self.judge(board, word[1:], cur):
                        return False
                return True
    def judge(self, board, w, cur):
        if w == "":
            return True
        x, y = cur
        if x-1 >= 0 and board[x-1,y] == w[0]:
            f1 = self.judge(board, w[1:], [x-1, y])
        if x+1 < len(board) and board[x+1, y] == w[0]:
            f2 = self.judge(board, w[1:], [x+1, y])



if __name__ == "__main__":
    board =[
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(board[0].index('E'))
    # Solution.exist(board,[1,2])