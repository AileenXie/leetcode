"""
最少放几颗球能让N个盒子里球数目不重复
输入：
N:盒子数
A:各盒子本来有多少球
4
1 3 1 4
输出：
1

输入：
5
3 3 4 4 5
输出：
6

75%
"""

n = int(input().strip())
A = list(map(int, input().strip().split()))

def func(n,A):
    if n == 1:
        return 0
    dic = {}
    for a in A:
        dic.setdefault(a,0)
        dic[a]+=1
    exist = list(dic.keys())
    exist.sort()
    count = 0
    for i,key in enumerate(exist):
        if dic[key]==1:
            continue
        cur_count = dic[key] - 1
        if i==len(exist)-1:  # 最后一个
            count += cur_count*(cur_count+1)//2
            continue
        count += cur_count
        if key+1 in dic.keys():
            dic[key+1]+=cur_count
    return count

print(func(n,A))

