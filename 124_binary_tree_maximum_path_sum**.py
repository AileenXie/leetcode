#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/1/22 3:06 PM
# @Author : aileen
# @File : 124_binary_tree_maximum_path_sum**.py
# @Software: PyCharm
"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.

Example 1:

Input: [1,2,3]

       1
      / \
     2   3

Output: 6
Example 2:

Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7

Output: 42
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
    def maxPathSum(self, root):
        self.ans = 0
        self.find_max(root)
        return self.ans

    def find_max(self, node):
        if not node:
            return 0
        left, right = self.find_max(node.left), self.find_max(node.right)
        v = max(node.val, node.val + max(left, right))  # 根 VS 根+单支
        self.ans = max(self.ans, v, left + node.val + right)  # ans VS (根 VS 根+单支) VS 根+双支
        return v


if __name__ == "__main__":
    s = [-10,9,20,None,None,15,7]
    s = [1,2,3]
    tree = create(s)
    ans = Solution().maxPathSum(tree)
    print(ans)