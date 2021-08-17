#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/6/10 2:13 PM
# @Author : aileen
# @File : real02.py
# @Software: PyCharm

"""
项目有依赖关系，求项目执行策略下最小耗费时长
time: n个项目的各自用时
depend: m个依赖关系（A，B）B依赖于A
"""


class Solution():
    def func(self,m,n,time,depend):
        self.outn = {}
        inn = {}
        for (p,h) in depend:
            self.outn.setdefault(p,[]).append(h)  # p的被依赖项
            inn.setdefault(h,[]).append(p)  # h的依赖项

        # 最大路径和
        def dfs(task,cost):
            if task not in self.outn:  # 不被其他项目依赖
                return cost+time[task]
            cur_max = -float('inf')
            for i in self.outn[task]:  # 遍历依赖于task的项目
                path_max = dfs(i,cost+time[task])
                cur_max = max(cur_max,path_max)
            return cur_max
        ans = -float('inf')
        for task in range(n):
            if task not in inn.keys():  # 不依赖其他项目
                cur = dfs(task,0)
                print(cur)
                ans = max(ans,cur)
        return ans

if __name__ == "__main__":
    time = [2,2,4,2,3,6,1]
    depend = [(0,1),(0,2),(1,3),(2,3),(5,6),(6,4),(3,4)]
    m,n = 7,7
    print(Solution().func(m,n,time,depend))
