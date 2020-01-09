#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/01/08 10:43 PM
# @Author : aileen
# @File : 105_construct_binary_tree_from_preorder_and_inorder_traversal.py
# @Software: PyCharm

"""
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    以前序（pre）序列的起始点为根节点i，在中序(in)序列中找i位置，
    i左边为左子树中序序列，右边为右子树中序序列；
    以前序序列的下一个点为根节点j,k,l,...，依次迭代在左右子树的中序中找该根节点位置，划分左右子树...
    """
    def buildTree(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.pop(0))  # pre中根节点出栈，找到根在inorder中的位置ind
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[0:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root

if __name__ == "__main__":
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    result = Solution().buildTree(preorder, inorder)
    print(result)