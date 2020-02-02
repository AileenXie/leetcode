#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/1 12:25 PM
# @Author : aileen
# @File : 130_surrounded_regions.py
# @Software: PyCharm

"""
Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:

X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X
Explanation:

Surrounded regions shouldn’t be on the border,
which means that any 'O' on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
Two cells are connected if they are adjacent cells connected horizontally or vertically.
"""


class Solution:
    """
    先找到外圈的O，向内感染 O -> W
    感染完后，O -> X, W -> O
    """
    # def solve(self, board) -> None:
    #     h = len(board)
    #     if h == 1 or h == 0:
    #         return board
    #     w = len(board[0])
    #     i = 0
    #     for j in range(w):
    #         if board[i][j] == "O":
    #             self.infaction(board, h, w, i, j)
    #     for i in range(1, h):
    #         if board[i][j] == "O":
    #             self.infaction(board, h, w, i, j)
    #     for j in range(w-1):
    #         if board[i][j] == "O":
    #             self.infaction(board, h, w, i, j)
    #     j = 0
    #     for i in range(1,h-1):
    #         if board[i][j] == "O":
    #             self.infaction(board, h, w, i, j)
    #
    #     for i in range(h):
    #         for j in range(w):
    #             if board[i][j] == "O":
    #                 board[i][j] = "X"
    #
    #     for i in range(h):
    #         for j in range(w):
    #             if board[i][j] == "W":
    #                 board[i][j] = "O"
    #
    # def infaction(self, board, h, w, x,y):
    #     """
    #     :param board:
    #     :param x: 当前被感染的坐标x
    #     :param y: 当前被感染的坐标y
    #     :return:
    #     """
    #     board[x][y] = "W"
    #     if x-1 >= 0:
    #         if board[x-1][y] == "O":
    #             board[x - 1][y] = "W"
    #             self.infaction(board, h, w, x-1, y)
    #     if x+1 < h:
    #         if board[x+1][y] == "O":
    #             board[x + 1][y] = "W"
    #             self.infaction(board, h, w, x+1, y)
    #     if y-1 >= 0:
    #         if board[x][y-1] == "O":
    #             board[x][y-1] = "W"
    #             self.infaction(board, h, w, x, y-1)
    #     if y+1 < w:
    #         if board[x][y+1] == "O":
    #             board[x][y+1] = "W"
    #             self.infaction(board, h, w, x, y+1)

    """
    同样的思路，优化一下步骤
    先找到外圈的O，向内感染 O -> W
    感染完后，O -> X, W -> O
    """
    def solve(self, board) -> None:
        h = len(board)
        if h == 1 or h == 0:
            return board
        w = len(board[0])
        for j in range(w):
            self.infaction(board, h, w, 0, j)
            self.infaction(board, h, w, h-1, j)
        for i in range(h):
            self.infaction(board, h, w, i, 0)
            self.infaction(board, h, w, i, w-1)

        for i in range(h):
            for j in range(w):
                if board[i][j] == "O":
                    board[i][j] = "X"

        for i in range(h):
            for j in range(w):
                if board[i][j] == "W":
                    board[i][j] = "O"

    def infaction(self, board, h, w, x,y):
        """
        :param board:
        :param x: 当前元素坐标x
        :param y: 当前元素坐标y
        :return:
        """
        if x < 0 or x >= h or y <0 or y >= w:  # 位置非法
            return
        if board[x][y] != "O":  # 不为O
            return

        board[x][y] = "W"  # 位置合法且为O-->被感染
        # 感染周边
        self.infaction(board, h, w, x-1, y)
        self.infaction(board, h, w, x+1, y)
        self.infaction(board, h, w, x, y-1)
        self.infaction(board, h, w, x, y+1)


if __name__ == "__main__":
    board =[["X","X","X","X"],
            ["X","O","O","X"],
            ["X","X","O","X"],
            ["X","O","X","X"]]
    # board =[["O","X","X","O","X"],
    #         ["X","O","O","X","O"],
    #         ["X","O","X","O","X"],
    #         ["O","X","O","O","O"],
    #         ["X","X","O","X","O"]]
    # board =[2]
    Solution().solve(board)
    print(board)