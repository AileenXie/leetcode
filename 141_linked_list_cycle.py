#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/22 5:39 PM
# @Author : aileen
# @File : 141_linked_list_cycle.py
# @Software: PyCharm

"""
Given a linked list, determine if it has a cycle in it.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.


Example 1:

Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the second node.


Example 2:

Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:

Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.


Follow up:
Can you solve it using O(1) (i.e. constant) memory?
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def list_to_node(x,pos):
    head = ListNode(x[0])
    p = head
    back = None
    for i in range(0,len(x)):
        p.next = ListNode(x[i])
        p = p.next
        if i == pos:
            back = p
    if back is not None:
        p.next = back
    return head.next

def node_to_list(head):
    x = []
    p = head
    visited = {}
    pos = -1
    index = 0
    while p:
        if p not in visited.keys():
            x.append(p.val)
            visited.setdefault(p, index)
            p = p.next
        else:
            pos = visited[p]
            break
        index += 1
    return x, pos


class Solution:
    """
    不破坏原链表
    Runtime: 48ms, faster than 64.66%(visited用字典！！，用列表耗时1196 ms, faster than 5.11%)
    Memory Usage: 15.9 MB, less than 100.00%
    """
    def hasCycle(self, head: ListNode) -> bool:
        p = head
        visited = {}
        while p:
            if p not in visited:
                visited.setdefault(p, 0)  # 只存key，value无用，为了查找更快
                p = p.next
            else:
                return True
        return False
    """
    巧思：有环，快跑和慢跑终会相遇
    Runtime: 48 ms, faster than 64.66%
    Memory Usage: 15.8 MB, less than 100.00% 
    """

    def hasCycle1(self, head: ListNode) -> bool:
        fast = slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if fast == slow:
                return True

        return False
    """
    破坏链表
    Runtime: 48 ms, faster than 64.66%
    Memory Usage: 15.6 MB, less than 100.00% 
    """
    def hasCycle2(self, head: ListNode) -> bool:
        while head:
            if head.val is None:
                return True
            pre = head
            head = head.next
            pre.val=None
        return False


if __name__ == "__main__":
    head = [1, 2]
    pos = 0
    node = list_to_node(head, pos)
    print(Solution().hasCycle(node))
