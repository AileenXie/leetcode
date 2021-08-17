#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/8 9:47 AM
# @Author : aileen
# @File : 周赛0607-4.py
# @Software: PyCharm

class Solution:
    def minCost(self, houses, cost, m: int, n: int, target: int) -> int:
        """
        还需几个街区，当前费用，当前涂哪个房子
        """
        self.min_cost = float('inf')
        self.visited = {}

        def color(i, pre_color, rest, cur_cost):
            if i >= m:  # 全部房子涂完了
                if rest == 0:
                    # print(f'涂完了，刚好满足街区数rest={rest}')
                    self.min_cost = min(self.min_cost, cur_cost)
                    return cur_cost
                else:
                    # print('涂完了，不满足街区数')
                    return -1
            # print(f'涂房子{i}，当前颜色{houses[i]},已用费用{cur_cost}，剩余街区数{rest}')
            if rest < 0:  # 不符合街区数
                # print('不符合街区数')
                return -1
            if (i, pre_color, rest) in self.visited:
                # print('visited')
                return self.visited[(i, pre_color, rest)]
            if houses[i] != 0:  # 已上色
                if houses[i] == pre_color:
                    total_cost = color(i + 1, pre_color, rest, cur_cost)
                else:
                    total_cost = color(i + 1, houses[i], rest - 1, cur_cost)
            else:
                total_cost = float('inf')
                for j, c in enumerate(cost[i]):
                    if j + 1 == pre_color:
                        path_cost = color(i + 1, pre_color, rest, cur_cost + c)
                    else:
                        path_cost = color(i + 1, j + 1, rest - 1, cur_cost + c)
                    if path_cost != -1:
                        print(path_cost)
                        total_cost = min(path_cost, total_cost)
                if total_cost == float('inf'):
                    total_cost = -1
            self.visited.setdefault((i, pre_color, rest), total_cost)
            return total_cost

        if houses[0] != 0:
            color(1, houses[0], target - 1, 0)
        else:
            for color_i, c in enumerate(cost[0]):
                color(1, color_i + 1, target - 1, c)
        print(self.visited)
        return self.min_cost if self.min_cost != float('inf') else -1

if __name__ == "__main__":
    houses=[0, 0, 0, 0, 0]
    cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    m=5
    n=2
    target=3

    # houses=[0, 2, 1, 2, 0]
    # cost=[[1, 10], [10, 1], [10, 1], [1, 10], [5, 1]]
    # m=5
    # n=2
    # target=3
    # houses=[0, 0, 0, 0, 0]
    # cost=[[1, 10], [10, 1], [1, 10], [10, 1], [1, 10]]
    # m=5
    # n=2
    # target=5
    # houses=[3, 1, 2, 3]
    # cost=[[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]]
    # m=4
    # n=3
    # target=3

    print(Solution().minCost(houses, cost, m, n, target))