#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/23 4:06 PM
# @Author : aileen
# @File : 01.py
# @Software: PyCharm


class Solution:
    def func(self,string,words):
        if not words: return string
        dic = {}
        dic_len = {}
        for word in words:
            dic.setdefault(word[0],[]).append(word)
            dic_len.setdefault(word[0],set()).add(len(word))
        ans = ""
        i=0
        while i<len(string):
            s=string[i]
            if s not in dic:
                ans+=s
            else:
                for word_len in dic_len[s]:
                    j,l=i+1,1
                    cur=s
                    while l<word_len and j<len(string):
                        if string[j]!=" ":
                            cur+=string[j]
                            l+=1
                        j+=1
                    if l<word_len:  # 长度不够
                        continue
                    if cur in dic[s]:  # 匹配
                        ans+=" "+cur+" "
                        i = j-1  # 处理下一个字符
                        break
            i+=1
        return " ".join(list(ans.split()))

print(Solution().func("可 今日小   主要  参加殿    选",["小主","殿选"]))
print(Solution().func("aa bcd edf deda",["ded"]))
print(Solution().func("娘娘 谬赞，臣妾愧 不敢 当",["愧不敢当"]))





