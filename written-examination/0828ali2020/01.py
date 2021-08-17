# n, m = map(int, input().strip().split())
class Solution:
    def func(self,n, m):
        nums = []
        while n:
            nums.append(n % 10)
            n //= 10
        print(nums)
        self.number = []

        def dfs(cur, rest):
            if not rest:
                if cur not in self.number:
                    self.number.append(cur)
            seen = set()
            for i,a in enumerate(rest):
                if a in seen: continue
                seen.add(a)
                dfs(cur*10 + a,rest[:i]+rest[i+1:])

        visited=set()
        for i,start in enumerate(nums):
            if start==0 or start in visited:continue
            visited.add(start)
            # print(nums[:i]+nums[i+1:])
            dfs(start, nums[:i]+nums[(i+1):])
        print(self.number)
        ans = 0
        for a in self.number:
            if a%m==0: ans+=1
        return ans

# n,m=322,2
# n,m=97284,4
n,m=12423546,3
n,m=1234567892,3
print(Solution().func(n,m))

