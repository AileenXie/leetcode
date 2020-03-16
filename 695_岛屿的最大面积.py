#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/15 3:35 PM
# @Author : aileen
# @File : 695_岛屿的最大面积.py
# @Software: PyCharm

"""
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:

[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。

"""


class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])
        self.visited = [[0 for col in range(n)] for row in range(m)]  # 记录走过的路，（可以直接在grid上操作！！！）
        ans = 0
        for i in range(m):
            for j in range(n):
                if not self.visited[i][j] and grid[i][j] == 1:
                    ans = max(self.countArea(m, n, grid, self.visited, (i, j)), ans)
        return ans

    # dfs
    def countArea(self, m, n, grid, visited, pos):
        (i, j) = pos
        if i < 0 or i >= m or j < 0 or j >= n:
            return 0
        if visited[i][j] == 1 or grid[i][j] == 0:
            return 0
        visited[i][j] = 1
        ans = 1
        for p, q in [[i - 1, j], [i + 1, j], [i, j - 1], [i, j + 1]]:
            next_ans = self.countArea(m, n, grid, visited, (p, q))
            ans += next_ans
        return ans


if __name__ == "__main__":
    # grid = [[1, 1, 0, 0, 0], [1, 1, 0, 0, 0], [0, 0, 0, 1, 1], [0, 0, 0, 1, 1]]
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    print(Solution().maxAreaOfIsland(grid))
