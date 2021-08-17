"""
房子的建法
"""
class Solution:
    def getHouses(self , t , xa ):
        # write code here
        center = [(xa[i],xa[i]-xa[i+1]/2,xa[i]+xa[i+1]/2) for i in range(0,len(xa),2)]
        center.sort(key=lambda x: x[0])
        n=len(center)
        if not n: return 1
        if n==1: return 2
        _,_,pre_r=center[0]
        ans = 2
        for i in range(1,n):
            c, l, r=center[i]
            if l-pre_r>t:
                ans+=2
            elif l-pre_r==t:
                ans+=1
            pre_r=r
        return ans

t,xa = 2,[-1,4,5,2,7,2]
print(Solution().getHouses(t,xa))
