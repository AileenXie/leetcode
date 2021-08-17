"""
计算arr的最佳切分点，使得两端数组的方差和最小

输入：
1 1 1 3 3 3

输出
3
"""

class Solution:
    """
    直接套方差定义式。Var(X)=E[(X-E(X))^2]
    """
    def find_best_cut1(self, arr ):
        # write code here
        n = len(arr)
        ans = float("inf")
        result = None
        for i in range(1,n):
            print(arr[:i],arr[i:])
            mean_a=sum(arr[:i])/i
            mean_b=sum(arr[i:])/(n-i)
            a=sum([(k-mean_a)**2 for k in arr[:i]])
            b=sum([(k-mean_b)**2 for k in arr[i:]])
            cur = a+b
            print(i,cur)
            if cur<ans:
                result=i
                ans = cur
        return result
    """
    Var(X)=E(X^2)-(E(X))2
    """
    def find_best_cut2(self, arr):
        # write code here
        n = len(arr)
        prex_2=[0]*n
        prex_sum=[0]*n
        prex_2[0]=arr[0]**2
        prex_sum[0]=arr[0]
        ans = float("inf")
        result=None
        for i in range(1,n):
            prex_2[i]=prex_2[i-1]+arr[i]**2
            prex_sum[i]=prex_sum[i-1]+arr[i]
        for i in range(1,n):
            aa=prex_2[i-1]/i
            a=(prex_sum[i-1]/i)**2
            bb=(prex_2[-1]-prex_2[i-1])/(n-i)
            b=((prex_sum[-1]-prex_sum[i-1])/(n-i))**2
            cur = aa-a+bb-b
            print(i, cur)
            if cur < ans:
                result=i
                ans=cur
        return result

arr = [1,1,1,1,1,1,3,3]
arr = [1,1,1,3,3,3]
print(Solution().find_best_cut1(arr))
print(Solution().find_best_cut2(arr))