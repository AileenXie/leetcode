"""
5 6
X00100
00000X
01T000
0X1010
00000X

4
0 0 1 5
"""
def func(n,m,matrix):
    # print(matrix)
    start=[]
    end=None
    for i in range(n):
        for j in range(m):
            cur = matrix[i][j]
            if cur=="T":
                end=(i,j)
            elif cur=="X":
                start.append((i,j))
    if not end:
        return 0
    queue = [(end,0)]
    min_step=None
    min_start=[]
    while queue:
        (i,j),step=queue.pop(0)
        if i>=n or i<0 or j>=m or j<0 or matrix[i][j]=="1" or matrix[i][j]=="v":
            continue
        ori = matrix[i][j]
        matrix[i][j]="v"  # 访问过标志
        if ori=="X":
            # print(i,j,step)
            if not min_step:
                min_step=step
                min_start.append((i,j))
            else:
                if min_step==step:
                    min_start.append((i, j))
                else: break
        else:
            queue.append(((i + 1, j), step + 1))
            queue.append(((i - 1, j), step + 1))
            queue.append(((i, j + 1), step + 1))
            queue.append(((i, j - 1), step + 1))
    if not min_step:
        return 0
    min_start.sort(key=lambda x: (x[0],x[1]))
    ans = ""
    for (a,b) in min_start:
        ans+=" "+str(a)+' '+str(b)
    print(min_step)
    return ans.strip()





n,m=map(int,input().strip().split())
matrix=[]
for _ in range(n):
    row = list(input().strip())
    matrix.append(row)
print(func(n,m,matrix))