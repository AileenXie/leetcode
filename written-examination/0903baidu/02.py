n = int(input().strip())
A = []
for _ in range(n):
    line = list(map(int, input().strip().split()))
    A.append(line)

class Solution():
    def func(self,n, A):
        if n == 1: return 0
        self.ans = float("inf")
        visited = set()
        def dfs(i, j, count):
            if (i,j)==(n-1,n-1):
                self.ans=min(self.ans,count)
                return
            if (i,j) in visited: return
            visited.add((i,j))
            if i<n-1:
                dfs(i+1,j,count+abs(A[i+1][j]-A[i][j]))
            if i>1:
                dfs(i-1,j,count+abs(A[i-1][j]-A[i][j]))
            if j<n-1:
                dfs(i,j+1,count+abs(A[i][j+1]-A[i][j]))
            if j>1:
                dfs(i,j-1,count+abs(A[i][j-1]-A[i][j]))
            visited.remove((i,j))
        dfs(0,0,0)
        return self.ans
print(Solution().func(n,A))

