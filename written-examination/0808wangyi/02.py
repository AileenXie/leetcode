

def get_time(delay):
    time = "am"
    s = delay%60
    res = delay//60
    m = res%60
    h = res//60+8
    if h>12:
        time = "pm"
        h-=12
    return h,m,s,time


def func(n,a,b):
    if not n: return get_time(0)
    if n==1: return get_time(a[0])
    dp = [(0,0)]*n
    dp[0]=(a[0],a[0])  # 和前面一起买，自己买
    dp[1]=(b[0], min(dp[0][0],dp[0][1])+a[1])
    for i in range(2,n):
        dp[i]=(dp[i-1][1]-a[i-1]+b[i-1],min(dp[i-1][0],dp[i-1][1])+a[i])
    # print(dp)
    return get_time(min(dp[-1]))


T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    if n==1:
        a = [int(input().strip())]
        b = []
    else:
        a = list(map(int, input().strip().split()))
        b = list(map(int, input().strip().split()))
    h, m, s, time =func(n, a, b)
    # print(h,m,s,time)
    h=str(h) if h>=10 else "0"+str(h)
    m=str(m) if m>=10 else "0"+str(m)
    s=str(s) if s>=10 else "0"+str(s)
    print("{}:{}:{} {}".format(h,m,s,time))
