#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/8/1 9:41 PM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm

#
# playfair加密算法
# @param key string字符串 密钥
# @param str string字符串 明文
# @return string字符串
#
class Solution:
    def Encode(self, key, str):
        # write code here
        code = [[None for _ in range(5)] for _ in range(5)]
        cchar = list(range(ord('a'), ord('z') + 1))  # 备选字母号
        cchar.remove(ord('j'))
        kkey = []  # 去重之后的秘钥
        dic = {}
        for k in key:
            if k == "j": k = "i"
            if k not in kkey:
                kkey.append(k)
                cchar.remove(ord(k))
        # 绘制密码表
        for i in range(5):
            for j in range(5):
                if kkey:
                    code[i][j] = kkey[0]
                    kkey.pop(0)
                else:
                    code[i][j] = chr(cchar[0])
                    cchar.pop(0)
                dic[code[i][j]] = (i, j)
        print(code)
        pair = []
        ans = ""
        p = 0
        while p + 1 < len(str):
            a = str[p] if str[p] != "j" else "i"
            b = str[p + 1] if str[p + 1] != "j" else "i"
            pair.append((dic[a], dic[b]))
            p += 2
        tail = str[-1] if p < len(str) else ""

        print(pair,tail)

        for (i, j), (p, q) in pair:
            if i == p and j == q:
                ans += code[i][j] + code[p][q]
                continue
            elif i == p:  # 同行
                x1, x2 = i, p
                y1 = j + 1 if j + 1 < 5 else 0
                y2 = q + 1 if q + 1 < 5 else 0
            elif j == q:  # 同列
                y1, y2 = j, q
                x1 = i + 1 if i + 1 < 5 else 0
                x2 = p + 1 if p + 1 < 5 else 0
            else:
                x1, y1 = i, q
                x2, y2 = p, j
            ans += code[x1][y1] + code[x2][y2]
        return ans + tail

key,str="nowcoder","iloveyou"
print(Solution().Encode(key,str))