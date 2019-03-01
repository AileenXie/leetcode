# Time: O(logn)
# Space: O(1)
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21


class Solution:
    def reverse(self, x: int) -> int:
        flag = 0
        if x < 0:
            x = abs(x)
            flag = 1

        res = 0
        while x > 0:
            tmp = x % 10
            res = res * 10 + tmp

            x = x // 10

        if flag == 1:
            res = -res

        if res > (2 ** 31 - 1) or res < -2 ** 31:
            return 0
        else:

            return res


if __name__ == '__main__':
    result = Solution().reverse(1234567890)
    print(result)