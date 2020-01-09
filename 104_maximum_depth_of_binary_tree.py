#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/01/08 10:25 PM
# @Author : aileen
# @File : 104_maximum_depth_of_binary_tree.py
# @Software: PyCharm

"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
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
    与上一题很类似，不需要记录各节点值，只需记录层数
    用level存每层节点，ans读节点值，temp存下层节点，去None后放入level迭代
    """
    def maxDepth(self, root) -> int:
        if not root:
            return 0
        level_num, level = 0, [root]
        while level:
            level_num += 1
            temp = []
            for node in level:  # 当前level的结点的子节点都放进temp
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]  # temp去掉None节点放入level
        return level_num

if __name__ == "__main__":
    s = [3,9,20,None,None,15,7]
    tree = create(s)
    result = Solution().maxDepth(tree)
    print(result)