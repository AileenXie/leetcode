#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 10:37 AM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm

n, k = map(int, input().strip().split())
number = input().strip()


def func(n, k, number):
    if k < 2:
        return 0
    dic = {}
    loc = {}
    exist = []
    for index, num in enumerate(number):
        dic.setdefault(num, 0)
        dic[num] += 1
        if dic[num]>k:
            return 0, number
        loc.setdefault(num, []).append(index)
        if num not in exist:
            exist.append(num)
    exist.sort()

    min_cost = float('inf')
    available = []
    for i, key in enumerate(exist):
        cost = 0
        need = k - dic[key]
        j = 1
        new_number = list(number)
        alter = [abs(int(value) - int(key)) for value in exist]
        rank = [index for index, value in sorted(list(enumerate(alter)), key=lambda x: x[1])]
        new_exist = [exist[ii] for ii in rank]
        while need:
            if cost > min_cost:
                break
            if dic[new_exist[j]] >= need:
                cost += need * abs(int(new_exist[j]) - int(key))
                if new_exist[j] > key:  # 从前往后改
                    for l in loc[new_exist[j]][:need]:
                        new_number[l] = key
                else:  # 从后往前
                    for l in loc[new_exist[j]][-need:]:
                        new_number[l] = key
                need = 0
            else:
                cur_need = dic[new_exist[j]]
                cost += cur_need * abs(int(new_exist[j]) - int(key))
                need -= cur_need
                for l in loc[new_exist[j]]:  # 全改
                    new_number[l] = key
                j += 1
        if cost < min_cost:
            min_cost = cost
            available=[]  # 清空
            available.append(''.join(new_number))
        if cost == min_cost:
            available.append(''.join(new_number))
    available.sort()
    return min_cost, available[0]

min_cost,ans = func(n, k, number)
print(min_cost)
print(ans)



