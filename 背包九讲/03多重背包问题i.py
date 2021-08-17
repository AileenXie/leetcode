"""
【多重背包 I】

有 N 种物品和一个容量是 V 的背包。

第 i 种物品最多有 si 件，每件体积是 vi，价值是 wi。

求解将哪些物品装入背包，可使物品体积总和不超过背包容量，且价值总和最大。
输出最大价值。

输入格式
第一行两个整数，N，V，用空格隔开，分别表示物品种数和背包容积。

接下来有 N 行，每行三个整数 vi,wi,si，用空格隔开，分别表示第 i 种物品的体积、价值和数量。

输出格式
输出一个整数，表示最大价值。

数据范围
0<N,V≤100
0<vi,wi,si≤100
输入样例
4 5
1 2 3
2 4 1
3 4 3
4 5 2
输出样例：
10
"""


# n, v = map(int, input().split())
# goods = []
# for _ in range(n):
#     vi, wi, si = map(int, input().split())
#     goods.append((vi, wi, si))

# O(N*V*S)+O(V)
def func(n,v,goods):
    dp=[0]*(v+1)
    for i in range(1,n+1):
        for j in range(v,0,-1):
            vi, wi, si = goods[i-1]
            for k in range(1,si+1):  # 加一层循环，遍历每个物品的取值个数，0个,1个,...,k个
                if k*vi<=j:
                    dp[j]=max(dp[j],dp[j-k*vi]+k*wi)
    return dp[-1]


n,v=4,5
goods=[(1,2,3),(2,4,1),(3,4,3),(4,5,2)]
print(func(n,v,goods))