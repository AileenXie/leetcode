#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2019/12/29 10:31 PM
# @Author : aileen
# @File : 102_binary_tree_level_order_traversal.py
# @Software: PyCharm

"""
Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

For example:
Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:
[
  [3],
  [9,20],
  [15,7]
]
"""


# Definition for a binary tree node.
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
    # def levelOrder(self, root: TreeNode):
    #
    #     """
    #     先中序遍历，记录加上层数，然后按层输出（比较慢）
    #     """
    #     if root is None:
    #         return
    #     tree_list = []
    #     self.inorder(root, tree_list)
    #     # print(tree_list)
    #     max_level = max(row[1] for row in tree_list)
    #     result = [[] for _ in range(max_level)]
    #     for [val,level] in tree_list:
    #         result[level-1].append(val)
    #     return result
    #
    # def inorder(self, root, tree_list, layer=1):
    #     if root is None:
    #         return
    #     self.inorder(root.left, tree_list, layer + 1)
    #     tree_list.append([root.val, layer])
    #     self.inorder(root.right, tree_list, layer + 1)

    """
    用level存每层节点，ans读节点值，temp存下层节点，去None后放入level迭代
    """
    def levelOrder(self, root):
        if not root:
            return []
        ans, level = [], [root]
        while level:
            ans.append([node.val for node in level])  # 当前层节点值append入ans
            temp = []
            for node in level:  # 当前level的结点的子节点都放进temp
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]  # temp去掉None节点放入level
        return ans

if __name__ == "__main__":
    # s = [1,2,2,None,3,None,3]
    # s = [1,2,2,3,4,4,3]
    s = [1,2,2,2,None,2]
    # s = []
    tree = create(s)
    result = Solution().levelOrder(tree)
    print(result)