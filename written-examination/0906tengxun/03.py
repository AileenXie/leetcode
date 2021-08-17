"""
L长的巧克力棒，当长度大于D就要对巧克力棒随机截断
截断的左侧丢弃，若右侧仍然大于D，继续截断

问终止截断的平均截断次数是多少

输入：
L,D
输出：
截断次数的期望（保留4位小数）

例如：，

输入：
1 1

输出：
0
————————
输入：
2 1

输出：
1.6931

【AC:100%】
"""


import math
l, d = map(int, input().strip().split())

if l == d:
    print(0.0000)
else:
    print("{:.4f}".format(math.log(l/d,math.e)+1))
