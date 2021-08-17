n = int(input().strip())

import copy
def fill_matrix(flag, m, a, b):
    sub_matrix = [[0 for _ in range(m)] for _ in range(m)]
    if flag:  # 1-\ 0-/
        for i in range(m):
            for j in range(m):
                if i>j:
                    sub_matrix[i][j]=a
                elif i<j:
                    sub_matrix[i][j]=b
    else:
        base = m-1
        for i in range(m):
            for j in range(m):
                if i+j<base:
                    sub_matrix[i][j] = a
                elif i+j>base:
                    sub_matrix[i][j] = b
    return sub_matrix


matrix = [[0 for _ in range(n)] for _ in range(n)]
mid=n//2  # 子矩阵边长
sub1=fill_matrix(1,mid,3,2)
sub2=fill_matrix(0,mid,4,5)
sub3=fill_matrix(1,mid,6,7)
sub4=fill_matrix(0,mid,1,8)
# matrix[0:mid][0:mid]=copy.deepcopy(sub1)
# matrix[mid:n][0:mid]=copy.deepcopy(sub2)
# matrix[mid:n][mid:n]=fill_matrix(1,mid,6,7)
# matrix[0:mid][mid:n]=fill_matrix(0,mid,1,8)
if n%2:  # 奇数
    for i in range(n):
        if i<mid:
            matrix[i]=sub1[i]+[0]+sub4[i]
        elif i>mid:
            j=i-mid-1
            matrix[i]=sub2[j]+[0]+sub3[j]
else:
    for i in range(n):
        if i<mid:
            matrix[i]=sub1[i]+sub4[i]
        elif i>=mid:
            j=i-mid
            matrix[i]=sub2[j]+sub3[j]
for i in range(n):
    ans = ""
    for a in matrix[i]:
        ans += str(a) +" "
    print(ans.strip())