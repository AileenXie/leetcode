"""
判断得分
C ——清除上一次得分
T ——本次得分为上一次得分的3倍
+ ——本次得分是前两次得分的加和
- ——本次得分是前两次得分之差的绝对值
数字——本次得分

求最终总得分

输入：
5 2 C T + -
输出：
45

【AC：100%】
"""
scores = input().strip().split()
pre = []
for i, s in enumerate(scores):
    if s == "C":
        if not pre: continue
        pre.pop()
    elif s == "T":
        if not pre: continue
        cur = pre[-1] * 3
        pre.append(cur)
    elif s == "+":
        if len(pre) >= 2:
            cur = pre[-1] + pre[-2]
        #elif len(pre)==1:
        #    cur = 2 * pre[-1]
        else: continue
        pre.append(cur)
    elif s == "-":
        if len(pre)>=2:
            cur = abs(pre[-1] - pre[-2])
        else: continue
        pre.append(cur)
    else:
        pre.append(int(s))
    print(pre)
print(sum(pre))
