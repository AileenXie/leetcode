#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/4 7:26 PM
# @Author : aileen
# @File : 994_rotting_orange.py
# @Software: PyCharm

"""
In a given grid, each cell can have one of three values:

the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:

Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
Example 3:

Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Note:

1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.

"""


class Solution:
    def orangesRotting(self, grid) -> int:
        good = {}
        bad = {}
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    bad.setdefault(0, []).append((i, j))
                if grid[i][j] == 1:
                    good.setdefault((i, j), 0)

        if bad == {}:  # 特殊情况，无坏橘子
            if good == {}:  # 有橘子
                return 0
            else:  # 无橘子
                return -1
        # BFS
        step = 0
        while step in bad.keys():
            for (p, q) in bad[step]:
                self.move_good_to_bad((p + 1, q), bad, good, step + 1)
                self.move_good_to_bad((p - 1, q), bad, good, step + 1)
                self.move_good_to_bad((p, q + 1), bad, good, step + 1)
                self.move_good_to_bad((p, q - 1), bad, good, step + 1)
            step += 1
        if good != {}:
            return -1
        else:
            return step - 1

    def move_good_to_bad(self, pos, bad, good, step):
        if pos in good.keys():
            del good[pos]
            bad.setdefault(step, []).append(pos)


if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    grid = [[0,2]]
    grid = [[0]]
    grid = [[0,1]]
    print(Solution().orangesRotting(grid))
