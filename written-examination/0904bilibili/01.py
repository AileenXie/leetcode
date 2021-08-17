string=input().strip()


def func(string):

    n=len(string)
    if not string or n==1: return string
    def judge(i,j):
        if i==j:  # 奇数个
            l=1
        else:  # 偶数个
            l=2
        p,q=i-1,j+1
        while p >= 0 and q < len(string):
            if string[p] == string[q]:
                l += 2
            else:
                break
            p-=1
            q+=1
        return l,p+1,q-1
    i=0
    ans,l,r = 1,0,0
    while i<n:
        length,p,q = judge(i,i)
        if length>ans:
            ans,l,r=length,p,q
        if i+1<n and string[i+1]==string[i]:
            length,p,q=judge(i,i+1)
            if length > ans:
                ans, l, r = length, p, q
        i+=1
    return string[l:r+1]

print(func(string))
