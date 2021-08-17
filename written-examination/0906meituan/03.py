"""
3
1 1 3
2
1 2

"""
import collections
def func(n,a):
    if not n: return "YES"
    if n==1 and a[0]==1: return "YES"
    for i in a:
        if i==2: return "NO"
    # return "YES"
    count = collections.Counter(a)
    if 3 in count.keys():
        k = count[3]
        while k>0:
            count[1]-=2
            if count[1]<0: return "NO"
            k-=1

    if 4 in count.keys():
        k=count[4]
        while k>0:
            count[1]-=3
            if count[1]<0: return "NO"
            k-=1
    if 5 in count.keys():
        if (3 not in count or count[3]<=0) and count[1]<4: return "NO"

    return "YES"



while True:
    n=input().strip()
    if not n : break
    n=int(n)
    a=list(map(int,input().strip().split()))
    print(func(n,a))
