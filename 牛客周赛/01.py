#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/9 9:05 PM
# @Author : aileen
# @File : 01.py
# @Software: PyCharm

# class Solution:
#     def change(self, s):
#         # write code here
#         count = 0
#         i=0
#         ans = ""
#         while i<len(s):
#             if s[i]=="a":
#                 count+=1
#             else:
#                 ans+=s[i]
#             i+=1
#         return ans+"a"*count


class Solution:
    def solve1(self, n, m):
        # write code here
        # @functools.lru_cache(maxsize=1000)
        self.visited=set()
        if m==n: return 0
        queue = [(n,0)]
        while queue:
            x, step = queue[0]
            queue.pop(0)
            if x == m: return step  # 第一次到就是最小步数
            if x in self.visited or abs(x-m)>abs(n-m): continue  # 比不走还离得更远了
            if x < m:
                queue.append((x+1,step+1))
                queue.append((x*x,step+1))
            if x > 1:
                queue.append((x-1,step+1))
            self.visited.add(x)

    def solve2(self , n , m ):
        # write code here
        dis=[-1 for i in range(2000)]
        dis[n]=0
        q=[n]
        while q :
            e=q[0]
            q.pop(0)
            if(e==m):
                return dis[m]
            if(e<m and dis[e+1]==-1) :
                dis[e+1]=dis[e]+1
                q.append(e+1)
            if(e>1 and dis[e-1]==-1):
                dis[e-1]=dis[e]+1
                q.append(e-1)
            if e<m and e*e<m+m-n and dis[e*e]==-1 :
                dis[e*e]=dis[e]+1
                q.append(e*e)


if __name__=="__main__":
    # print(Solution().change("abcavvsssdfase"))
    print(Solution().solve1(12,1))
    print(Solution().solve2(12,1))


