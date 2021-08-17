"""
2
10
0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 1 1 0 0 1 1 0 0
0 0 1 1 0 0 1 1 0 0
0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 1 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
20
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0
0 0 1 1 1 1 0 0 1 1 1 1 0 0 0 0 0 0 0 0
0 0 1 1 1 1 0 0 1 1 1 1 0 0 0 0 0 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0
0 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0



0 0 0 0 0 0 0 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 1 1 0 0 1 1 0 0
0 0 1 1 0 0 1 1 0 0
0 0 0 1 1 1 1 1 0 0
0 0 0 0 0 0 1 1 0 0
0 0 0 0 0 0 1 1 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
"""
def func(n,matrix):
    a=n//10
    top,down=None,None
    t,d=0,0
    for i in range(n):  # 统计最上方1的数量
        if top and i > top:
            break
        for j in range(n):
            if not top:
                if matrix[i][j]==1:
                    top=i
                    t+=1
            else:
                if i==top and matrix[i][j]==1:
                    t+=1

    for i in range(n-1,-1,-1):  # 统计最下方1的数量
        if down and i<top:
            break
        for j in range(n):
            if not down:
                if matrix[i][j]==1:
                    down=i
                    d+=1
            else:
                if i==down  and matrix[i][j]==1:
                    d+=1

    # print(a,top,down,t,d)
    dic = {(5,5):0,(2,2):2,(2,4):3,(5,3):5,(5,2):6,(3,3):7,(4,4):8,(2,5):9}
    cur = (t//a,d//a)
    if cur ==(2,1):
        if down-top+1==6*a:
            return 1
        if down-top+1==4*a:
            return 4
    return dic[cur]

t = int(input())
for _ in range(t):
    n=int(input())
    matrix = [[] for _ in range(n)]
    for i in range(n):
        line=list(map(int,input().strip().split()))
        for j,num in enumerate(line):
            matrix[j].append(num)
    # print(matrix)
    print(func(n,matrix))