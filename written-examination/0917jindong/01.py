"""
多重背包
# 物品n 最大预算p
物品1数量，价格，价值
...
物品n数量，价格，价值

输出最大价值

3 10
2 2 3
1 5 10
2 4 12

27
"""
n, p = map(int, input().strip().split())
goods = []
for i in range(n):
    count, price, value = map(int, input().strip().split())
    base = 1
    while count > base:
        count -= base
        goods.append((price * base, value * base))
        base *= 2
    if count:
        goods.append((price * count, value * count))


def func(n, p, goods):
    dp=[0]*(p+1)
    for i in range(len(goods)):  # 遍历物品
         price,value=goods[i]
         for j in range(p,0,-1):
             if j>=price:
                 dp[j]=max(dp[j],dp[j-price]+value)
    return dp[-1]

print(func(n,p,goods))

