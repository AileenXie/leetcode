class Solution:
    def solve(self , n , a , b ):
        # write code here
        if a+b<n: return 0
        if a+b==n: return 1
        dp = [0]*n  # dp[i]表示i个盘子装a蛋糕
        for i in range(1,n):
            dp[i]=min(a//i, b//(n-i))
        return max(dp)

if __name__ == "__main__":
    print(Solution().solve(5,2,3))
    print(Solution().solve(4,7,10))