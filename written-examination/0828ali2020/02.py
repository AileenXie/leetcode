# n = int(input().strip())
# a = input().strip()
# b = input().strip()


def func(n, a, b):
    # if a == b or a == b[::-1]: return 0
    # print(b[::-1])
    a1=a[::-1]
    tmp1,tmp2=0,0
    for i in range(n):
        if a[i]!=b[i]:
            tmp1+=1
    for i in range(n):
        if a1[i]!=b[i]:
            tmp2+=1
    ans=0
    if tmp1>tmp2:
        a=a1
        ans=1
    zero_one,one_zero=0,0
    print(a,b)
    for i in range(n):
        if a[i]!=b[i]:
            if a[i]=="0":
                zero_one+=1
            else:
                one_zero+=1
    print(zero_one,one_zero)
    ans += min(zero_one,one_zero)+abs(zero_one-one_zero)
    return ans

n,a,b=7,"1111000","0010011"
# n,a,b=3,"110","001"
print(func(n,a,b))