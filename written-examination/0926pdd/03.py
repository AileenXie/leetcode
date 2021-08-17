"""
1
5 2
2 3 1 5 4
1 2
1 3
1 4
1 5

9

______
1
5 1
2 4 5 1 3
1 2
1 3
1 5
3 4

5
"""
class Solution:
    def func(self,n,k,A,relation):
        if n==1:
            return A[0]
        dic = {}
        for a,b in relation:
            dic.setdefault(a,set()).add(b)
            dic.setdefault(b,set()).add(a)
        self.ans = -float("inf")
        def dfs(unavailable,rest,cur_value,cur_num,path):
            if cur_num==k:  # 选了k个了
                self.ans=max(self.ans,cur_value)
                # print(cur_value,path)
                return
            if not rest: return   # 选不出
            for people in rest:
                if people in unavailable:
                    continue
                else:
                    next_rest = range(people+1,n)
                    new_unavailable=unavailable.copy()
                    if people in dic:
                        for p in dic[people]:
                            new_unavailable.add(p)
                    dfs(new_unavailable,next_rest,cur_value+A[people-1],cur_num+1,path+[people])
        for p in range(1,n+1):
            unava=dic[p] if p in dic else set()
            rest=range(p+1,n+1)
            dfs(unava,rest,A[p-1],1,[p])
        return self.ans if self.ans != -float("inf") else -1




t = int(input())
for _ in range(t):
    n,k=map(int,input().strip().split())
    a=list(map(int,input().strip().split()))
    relation = []
    for i in range(n-1):
        u,v=map(int,input().strip().split())
        relation.append((u,v))
    print(Solution().func(n,k,a,relation))