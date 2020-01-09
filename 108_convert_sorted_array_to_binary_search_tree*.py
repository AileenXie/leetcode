#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/01/09 10:03 PM
# @Author : aileen
# @File : 105_construct_binary_tree_from_preorder_and_inorder_traversal.py
# @Software: PyCharm

"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def treeToArray(root: TreeNode):
    ans, level = [], [root]
    ans.append(root.val)
    while level:
        tmp = []
        for node in level:
            tmp.extend([node.left, node.right])
        for node in tmp:
            if node is None:
                ans.append("null")
            else:
                ans.append(node.val)
        level = [leave for leave in tmp if leave]
    while ans[-1] == "null":
        ans = ans[:-1]
    return ans



class Solution:
    """
    平衡二叉树：左右子树高度相差不大于1
    给定的是有序序列，直接用二分法建树
    """

    def sortedArrayToBST(self, nums) -> TreeNode:
        if not nums:
            return None
        mid = len(nums)//2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


if __name__ == "__main__":
    nums = [-10,-3,0,5,9]
    result = Solution().sortedArrayToBST(nums)
    result = treeToArray(result)
    print(result)