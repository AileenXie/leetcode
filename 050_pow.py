"""
Implement pow(x, n), which calculates x raised to the power n (x^n).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−2^31, 2^31 − 1]
"""

# 求幂，注意不要超出迭代次数
# 相关：029

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if not n:
            return 1
        if n < 0:
            return self.myPow(1/x, -n)
        if not n % 2:  # 能被2整除
            return self.myPow(x*x, n/2)  # 2^32 = 4^16 = 16^8 = 246^4 = ...
        else:
            return x*self.myPow(x, n-1)

if __name__ == '__main__':
    # result = Solution().myPow(2,4)
    result = Solution().myPow(1.00001,123456)
    print(result)
