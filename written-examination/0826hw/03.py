"""
猜词游戏
输入单词长度和猜词次数，然后下面输入猜词的情况，
第一个是猜词内容，后面跟两个数，
第一个是位置和字符都匹配的次数，第二个是位置不对、字符匹配的次数，输入
5
5
cloxy 3 0
cxmnu 1 1
kcotd 2 1
apqud 2 0
bldwz 1 1
输出
cloud

"""

p = int(input())
t = int(input())
words = []
count = []

import collections

for _ in range(t):
    w, m, n = input().strip().split()
    words.append(w)
    count.append(int(m), int(n))


def func(p, t, words, count):
    dp = [[0 for _ in range(t)] for _ in range(26)]
    for w in words:
        for i, a in enumerate(w):
            dp[a - ord()]

