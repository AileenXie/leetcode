#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/26 8:00 PM
# @Author : aileen
# @File : 02最大面积.py
# @Software: PyCharm
"""
柱状图给出了每个柱子的宽度和高度，求柱状图内最大矩形面积

输入：
[1,1,1,1,2,1,1]
[5,2,5,4,5,1,6]

输出：
16
"""

# n, k = map(int, input().strip().split())
# numbers = list(map(int,input().strip().split()))

# ww,hh=input().strip().split("],[")
# ww=ww[1:]
# hh=hh[:-1]
# w=list(map(int,ww.split(",")))
# h=list(map(int,hh.split(",")))
# print(w,h)
def func(w,h):
    n=len(w)
    if not n or len(h)!=n: return 0
    h=[0]+h+[0]
    w=[0]+w+[0]
    stack=[(0,0)]  # 补一个最低点，高度递增单调栈。
    ans = 0
    start=0
    for i in range(1,n+2):
        start+=w[i]  # 每个柱子右下角Index
        if i!=n+1 and (w[i]<=0 or h[i]<=0): return 0  # 不合法
        while stack and h[i]<stack[-1][1]:  # 遇到更小的柱子，单调栈开始pop，知道加入新柱子依然保持递增
            _,cur_h = stack.pop()
            ans = max(ans,(cur_h*(start-w[i]-stack[-1][0])))  # 高度*单调栈现存的最右下角坐标到当前柱子左下角坐标距离（宽度）
        stack.append((start,h[i]))
    return ans


w=[1,1,1,1,2,1,1]
h=[4,4,4,1,3,3,3]
# w=[1,1,1,1,2,1,1]
# h=[5,2,5,4,5,1,6]
print(func(w,h))


"""
未知题1
"""
# import collections
# def func(n,users):
#     # count = collections.Counter(users)
#     dic = {}
#     ans = 0
#     for u in users:
#         dic.setdefault(u,0)
#         dic[u]+=1
#         ans = max(ans,dic[u])
#     return ans
#
# n=11
# users=[11,34,34,9,23,23,23,29,12,12,28]
# n=3
# users=[2,3,4]
# print(func(n,users))
"""
未知题2
"""
# def func(n,nums):
#     h=0
#     # while 2**h-1<n:
#     #     h+=1
#     # left = 2**(h-1)-1
#     global ans
#     ans=[]
#
#     def inorder(cur):
#         if nums[cur]==-1:
#             return
#         if cur*2+1<n:
#             inorder(cur*2+1)
#         ans.append(nums[cur])
#         if cur*2+2<n:
#             inorder(cur*2+2)
#     inorder(0)
#     return ans
#
# print(func(7,[1,2,9,5,-1,7,6]))