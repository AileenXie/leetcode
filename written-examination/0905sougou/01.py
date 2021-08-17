"""
abc一套兑换一个玩具
支持二换一指定票券

最多能兑换几个玩具


设a为最小值，b为中间值，c为最大值。k为最终的分配结果。
"""


class Solution:
    def numberofprize(self, a, b, c):
        # write code here
        m=min(a,b,c)
        [a,b,c]=sorted([a-m, b-m, c-m])  # a必定为0
        # 假设最终能组成k个，假设由b,c剩余票共同兑换a
        k=(b+c)//4  # (b+c-2k)/2≥k
        if b>=k:
            return m+k  # b的票够，符合假设
        else:
            return m+(b+c)//5  # b的票不够，由兑换a,b： (c-k)/2≥(k-b)+k


a,b,c=4,4,2
a,b,c=9,3,3
a,b,c=6,4,2
a,b,c=100000,4,2

print(Solution().numberofprize(a,b,c))