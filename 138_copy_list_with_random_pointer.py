#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/22 12:58 PM
# @Author : aileen
# @File : 138_copy_list_with_random_pointer.py
# @Software: PyCharm
"""
A linked list is given such that each node contains an additional random pointer which could point
to any node in the list or null.
Return a deep copy of the list.
The Linked List is represented in the input/output as a list of n nodes.
Each node is represented as a pair of [val, random_index] where:

[val]: an integer representing Node.val
[random_index]: the index of the node (range from 0 to n-1) where random pointer points to,
            or null if it does not point to any node.
Example 1:
Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]

Example 2:
Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
"""

# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random



class Solution:
    def build_num_list(self, node):  # node -> []
        cur = node
        out = []
        len_node = 0
        res_node = {}  # 用来存遍历过的 node:index
        unprocessing = []  # 用来存random node还没遍历到的 node
        while cur is not None:
            res_node.setdefault(cur, len_node)
            if cur.random in res_node.keys():
                out.append([cur.val, res_node[cur.random]])
            elif cur.random is not None:
                unprocessing.append(cur)
                out.append([cur.val, None])
            else:
                out.append([cur.val, None])
            cur = cur.next
            len_node += 1
        for node in unprocessing:
            out[res_node[node]][1] = res_node[node.random]
        return out


    def rebuild_node_list(self,num_list):  # [] -> node
        head_node = Node(x=0)
        pre_node = head_node
        len_node = -1
        res_node = {}  # 用来存遍历过的 index:node
        unprocessed_node = []  # 用来存random_index还没遍历到的 index
        for num in num_list:
            len_node += 1
            cur_node = Node(x=num[0], next=None, random=None)
            if num[1] is not None:
                if num[1] < len_node:
                    cur_node.random = res_node[num[1]]
                else:
                    unprocessed_node.append(len_node)
            res_node.setdefault(len_node, cur_node)
            pre_node.next = cur_node
            pre_node = cur_node
        for index in unprocessed_node:
            res_node[index].random = res_node[num_list[index][1]]
        head_node = head_node.next
        return head_node

    def copyRandomList(self, head: 'Node') -> 'Node':
        num_list = self.build_num_list(head)
        node_copy = self.rebuild_node_list(num_list)
        return node_copy


if __name__ == "__main__":
    num_list = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    solution = Solution()
    head = solution.rebuild_node_list(num_list)  # 确保送进去的是node link

    head_node = solution.copyRandomList(head)  # main

    result = solution.build_num_list(head_node)  # 方便查看输出结果
    print(result)