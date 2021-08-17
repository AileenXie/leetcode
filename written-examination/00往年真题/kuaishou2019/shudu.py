#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/22 4:52 PM
# @Author : aileen
# @File : shudu.py
# @Software: PyCharm

grid = []
for i in range(9):
    grid.append([i for i in input()])

def isshudu(grid):
    row_count = [[0 for _ in range(9)]for _ in range(9)]
    col_count = [[0 for _ in range(9)]for _ in range(9)]
    box_count = [[0 for _ in range(9)]for _ in range(9)]
    for i in range(9):
        for j in range(9):
            val = grid[i][j]
            if val != "X":
                val = int(val)
                row_count[i][val-1]+=1
                col_count[j][val-1]+=1
                box_count[i//3 *3+j//3][val-1]+=1
                if row_count[i][val-1]>1 or col_count[j][val-1]>1 or box_count[i//3 *3+j//3][val-1] >1:
                    return False
    return True
print(isshudu(grid))
