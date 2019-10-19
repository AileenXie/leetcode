# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
#
# Return the quotient after dividing dividend by divisor.
#
# The integer division should truncate toward zero.
#
# Example 1:
#
# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:
#
# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
#
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range:
# [−231,  231 − 1]. For the purpose of this problem,
# assume that your function returns 231 − 1 when the division result overflows.



class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # C/C++中：
        # int n1 = 0x80000000  # 最大负数, -2147483648
        # int n2 = 0x7fffffff  # 最大正数, 2147483647
        # python中 print(n1,n2) 输出 2147483648，2147483647
        # 没有负号，python 存储数据是 number，对于整型，不区分 int(32bit), byte, long

        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            neg_flag = 1
        else:
            neg_flag = 0
        dividend = abs(dividend)
        divisor = abs(divisor)

        result = 0
        while dividend >= divisor:  # 没有除完重新开始
            temp, i = divisor, 1
            while dividend >= temp:  # 减去1,2,4,..2^n个temp
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1
        if neg_flag:
            result = -result

        return min(max(-2147483648, result), 2147483647)

if __name__ == '__main__':
    result = Solution().divide(-10, -3)
    # # result = Solution().divide(-2147483648, -1)
    # result = Solution().divide(-21474836600, 1)
    print(result)