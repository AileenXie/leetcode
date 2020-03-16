#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/15 2:12 PM
# @Author : aileen
# @File : 5359***-_最大的团队表现值.py
# @Software: PyCharm

"""
公司有编号为 1 到 n 的 n 个工程师，给你两个数组 speed 和 efficiency ，其中 speed[i] 和 efficiency[i] 分别代表第 i 位工程师的速度和效率。请你返回由最多 k 个工程师组成的 ​​​​​​最大团队表现值 ，由于答案可能很大，请你返回结果对 10^9 + 7 取余后的结果。

团队表现值 的定义为：一个团队中「所有工程师速度的和」乘以他们「效率值中的最小值」。

 

示例 1：

输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2
输出：60
解释：
我们选择工程师 2（speed=10 且 efficiency=4）和工程师 5（speed=5 且 efficiency=7）。他们的团队表现值为 performance = (10 + 5) * min(4, 7) = 60 。
示例 2：

输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3
输出：68
解释：
此示例与第一个示例相同，除了 k = 3 。我们可以选择工程师 1 ，工程师 2 和工程师 5 得到最大的团队表现值。表现值为 performance = (2 + 10 + 5) * min(5, 4, 7) = 68 。
示例 3：

输入：n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4
输出：72
 

提示：

1 <= n <= 10^5
speed.length == n
efficiency.length == n
1 <= speed[i] <= 10^5
1 <= efficiency[i] <= 10^8
1 <= k <= n

"""


class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        if n == 0:
            return 0
        if k >= n:
            result = sum(speed) * min(efficiency) % (10 ** 9 + 7)
            return result

        max_single = 0
        for p in range(n):
            cur = speed[p] * efficiency[p]
            if cur > max_single:
                max_single = cur
                total = speed[p]
                min_e = efficiency[p]
                index_list = [p]
        dp = [[index_list, total, min_e, max_single]]

        for i in range(k):
            # 计算取i个人的最大团队表现值
            j = i - 1
            if j >= 0:
                max_i = dp[j][3]
                new_index_list = dp[j][0]
                max_total = dp[j][1]
                max_min_e = dp[j][2]
                for p in range(n):
                    if p not in dp[j][0]:  # rest people
                        total = dp[j][1] + speed[p]
                        min_e = min(dp[j][2], efficiency[p])
                        cur_value = (total) * min_e
                        if max_i < cur_value:
                            new_index_list = dp[j][0] + [p]
                            max_total = total
                            max_min_e = min_e
                            max_i = cur_value
                dp.append([new_index_list, max_total, max_min_e, max_i])
            print(f'********count:{i},dp:{dp}')
        final_max = 0
        for plan in range(k):
            if dp[plan][3] > final_max:
                final_max = dp[plan][3]
        return final_max % (10 ** 9 + 7)


if __name__ == "__main__":
    n=6
    speed=[10, 5, 1, 7, 4, 2]
    efficiency=[2, 1, 1, 1, 7, 3]
    k=6
    print(Solution().maxPerformance(n,speed,efficiency,k))
