import functools

# n=int(input().strip())
# a=list(map(int,input().strip().split()))

def func(n,a):
    @functools.lru_cache(None)
    def num_split(num):
        if num<2: return False,0
        if num == 2 or num == 3: return True,1
        i = num//2
        ans = 0
        while i<num:
            z = num-i
            flag1,result1 = num_split(z)
            flag2,result2 = num_split(i)
            if flag1 and flag2:
                ans+=result1+result2
                return True, ans
            i+=1
        return True,1
    ans = 0
    for k in range(n):
        flag, count= num_split(a[k])
        ans+=count
    return ans

# n,a=3,[1, 1, 1]
n,a=3,[5, 3, 7]
# n,a=3,[500, 32, 7899]
print(func(n,a))