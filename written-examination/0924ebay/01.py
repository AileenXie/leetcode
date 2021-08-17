n = int(input().strip())
import functools
class Solution:
    def jump(self,n):
        if n == 1: return 1
        self.ans = 0
        @functools.lru_cache(None)
        def dfs(cur):
            if cur == n:
                return 1
            step = 1
            count = 0
            while cur + step <= n:
                count += dfs(cur + step)
                step *= 2
            return count


        return dfs(cu)


print(Solution().jump(n))

