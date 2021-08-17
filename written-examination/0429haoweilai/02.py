#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/29 6:45 PM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm

"""
十进制转换成二进制
时间限制：C/C++语言 2000MS；其他语言 4000MS
内存限制：C/C++语言 102400KB；其他语言 626688KB
题目描述：
输入一个十进制整数， 输出其二进制形式的字符串。

输入
任意输入一个正整数 int 类型，字节为4个字节。

输出
此正整数的二进制字符串，注意不要包括最左边的0，比如100的二进制形式是：000000000000000000000000‭01100100‬，代码输出时，移除左边的0，则应该输出 1100100


样例输入
100
样例输出
1100100
"""

def func(num):
    if num == 0:
        return 0
    ans = ""
    while num:
        a = num%2
        num //= 2
        ans += str(a)
    ans = list(ans)
    ans.reverse()
    ans = ''.join(ans)
    return int(ans)

m = int(input().strip())
print(func(m))
