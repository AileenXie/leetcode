#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/28 3:24 PM
# @Author : aileen
# @File : 146_LRU_cache.py
# @Software: PyCharm
"""
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

The cache is initialized with a positive capacity.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
"""

"""
Runtime: 212 ms, faster than 60.45% 
Memory Usage: 22.3 MB, less than 7.57% 

双链表DoubleLink
"""


class Node:
    def __init__(self, value, next=None, pre=None):
        self.value = value
        self.next = next
        self.pre = pre


class LRUCache:

    def __init__(self, capacity: int):
        self.position = {}  # key->node
        self.start = None
        self.end = None
        self.dic = {}
        self.capacity = capacity

    def move_node_to_end(self, key):
        cur_node = self.position[key]
        print("cur_node : {}".format(cur_node))
        if cur_node.next is not None:  # 只处理非链尾的情况，链尾不用动
            if cur_node.pre is not None:  # 非链首
                cur_node.pre.next = cur_node.next
                cur_node.next.pre = cur_node.pre
            else:  # 链首
                self.start = cur_node.next  # 当前结点位于链首
                cur_node.next.pre = cur_node.pre
            cur_node.pre = self.end
            cur_node.next = None
            self.end.next = cur_node
            self.end = cur_node

    def add_node_to_end(self, key):
        cur_node = Node(key)
        self.end.next = cur_node
        cur_node.pre = self.end
        cur_node.next = None
        self.end = cur_node
        self.position.setdefault(key, cur_node)  # 新增地址

    def replace_node(self, key):
        cur_node = Node(key)
        delete_node = self.start
        self.position.pop(delete_node.value)  # 移出地址字典
        self.position.setdefault(key, cur_node)  # 新增地址

        if delete_node.next is None:  # 位于链尾
            self.start = cur_node
            self.end = cur_node
        else:
            self.start = delete_node.next  # 重置start位
            self.start.pre = None
            self.end.next = cur_node
            cur_node.pre = self.end
            self.end = cur_node

    def init_link(self, key):
        cur_node = Node(key)
        self.start = cur_node
        self.end = cur_node
        self.position = {key: cur_node}

    def get(self, key: int) -> int:
        # 无key
        if key not in self.dic.keys():
            return -1
        # 有key
        self.move_node_to_end(key)  # 活跃的放到列表末尾
        print("_________get__________")
        print(self.dic)
        print(self.position)
        print(self.start)
        print(self.end)
        return self.dic[key]

    def put(self, key: int, value: int) -> None:
        # key未满
        dic_len = len(self.dic)
        if dic_len == 0:  # 键空
            self.init_link(key)
            self.dic.setdefault(key, value)
        elif key in self.dic:  # 键存在，更新
            self.move_node_to_end(key)  # link
            self.dic[key]=value
        elif dic_len < self.capacity:  # 键未满
            self.add_node_to_end(key)
            self.dic.setdefault(key, value)
        elif dic_len == self.capacity:  # 键满
            self.dic.pop(self.start.value)  # 删除最不活跃
            self.replace_node(key)  # 替换掉非活跃结点
            self.dic.setdefault(key, value)
        print("_________put__________")
        print(self.dic)
        print(self.position)


# class LRUCache:
#     """
#     Runtime: 644 ms, faster than 8.18%
#     Memory Usage: 21.9 MB, less than 36.36%
#     """
#
#     def __init__(self, capacity: int):
#         self.active_key = []  # 最不活跃的放第一
#         self.dic = {}
#         self.capacity = capacity
#
#     def get(self, key: int) -> int:
#         # 无key
#         if key not in self.dic.keys():
#             return -1
#         # 有key
#         self.active_key.remove(key)
#         self.active_key.append(key)  # 活跃的放到列表末尾
#         return self.dic[key]
#
#     def put(self, key: int, value: int) -> None:
#         # key未满
#         dic_len = len(self.dic)
#         # print(dic_len)
#         # print(self.dic)
#         # print(self.active_key)
#         if key in self.dic:  # 键存在，更新
#             self.dic[key] = value
#             self.active_key.remove(key)
#             self.active_key.append(key)  # 活跃的放到列表末尾
#         elif dic_len < self.capacity:  # 键空
#             self.dic.setdefault(key, value)
#             self.active_key.append(key)
#         elif dic_len == self.capacity:  # 键满
#             self.dic.pop(self.active_key[0])  # 删除最不活跃
#             self.dic.setdefault(key,value)
#             self.active_key.pop(0)
#             self.active_key.append(key)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
if __name__ == "__main__":
    # action = ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
    # content = [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]

    # action = ["LRUCache", "put", "get"]
    # content = [[1], [2, 1], [2]]

    # action = ["LRUCache", "put", "put", "get", "put", "put", "get"]
    # content = [[2], [2, 1], [2, 2], [2], [1, 1], [4, 1], [2]]

    action = ["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
    content = [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]

    # action = ["LRUCache","put","get","put","get","get"]
    # content = [[1],[2,1],[2],[3,2],[2],[3]]

    result = [None]
    obj = LRUCache(content[0][0])
    for ii in range(1, len(action)):
        if action[ii] == "put":
            print(f"\nput {content[ii]}")
            obj.put(content[ii][0], content[ii][1])
            result.append(None)
        elif action[ii] == "get":
            print(f"\nget {content[ii]}")
            value = obj.get(content[ii][0])
            result.append(value)
    print(result)
