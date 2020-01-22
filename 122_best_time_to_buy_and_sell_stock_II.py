#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/01/21 14:32 PM
# @Author : aileen
# @File : 122_best_time_to_buy_and_sell_stock_II.py
# @Software: PyCharm

"""
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example 1:

Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Example 2:

Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
"""


# 多次买卖，求最大收益
class Solution:
    """
    方案一：下降前卖出，上升前买入
    """
    # def maxProfit(self, prices) -> int:
    #     if len(prices) < 2:
    #         return 0
    #     profit = 0
    #     buy = prices[0]
    #     buy_flag = True
    #     pre_price = prices[0]
    #     for i in prices[1:]:
    #         if buy_flag:
    #             if i < pre_price:
    #                 profit = profit + (pre_price - buy)
    #                 buy_flag = False
    #         else:
    #             if i > pre_price:
    #                 buy = pre_price
    #                 buy_flag = True
    #         pre_price = i
    #     if buy_flag:
    #         profit += prices[-1] - buy
    #     return profit

    """
    方案二： 最大收益等价于算全部前后两天的正收益
    """
    def maxProfit(self, prices):
        return sum(max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1))


if __name__ == "__main__":
    # prices = [7,1,5,3,6,4]
    # prices = [7,6,4,3,1]
    # prices = [1,2,3,4,5]
    prices = []
    result = Solution().maxProfit(prices)
    print(result)