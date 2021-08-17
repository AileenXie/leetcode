"""
异或求模式子计算
"""
n=int(input().strip())
a=list(map(int,input().strip().split()))

def func(n,a):
    part_a=a[0]
    for ai in a[1:]:
        part_a^=ai
    part_b = 0
    for i in range(1,n):
        # 本次i异或n-i次
        if(n-i)%2: # 奇数次异或后等于i
            part_b^=i
        else:  # 偶数次异或后等于0
            part_b^=0
    part_c = 0
    for i in range(1,n+1):
        cur = 0
        for j in range(1,(i+1)//2):
            cur^=i%j
        part_c^=cur
    return part_a^part_b^part_c
    part_d = 0
    mid =(n+1)//2
    prex = [0]*(mid+1)
    for i in range(2,mid+1):
        prex[i]=prex[i-1]^(i-1)
    for i in range(n):
        part_d^=prex[i]

print(func(n,a))