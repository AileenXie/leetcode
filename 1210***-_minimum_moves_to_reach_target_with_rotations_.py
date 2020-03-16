#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/4 7:36 PM
# @Author : aileen
# @File : 1210***-_minimum_moves_to_reach_target_with_rotations_.py
# @Software: PyCharm


class Solution:
    def __init__(self):
        self.min_count = float("inf")
        self.visited = []

    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        pos = ((0, 0), (0, 1))
        target = ((n - 1, n - 2), (n - 1, n - 1))
        print(target)
        self.move(grid, n, pos, target, 0)
        if self.min_count == float("inf"):
            return -1
        else:
            return self.min_count

    # DFS会在非最优路径时把最优路径的必经点visited，导致最优路径走不过去
    def move(self, grid, n, pos, target, step):
        print("cur step:{}, min:{}".format(step, self.min_count))
        if pos in self.visited:
            print("back to exist pos!")
            return
        if step > self.min_count:  # not min count
            print("no need to continue..")
            return
        ((i, j), (p, q)) = pos
        if i >= n or j >= n or p >= n or q >= n:  # out of range
            print("out of range")
            return
        if grid[i][j] == 1 or grid[p][q] == 1:  # WALL
            print("WALL")
            return
        if pos == target:
            print("_____________")
            if step < self.min_count:
                self.min_count = step
            return
        self.visited.append(pos)
        # print("→")
        self.move(grid, n, ((i, j + 1), (p, q + 1)), target, step + 1)  # right
        # print("↓")
        self.move(grid, n, ((i + 1, j), (p + 1, q)), target, step + 1)  # down
        if i == p:
            # print("🔃")
            if i + 1 < n:
                if grid[i + 1][j] == 0 and grid[p + 1][q] == 0:
                    self.move(grid, n, ((i, j), (p + 1, q - 1)), target, step + 1)  # clockwize
        else:
            # print("🔄")
            if j + 1 < n:
                if grid[i][j + 1] == 0 and grid[p][q + 1] == 0:
                    self.move(grid, n, ((i, j), (p - 1, q + 1)), target, step + 1)  # counterclockwize


if __name__ == "__main__":
    grid = [[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0],
            [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0]]

    # [[-, -, -, -, -, -, -, 1, 0, 0, 1, 0, 0, 0, 0],
    #  [1, 0, 0, -, -, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    #  [1, 0, 0, -, -, -, -, -, -, -, -, -, -, -, 1],
    #  [0, 0, 1, 0, 1, 0, 0, 0, 0, 1, -, -, 1, 0, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, -|, -|, -, 1, 0],
    #  [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, -|, -|, 1, 0, 1],
    #  [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, |, 1, 0, 1, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, |, 0, 1, 0, 0],
    #  [1, 0, 0, 0, 0, 0, 1, 0, 0, 0, |, 0|, 1, 1, 0],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, |, 0|, 1, 1, 0],
    #  [0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0|, 1, 1, 0],
    #  [0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1, 0|, |, |, |],
    #  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0|, |, |, |],
    #  [0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 1, -|, -|],
    #  [0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, -|, -|]]