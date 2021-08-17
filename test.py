#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/15 10:15 AM
# @Author : aileen
# @File : test.py
# @Software: PyCharm


# visited = [[0]*4]*5
# visited=[[0,0,0],[0,0,0]]
# visited=[[0 for col in range(4)] for row in range(5)]
# visited = [0]*4
# visited[0]=1
# print(visited)


# a = [1,2,3,4]
# b = [a[i]+1 for i in range(len(a))]
# print(b)
#
# print(min(1,2))
# print(sum(a))
# print(a+[3,4])
# print(1e9 + 7 == 10**9+7)
#
#
# print(583438149971672%(1e9+7))


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# print(matrix is matrix[:])
# print(matrix)
# print(*matrix)  # *matrix是3个变量：[1,2,3]、 [4,5,6] 和 [7,8,9]
# for i in zip(*matrix):
#     print(list(i))
# print(id(matrix))
# matrix[:] = map(list, zip(*matrix))  # 返回的是3个变量 [1,4,7]、[2,5,8] 和 [3,6,9]
# print(matrix)
# print(id(matrix))


# a = [1,2]
# print(a[4:])  # 会返回[]

# a = "-1E-1 "
# print(float(a))

# dp = [(0,0,0) for _ in range(3)]
# dp[1:3]=(4,4,1),(5,7,8)
# print(dp)
# print(sum(dp[2]))

# a = "1 2 3 4"
# b = a.split()
# print(b)

# n,m = input().split()
# n, m = int(n), int(m)
# Q = input().split()
# L = input().split()
# label = {}
# for i,l in enumerate(L):
#     label.setdefault(l,[]).append(i)
# score = 0
# for l in label.keys():
#     for i,index in enumerate(label[l][1:],1):
#         for j in range(i):
#             index_a = label[l][j]
#             index_b = label[l][i]
#             score += (index_a+index_b)*(int(Q[index_a])+int(Q[index_b]))
# print(score)

# n = int(input())
# num = input().split()
# nums = [int(i) for i in num]
# min_step = float('inf')
# for i,num in enumerate(nums):
#     visited = [i]
#     step = 0
#     while True:
#         if num-1 not in visited:
#             visited.append(num - 1)
#             num = nums[num-1]
#             step += 1
#         else:
#             if num-1 == i and step < min_step:
#                 min_step = step
#             break
# print(min_step)


# a = [1,2,3]
# b = [5,6,7]
# c1,c2,c3 = zip(a,b)
# d = zip(a,b)
# print(c1)  # (1,5)
# print(*d)  #


def P(x):
    y = map(lambda x, y: x * y, map(int, str(x)))
    return y and not x % y
def Q(x):
    return P(x) and P(x + 1)
print(sum(Q(x) for x in range(2019)))
