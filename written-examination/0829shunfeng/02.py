# n, k = map(int, input().strip().split())
# a = list(map(int, input().strip().split()))


def func(n, k, a):
    # if k==n:
    #     print(max(a),1)
    #     return
    max_len = n - k + 1
    l, r = 0, max_len
    ll,rr=l,r
    max_value = sum(a[l:r]) ** 2
    l+=1
    r+=1
    while r <= n:
        if a[r - 1] > a[l-1]:
            cur_value = sum(a[l:r]) ** 2
            if cur_value>max_value:
                max_value=cur_value
                ll,rr=l,r
        l += 1
        r += 1
    # if a[ll]!=0 and a[rr]!=0:
    #     print(max_value,rr-ll)
    # else:
    while ll<rr and a[ll]==0:
        ll+=1
    while ll<rr and a[rr-1]==0:
        rr-=1
    print(max_value,rr-ll)

n,k,a=5,5,[0,0,10,0,10]
func(n,k,a)