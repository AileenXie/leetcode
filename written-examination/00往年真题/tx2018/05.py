#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/26 3:18 PM
# @Author : aileen
# @File : 05混合背包问题.py
# @Software: PyCharm
"""
小Q的公司最近接到m个任务, 第i个任务需要xi的时间去完成, 难度等级为yi。
小Q拥有n台机器, 每台机器最长工作时间zi, 机器等级wi。
对于一个任务,它只能交由一台机器来完成, 如果安排给它的机器的最长工作时间小于任务需要的时间, 则不能完成,如果完成这个任务将获得200 * xi + 3 * yi收益。

对于一台机器,它一天只能完成一个任务, 如果它的机器等级小于安排给它的任务难度等级, 则不能完成。

小Q想在今天尽可能的去完成任务, 即完成的任务数量最大。如果有多种安排方案,小Q还想找到收益最大的那个方案。小Q需要你来帮助他计算一下。


输入描述:
输入包括N + M + 1行,
输入的第一行为两个正整数n和m(1 <= n, m <= 100000), 表示机器的数量和任务的数量。
接下来n行,每行两个整数zi和wi(0 < zi < 1000, 0 <= wi <= 100), 表示每台机器的最大工作时间和机器等级。
接下来的m行,每行两个整数xi和yi(0 < xi < 1000, 0 <= yi<= 100), 表示每个任务需要的完成时间和任务的难度等级。

输出描述:
输出两个整数, 分别表示最大能完成的任务数量和获取的收益。

输入例子1:
1 2
100 3
100 2
100 1

输出例子1:
1 20006
"""


# def func(n,m,machine,target):
#     # 优先考虑最多任务数，然后考虑收益
#     machine = sorted(machine,reverse=True)
#     target = sorted(target,reverse=True)
#     available_level = [0]*101  # 存放可用机器
#     mac = 0  # 当前遍历到的机器编号
#     count = 0  # 最大能完成的任务数
#     profit = 0  # 获取的收益
#     for need_time, hard_level in target:
#         # 遍历机器，记录所有满足当前任务时间要求的可用机器
#         # mac是持续增长的，符合前一个任务的机器必然符合后一个任务，因为已做排序
#         while mac < n and machine[mac][0]>=need_time:  # 控制遍历，找出当前任务的所有可行机器
#             run_time, level = machine[mac]
#             available_level[level]+=1
#             mac += 1
#         # 在现有可行机器中找到level最接近的
#         for i in range(hard_level,101):
#             if available_level[i] > 0:
#                 available_level[i]-=1
#                 count += 1
#                 profit += 200 * need_time + 3 * hard_level
#                 break  # 找到一个就可以了
#     print(count, profit)
#
#
#
# n,m = map(int, input().split())
# machine=[]
# target = []
# for _ in range(n):
#     run_time,level = map(int, input().split())
#     machine.append((run_time,level))
# for _ in range(m):
#     need_time,hard_level = map(int, input().split())
#     target.append((need_time,hard_level))
# func(n, m, machine, target)

def func(n, m, machines, jobs):
    # n 机器数， m 任务数
    machines.sort(reverse=True)
    jobs.sort(reverse=True)
    index = 0
    available_level = [0] * 101
    count = 0
    profit = 0
    for need_time, need_level in jobs:
        # 从前往后找到符合当前任务运行时间的机器，对应level放入available_level
        while index < n and machines[index][0] >= need_time:
            available_level[machines[index][1]] += 1
            index += 1
        # 从最低要求的level往后找，找到Level最进的可用机器用来执行当前任务
        for l in range(need_level, 101):
            if available_level[l] > 0:
                available_level[l] -= 1  # 把这个机器拿来用
                count += 1
                profit += 200 * need_time + 3 * need_level
                break
    print(count, profit)


n, m = map(int, input().strip().split())
machines = []
jobs = []
for _ in range(n):
    run_time, run_level = map(int, input().strip().split())
    machines.append((run_time, run_level))
for _ in range(m):
    need_time, need_level = map(int, input().strip().split())
    jobs.append((need_time, need_level))
func(n, m, machines, jobs)