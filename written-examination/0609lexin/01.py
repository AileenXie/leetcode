#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/9 5:38 PM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm

# m, n = map(int, input().strip().split())
# grid = []
# for _ in range(m):
#     row = list(map(int, input().strip().split()))
#     grid.append(row)

class Solution():
    def func(self, grid, m, n):
        self.valid = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    self.valid.append((i, j))

        def count_group(i, j, count, midx, midy):
            if (i, j) in self.valid:
                count += 1
                midx.append(i)
                midy.append(j)
                self.valid.remove((i, j))
                for (ii, jj) in [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, 0), (1, -1), (1, 1)]:
                    if 0 <= i + ii < m and 0 <= j + jj < n:
                        count, midy, midx = count_group(i + ii, j + jj, count, midx, midy)
            return count, midy, midx

        ans = []
        for (i, j) in self.valid:
            count,midy,midx=count_group(i, j, 0, [], [])
            mid_x = sum(midx)/count
            mid_y = sum(midy)/count
            ans.append([count,mid_y,mid_x])
        print(len(ans))
        for row in ans:
            print(row)

# if __name__ == "__main__":
    # grid =




