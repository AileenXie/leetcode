n, m = map(int, input().strip().split())
A = []
for i in range(n):
    line = list(map(int, input().strip().split()))
    A.append(line)

def func(n, m, A):
    def dfs(i,j):
        if i>=n or i<0 or j>=m or j<0:
            return 0
        if (i,j) in visited: return 0
        if A[i][j]==0: return 0
        visited.add((i,j))
        return dfs(i+1,j)+dfs(i-1,j)+dfs(i,j+1)+dfs(i,j-1)+1

    total = 0
    for i in range(n):
        for j in range(m):
            if A[i][j]==1:
                total+=1
    max_len = 0
    for i in range(n):
        for j in range(m):
            if A[i][j]==0:
                visited = set()
                A[i][j]=1
                cur = dfs(i,j)
                A[i][j]=0
                cur -= 1 if cur>total else 0
                max_len=max(max_len,cur)
    return max_len

print(func(n,m,A))