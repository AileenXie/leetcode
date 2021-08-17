"""
【二维费用的背包问题】背包有2个限制条件，2层条件循环

有 N 件物品和一个容量是 V 的背包，背包能承受的最大重量是 M。

每件物品只能用一次。体积是 vi，重量是 mi，价值是 wi。

求解将哪些物品装入背包，可使物品总体积不超过背包容量，总重量不超过背包可承受的最大重量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V,M，用空格隔开，分别表示物品件数、背包容积和背包可承受的最大重量。

接下来有 N 行，每行三个整数 vi,mi,wi，用空格隔开，分别表示第 i 件物品的体积、重量和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N≤1000
0<V,M≤100
0<vi,mi≤100
0<wi≤1000
输入样例
4 5 6
1 2 3
2 4 4
3 4 5
4 5 6
输出样例：
8
"""

n, v, m = map(int, input().split())
goods = []
for _ in range(n):
    vi, mi, wi = map(int, input().split())
    goods.append((vi, mi, wi))


# O(N*V*M)+O(V*M)
def func(n, v, m, goods):
    dp = [[0 for _ in range(m + 1)] for _ in range(v + 1)]  # dp[i][j]表示体积i内重量j内的最大价值
    for vi, mi, wi in goods:
        for i in range(v, vi - 1, -1):  # 从后向前
            for j in range(m, mi - 1, -1):  # 2层遍历
                dp[i][j] = max(dp[i][j], dp[i - vi][j - mi] + wi)
    return dp[-1][-1]


print(func(n, v, m, goods))