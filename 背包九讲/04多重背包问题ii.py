"""
【多重背包问题 II】
—— i物品7个可选，朴素做法：for k in range(1,8)讨论每个选法的取值
—— 优化做法【二进制优化】：把7拆成1 2 4（三位二进制）考虑3个选与不选的问题，可以完美组合出所有[1,7]的选择情况

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
0<N≤1000
0<V≤2000
0<vi,wi,si≤2000
提示：
本题考查多重背包的二进制优化方法。

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
# goods = []  # 直接在输入的时候进行组合
# for _ in range(n):
#     vi, wi, si = map(int, input().split())
#     k = 1
#     while k <= si:
#         goods.append((vi * k, wi * k))
#         si -= k
#         k *= 2
#     if si:
#         goods.append((vi * si, wi * si))


# O(N*V*log(s))+O(V)
def func(n, v, goods):
    dp = [0] * (v + 1)
    new_goods=[]  # 个数不同拆分组合成新的物品
    for vi,wi,si in goods:
        k = 1  # 拆分为1，2，4，...，rest。如9=1+2+4+2；10=1+2+4+3
        while k <= si:
            new_goods.append((vi * k, wi * k))
            si -= k
            k *= 2
        if si:
            new_goods.append((vi * si, wi * si))

    for vi, wi in new_goods:
        for j in range(v, 0, -1):
            if vi <= j:
                dp[j] = max(dp[j], dp[j - vi] + wi)
    # print(dp)
    return dp[-1]

n,v=4,5
goods=[(1,2,3),(2,4,1),(3,4,3),(4,5,2)]
print(func(n, v, goods))