n,m=map(int,input().strip().split())
C = []
V = []
for i in range(n):
    c,v=map(int,input().strip().split())
    C.append(c)
    V.append(v)
def func(n,m,C,V):
    new_C = []
    new_V = []
    neg_C = []
    neg_V = []
    neg = 0
    for i in range(n):
        if C[i]<0:
            neg+=1
            neg_C.append(C[i])
            neg_V.append(V[i])
        else:
            new_C.append(C[i])
            new_V.append(V[i])
    new_C+=neg_C
    new_V+=neg_V
    print(new_C,new_V)
    dp = [[-float('inf') for _ in range(m-sum(neg_C))]for _ in range(n)]
    dp[0][new_C[0]]=new_V[0]*(m-new_C[0])
    for i in range(1,n-neg):  # 遍历正空间物品
        for j in range(m):
            dp[i][j]=dp[i-1][j]
            if j>new_C[i]:
                dp[i][j]=max(dp[i][j],dp[i-1][j-new_C[i]]+new_V[i])
    print(dp[n-neg-1])


func(n,m,C,V)

