"""
输入：
T个测试用例
n
n个数

输出：
最大山谷长度

例如：
输入：
3
9
5 4 3 2 1 2 3 4 5
5
1 2 3 4 5
14
87 70 17 12 14 86 61 51 12 90 69 89 4 65

输出：
9
0
6

"""


# 0%
def func(n, nums):
    dp1 = [0]*n  # i左边比自己大的数
    dp2 = [0]*n  # i右边比自己大的数
    for i in range(1,n):
        if nums[i]<nums[i-1]:
            dp1[i]=dp1[i-1]+1
        else:
            j=i-1
            while j>=0 and nums[j]<=nums[i]:
                j-=1
            if j<0: dp1[i]=0
            else: dp1[i]=dp1[j]+1
    for i in range(n-2,-1,-1):
        if nums[i] < nums[i+1]:
            dp2[i]=dp2[i+1]+1
        else:
            j=i+1
            while j<n and nums[j]<=nums[i]:  # case 3有问题！！！
                j+=1
            if j==n: dp2[i]=0
            else: dp2[i]=dp2[j]+1
    max_len = 0
    # 奇数山谷
    for i in range(n):
        cur_half=min(dp1[i], dp2[i])
        cur = cur_half*2+1 if cur_half else 0
        max_len=max(max_len,cur)
    # 偶数山谷
    for i in range(n):  # 找两个相同的数作为山谷底
        for j in range(i+1,n):
            if nums[i]==nums[j]:
                cur_half = min(dp1[i], dp2[j])
                cur = cur_half*2+2 if cur_half else 0
                max_len = max(max_len, cur)
    print(dp1)
    print(dp2)
    return max_len


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    nums = list(map(int, input().strip().split()))
    print(func(n, nums))

