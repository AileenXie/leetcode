#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/29 9:15 PM
# @Author : aileen
# @File : 098_validate_binary_search_tree.py
# @Software: PyCharm

"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

    2
   / \
  1   3

Input: [2,1,3]
Output: true
Example 2:

    5
   / \
  1   4
     / \
    3   6

Input: [5,1,4,null,null,3,6]
Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
Accepted
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
    def isValidBST(self, root: TreeNode, low=float('-inf'), high=float('inf')) -> bool:
        if root is None:
            return True
        cur = root.val
        if low >= cur or high <= cur:
            return False
        return self.isValidBST(root.left, low, cur) and self.isValidBST(root.right, cur, high)


if __name__ == "__main__":
    # s = [5,1,4,None,None,3,6]
    # s = [2,1,3]
    # s = [1,1]
    s = [10,5,15,None,None,6,20]
    tree = create(s)
    result = Solution().isValidBST(tree)
    print(result)