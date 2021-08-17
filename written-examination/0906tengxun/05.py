"""
有n个结点，结点间有m条单向路径，路径长度为[a1,a2,...an]
从1号点出发给位于n位置的公司送餐，每次送餐需要往返一次，
问送T次餐，最短要往返的路径总长

输入：
n m T
出发点 到达点 边长1
出发点 到达点 边长2
...
出发点 到达点 边长m


输出：
最短路径长度

例如：
输入:
5 5 3
1 2 1
2 3 1
3 5 1
5 1 1
5 4 1

输出：
12

最短往返路径：1->2->3->5->1 = 4,共3趟=12
"""

n,m,T=map(int, input().strip().split())
a = [[float("inf") for _ in range(n)]for _ in range(n)]
for i in range(n):
    a[i][i]=0  # 对角线
for j in range(m):
    x,y,d=map(int, input().strip().split())
    a[x-1][y-1]=d

def func(n,m,a):
    for ii in range(n):
        for jj in range(n):
            for kk in range(n):
                a[jj][kk]=min(a[jj][ii]+a[ii][kk],a[jj][kk])
    return a[0][-1]+a[-1][0]
print(func(n,m,a)*T)