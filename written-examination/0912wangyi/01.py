#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/12 2:52 PM
# @Author : aileen
# @File : 01.py
# @Software: PyCharm


"""
找"樱桃"

10 9
1 left 2
1 right 3
2 left 4
2 right 5
3 right 6
6 left 7
6 right 8
7 left 9
7 right 10

2
___________
4 3
1 right 2
2 right 3
3 left 4

"""


import collections

class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

m, n = map(int, input().split())
father=set()
root = TreeNode(1)
dic = {"1":root}
for i in range(n):
    index, direct, sub_index = input().strip().split()  # index 是str
    father.add(index)
    cur = TreeNode(sub_index)
    dic[sub_index]=cur
    if direct=="left":
        dic[index].left=cur
    elif direct=="right":
        dic[index].right=cur
ans = 0
for i in dic:
    cur = dic[i]
    # print(cur.val,cur.left,cur.right)
    if cur.left and cur.right and cur.right.val not in father and cur.left.val not in father:
        # print(cur.val)
        ans+=1

print(ans)