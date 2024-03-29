"""
【完全背包】

有 N 种物品和一个容量是 V 的背包，每种物品都有无限件可用。

第 i 种物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 种物品的体积和价值。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤1000
0<vi,wi≤1000
输入样例
4 5
1 2
2 4
3 4
4 5
输出样例：
10
"""

# n, v = map(int, input().split())
# goods = []
# for _ in range(n):
#     vi, wi = map(int, input().split())
#     goods.append((vi, wi))

# O(N*V)+O(V)
def func(n, v, goods):
    dp = [0] * (v + 1)
    for i in range(1, n + 1):
        for j in range(1, v + 1):
            vi, wi = goods[i - 1]
            if vi <= j:
                dp[j] = max(dp[j], dp[j - vi] + wi)
    print(dp)
    # [0, 2, 4, 6, 8, 10]
    return dp[-1]

n,v=4,5
goods=[(1,2),(2,4),(3,4),(4,5)]
print(func(n, v, goods))