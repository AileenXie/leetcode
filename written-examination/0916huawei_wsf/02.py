#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/16 7:14 PM
# @Author : aileen
# @File : 02.py
# @Software: PyCharm
"""
判断图对称性
返回对称轴元素和
"""

# class Solution:
#     def __init__(self):
#         self.layer = {}
#
#     def getLayer(self, node, l):
#         self.layer.setdefault(l,[])
#         if node is None:
#             self.layer[l].append(None)
#             return l
#         self.layer[l].append(node.val)
#         return max(self.getLayer(node.left, l+1),self.getLayer(node.right, l+1))
#
#     def isSym(self, nums):
#         n = len(nums)
#         i, j = 0, n-1
#         while i<j:
#             if nums[i] != nums[j]:
#                 return False
#             i += 1
#             j -= 1
#         return True
#
#     def isSymmetric(self, root: TreeNode) -> bool:
#         if root is None:
#             return True
#         layer = self.getLayer(root,0)
#         for i in range(layer+1):
#             if not self.isSym(self.layer[i]):
#                 return False
#         return True

class Solution:
    def func(self, s, e, n, edege):
        dic = {}
        for (a,b) in edege:
            dic.setdefault(a,[]).append(b)
            dic.setdefault(b,[]).append(a)
        l=[(s,0)]  # 用于层次遍历
        r=[(e,0)]
        l_layer={0:[s]}  # 用于记录同层元素
        r_layer={0:[r]}
        l_visited = set()  # 用于记录走过的点
        r_visited = set()
        pre_layer=-1  # 用于判断层数是否发生变化
        while True:
            left,ll = l.pop(0)
            right,rl = r.pop(0)
            l_visited.add(left)
            r_visited.add(right)
            if ll != rl:  # 不对称
                return 0
            if ll != pre_layer and ll!=0:  # 遍历到新的一层了，比对上一层
                if l_layer[pre_layer]==r_layer[pre_layer]:  # 到达对称轴
                    return sum(l_layer[pre_layer])
            pre_layer=ll  # 更新上一层数
            # 层次遍历
            over = True
            for i in dic[left]:
                if i in l_visited: continue
                l_layer.setdefault(ll+1,[]).append(i)
                l.append((i,ll+1))
                over=False
            if over: return 0  # 遍历完所有结点
            over = True
            for i in dic[right]:
                if i in r_visited: continue
                r_layer.setdefault(rl+1,[]).append(i)
                r.append((i,rl+1))
                over=False
            if over: return 0

print(Solution().func(1,3,4,[(1,2),(2,3),(1,4),(3,4)]))
print(Solution().func(1,3,5,[(1,5),(5,6),(5,7),(3,6),(3,7)]))




