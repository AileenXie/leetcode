"""
航海： 求最少危险区域休息次数。

输入：
目标历程x
每日航行范围[l,t], 危险区域n个
具体n个危险区域。

输出：
最少经过危险区域次数

10
2 3 4
5 3 2 6

1
——————————
10
1 3 4
5 3 2 6

0
——————————
10
2 3 5
1 3 5 6 7

1
——————————
10
2 3 8
0 1 2 3 4 5 6 7

1
"""
x = int(input().strip())
l, t, n = map(int, input().strip().split())
a = list(map(int, input().strip().split()))


# 9% ？？？
import functools
class Solution:
    def func(self,x, l, t, n, a):
        if not n: return 0
        dange = set(a)
        max_d = max(a)
        # print(dange)
        @functools.lru_cache(None)
        def dfs(cur, count):
            if cur > max_d:
                return count
            if cur in dange: count += 1  # 包括当前位置在内，经过的危险区域个数
            cur_count=float("inf")
            for i in range(l,t+1):
                cur_count=min(cur_count,dfs(cur+i,count))
            return cur_count
        return dfs(0,0)
print(Solution().func(x,l,t,n,a))

# 70%
def func(x,l,t,n,a):
    dp=[float("inf") for _ in range(10002)]
    dp[0]=0 if 0 not in a else 1
    for i in range(len(dp)):
        for step in range(l,t+1):
            dp[i]=min(dp[i-step],dp[i])
        if i in a:
            dp[i]+=1
    print(dp)
    return dp[-1]
print(func(x,l,t,n,a))
