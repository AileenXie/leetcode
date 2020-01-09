#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/01/07 11:12 PM
# @Author : aileen
# @File : 103_binary_tree_zigzag_level_order_traversal.py
# @Software: PyCharm

"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its zigzag level order traversal as:
[
  [3],
  [20,9],
  [15,7]
]
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def create(s, index=0):
    if index >= len(s):
        return
    if s[index] is None:
        root = None
    else:
        root = TreeNode(s[index])
        root.left = create(s, 2*index+1)
        root.right = create(s, 2*index+2)
    return root

class Solution:
    """
    与上一题很类似，加了个控制方向的flag
    用level存每层节点，ans读节点值，temp存下层节点，去None后放入level迭代
    """
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]
        flag = 1
        while level:
            cur_level = [node.val for node in level]
            if flag == 1:
                ans.append(cur_level)
            else:
                cur_level.reverse()
                ans.append(cur_level)
            flag = -1*flag
            temp = []
            for node in level:  # 当前level的结点的子节点都放进temp
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]  # temp去掉None节点放入level
        return ans

if __name__ == "__main__":
    s = [3,9,20,None,None,15,7]
    tree = create(s)
    result = Solution().zigzagLevelOrder(tree)
    print(result)