#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/2/2 5:18 PM
# @Author : aileen
# @File : 134_gas_station*.py
# @Software: PyCharm
"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1.

Note:

If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
Example 1:

Input:
gas  = [1,2,3,4,5]
cost = [3,4,5,1,2]

Output: 3

Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
Example 2:

Input:
gas  = [2,3,4]
cost = [3,4,3]

Output: -1

Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
"""


class Solution:
    def canCompleteCircuit(self, gas, cost):
        res = [i-j for i, j in zip(gas, cost)]
        print(res)
        if sum(res) < 0:
            return -1
        """
        遍历起始点，会TimeLimit
        """
        # for i in range(len(res)):  # 从i开始
        #     if i < 0:
        #         continue
        #     bak = res.copy()
        #     bak_i = i
        #     cur_sum = 0
        #     flag = 1
        #     while bak:
        #         if len(bak) <= bak_i:
        #             bak_i = 0
        #         cur_sum = cur_sum + bak[bak_i]
        #         if cur_sum < 0:
        #             flag = 0
        #             break
        #         bak.pop(bak_i)
        #     if flag:
        #         return i
        start, cur = 0, 0
        cur_sum = 0
        step = 1
        l = len(res)
        while step < l:
            if cur >= l:
                cur = 0  # 到开头
            cur_sum = cur_sum + res[cur]
            cur += 1
            step += 1
            while cur_sum < 0:  # 起始点逆时针向前补足!!!
                start = start - 1
                if start < 0:
                    start = l-1  # 到末尾
                cur_sum = cur_sum + res[start]
                step += 1
        return start


if __name__ == "__main__":
    gas = [2, 3, 4]  # -1
    cost = [3, 4, 3]
    gas = [1, 2, 3, 4, 5]  # 3
    cost = [3, 4, 5, 1, 2]
    # gas = [5, 1, 2, 3, 4]  # 4
    # cost = [4, 4, 1, 5, 1]
    # gas = [5, 8, 2, 8]  # 3
    # cost = [6, 5, 6, 6]
    result = Solution().canCompleteCircuit(gas, cost)
    print(result)