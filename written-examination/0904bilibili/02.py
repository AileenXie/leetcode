nums = list(map(int, input().strip().split(",")))


def func(nums):
    n = len(nums)
    if not n: return 0
    dp = [0]*n
    dp[0]=nums[0]
    for i,num  in enumerate(nums[1:],1):
        dp[i]=max(dp[i-1],0)+num
    return max(dp)

print(func(nums))