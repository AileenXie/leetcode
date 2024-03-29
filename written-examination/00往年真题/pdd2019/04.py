#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/5/6 11:35 AM
# @Author : aileen
# @File : 04多重背包问题ii.py
# @Software: PyCharm

"""
你在玩一个回合制角色扮演的游戏。现在你在准备一个策略，以便在最短的回合内击败敌方角色。在战斗开始时，敌人拥有HP格血量。当血量小于等于0时，敌人死去。一个缺乏经验的玩家可能简单地尝试每个回合都攻击。但是你知道辅助技能的重要性。
在你的每个回合开始时你可以选择以下两个动作之一：聚力或者攻击。
    聚力会提高你下个回合攻击的伤害。
    攻击会对敌人造成一定量的伤害。如果你上个回合使用了聚力，那这次攻击会对敌人造成buffedAttack点伤害。否则，会造成normalAttack点伤害。
给出血量HP和不同攻击的伤害，buffedAttack和normalAttack，返回你能杀死敌人的最小回合数。

输入描述:
第一行是一个数字HP
第二行是一个数字normalAttack
第三行是一个数字buffedAttack
1 <= HP,buffedAttack,normalAttack <= 10^9

输出描述:
输出一个数字表示最小回合数

输入例子1:
13
3
5

输出例子1:
5
"""

hp = int(input().strip())
normal = int(input().strip())
buffed = int(input().strip())


def func(hp,normal,buffed):
    if hp <=0:
        return 0
    min_count = float('inf')
    stack = [(1,hp,0)]  # pre_operate, rest_blood, count
    visited = []
    while stack:
        pre_operate, rest_blood, count = stack.pop()
        if (rest_blood,count) in visited:
            continue
        if count > min_count:
            continue
        if rest_blood <= 0:
            min_count = count
            continue
        visited.append((rest_blood,count))
        if pre_operate==0:  # 上次蓄力
            stack.append((0,rest_blood,count+1))
            stack.append((1,rest_blood-buffed,count+1))
        else:  # 上次攻击
            stack.append((0,rest_blood,count+1))
            stack.append((1,rest_blood-normal,count+1))
    return min_count

print(func(hp,normal,buffed))

