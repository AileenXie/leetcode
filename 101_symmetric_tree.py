#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/29 10:05 PM
# @Author : aileen
# @File : 101_symmetric_tree.py
# @Software: PyCharm

"""
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
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
    先中序遍历，再头尾比对
    记录加上层数，以免不同层相同数字情况
    """
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        tree_list = []
        self.inorder(root, tree_list)
        print(tree_list)
        ll = len(tree_list)
        if ll%2 == 0:
            return False
        low, high = 0, ll-1
        while low < high:
            if tree_list[low] != tree_list[high]:
                return False
            low += 1
            high -= 1
        return True

    def inorder(self, root, tree_list, layer=1):
        if root is None:
            return
        self.inorder(root.left, tree_list, layer+1)
        tree_list.append([root.val, layer])
        self.inorder(root.right, tree_list, layer+1)


if __name__ == "__main__":
    # s = [1,2,2,None,3,None,3]
    # s = [1,2,2,3,4,4,3]
    # s = [1,2,2,2,None,2]
    s = []
    tree = create(s)
    result = Solution().isSymmetric(tree)
    print(result)

