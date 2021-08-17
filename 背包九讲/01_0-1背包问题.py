"""
【0-1背包】

有 N 件物品和一个容量是 V 的背包。每件物品只能使用一次。

第 i 件物品的体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使这些物品的总体积不超过背包容量，且总价值最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品数量和背包容积。

接下来有 N 行，每行两个整数 vi,wi，用空格隔开，分别表示第 i 件物品的体积和价值。

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
8
"""

# n, v = map(int, input().split())
# goods = []
# for _ in range(n):
#     vi, wi = map(int, input().split())
#     goods.append((vi, wi))
"""
定义dp[i][j]为前i件物品在j容量内能装入的最大价值
dp[i][j]=dp[i-1,j]  # i物品不放入背包
dp[i][j]=dp[i-1][j-vi]+wi  # i物品放入背包
dp[0][j]=0,dp[i][0]=0
"""
# O(N*V)+O(N*V)
def func1(n, v, goods):
    dp = [[0 for _ in range(v + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, v + 1):
            dp[i][j] = dp[i - 1][j]
            vi, wi = goods[i - 1]
            if vi <= j:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - vi] + wi)
    print(dp)
    # [[0, 0, 0, 0, 0, 0],
    #  [0, 2, 2, 2, 2, 2],
    #  [0, 2, 4, 6, 6, 6],
    #  [0, 2, 4, 6, 6, 8],
    #  [0, 2, 4, 6, 6, 8]]
    return dp[-1][-1]
"""
空间维度压缩O(n*v)——>O(v)
因为dp[i]只与dp[i-1]有关
"""
# O(N*V)+O(V)
def func2(n,v,goods):
    dp=[0 for _ in range(v+1)]
    for i in range(1,n+1):
        for j in range(v,0,-1):  # 从后向前，防止从前向后过程中要用到的dp[i-1][xx]的位置被dp[i][xx]覆盖
            vi,wi=goods[i-1]
            if vi<=j:
                dp[j]=max(dp[j],dp[j-vi]+wi)
    print(dp)
    # [0, 2, 4, 6, 6, 8]
    return dp[-1]




n,v=4,5
goods=[(1,2),(2,4),(3,4),(4,5)]
print(func1(n, v, goods))
print(func2(n, v, goods))