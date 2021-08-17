#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/19 2:20 PM
# @Author : aileen
# @File : 02.py
# @Software: PyCharm


"""
(let x 2 (mult (let x 3 (let x 4 x)) x))
8

"""


# s = input().strip()
#
#
# def func(s):
#     n=len(s)
#     i=0
#
#     def get_str(i):  # 获得以i开头的字符串
#         cur = s[i]
#         if cur.isalpha():
#             i += 1
#             while i < len(s) and s[i].isalpha():
#                 cur += s[i]
#                 i += 1
#         return cur,i
#
#     def comput(i,j):
#         left_val = None
#         right_val = None
#         op=None
#         dic = {}  # 变量名和变量值
#         while i<j:
#             cur = s[i]
#             if cur ==" ":
#                 i+=1
#                 continue
#             if cur == "(":
#
#             if cur.isalpha():
#                 opt, i = get_str(i)
