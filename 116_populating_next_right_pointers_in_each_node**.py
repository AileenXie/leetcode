#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/01/09 10:52 PM
# @Author : aileen
# @File : 116_populating_next_right_pointers_in_each_node**.py
# @Software: PyCharm

"""
You are given a perfect binary tree where all leaves are on the same level, and every parent has two children. The binary tree has the following definition:

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.



Follow up:

You may only use constant extra space.
Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.


Example 1:



Input: root = [1,2,3,4,5,6,7]
Output: [1,#,2,3,#,4,5,6,7,#]
Explanation: Given the above perfect binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.


Constraints:

The number of nodes in the given tree is less than 4096.
-1000 <= node.val <= 1000
"""


# Definition for a binary tree node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


def create(s, index=0):
    if index >= len(s):
        return
    if s[index] is None:
        root = None
    else:
        root = Node(s[index])
        root.left = create(s, 2*index+1)
        root.right = create(s, 2*index+2)
    return root


def treeToNext(root):
    ans = [root.val, "#"]
    cur = root.left
    while cur:
        ans.append(cur.val)
        next = cur.left
        while cur.next:
            ans.append(cur.next.val)
            cur = cur.next
        ans.append("#")
        cur = next
    return ans



class Solution:
    """
    1->2->1->2...->3
    """
    def connect(self, root):
        if not root:
            return None
        cur = root
        next = root.left

        while next:
            cur.left.next = cur.right  # 1. 连左右
            if cur.next:
                cur.right.next = cur.next.left  # 2. 连右左
                cur = cur.next
            else:  # 根节点和最右结点没有next，直接通过Left到下一层
                cur = next
                next = cur.left  # 3. 下一层
        return root


if __name__ == "__main__":
    root = [1, 2, 3, 4, 5, 6, 7]
    root = create(root)
    result = Solution().connect(root)
    result = treeToNext(result)
    print(result)