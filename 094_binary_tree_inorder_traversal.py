#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/29 8:44 PM
# @Author : aileen
# @File : 094_binary_tree_inorder_traversal.py
# @Software: PyCharm

"""
Given a binary tree, return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
   1
    \
     2
    /
   3

Output: [1,3,2]
Follow up: Recursive solution is trivial, could you do it iteratively?
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
    def __init__(self):
        self.result = []

    # # recursively
    # def inorderTraversal(self, root: TreeNode):
    #     if root is None:
    #         return
    #     else:  # 中序遍历
    #         self.inorderTraversal(root.left)
    #         self.result.append(root.val)
    #         self.inorderTraversal(root.right)
    #     return self.result

    # iteratively
    def inorderTraversal(self, root):
        res, stack = [], []
        while True:
            while root:  # 先往左到底
                stack.append(root)
                root = root.left
            if not stack:  # 栈空，结束
                return res
            node = stack.pop()  # 末端出栈
            res.append(node.val)
            root = node.right  # 访问右节点


if __name__ == "__main__":
    # s = [1,None,2,3]
    s = [5,1,4,None,None,3,6]
    tree = create(s)
    result = Solution().inorderTraversal(tree)
    print(result)