#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/7/30 9:17 PM
# @Author : aileen
# @File : 01_0-1背包问题.py
# @Software: PyCharm

class Solution:
    def solve(self, n, Edge , f ):
        # write code here
        out = {}
        for i,(a,b) in enumerate(Edge):
            # a,b = node.x, node.y
            out.setdefault(a,[]).append(b)
            out.setdefault(b,[]).append(a)
        # print(out)
        queue = [(1,f[0])]
        visited = set()
        visited.add(1)
        path_count = 0
        while queue:
            cur,count = queue.pop(0)
            # print(cur,count)
            if len(out[cur])==1 and out[cur][0] in visited:  # 叶子
                # print(count)
                if count<=2: path_count+=1
                continue
            for index in out[cur]:
                if index in visited:
                    continue
                queue.append((index,count+f[index-1]))
                visited.add(index)
        return path_count


if __name__ == "__main__":
    n,e,f=7,[(7,2),(6,1),(5,2),(1,2),(4,6),(6,3)],[0,0,1,0,1,0,0]
    print(Solution().solve(n,e,f))