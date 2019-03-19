# Time: O(n)
# Space: O(1)
#
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:
#
# Coud you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x is None:
            return True
        if x < 0:
            return False
        a = 1
        while x // a >= 10:
            a *= 10
        while x:
            l = x // a
            r = x % 10
            if l != r:
                return False
            x = (x % a) // 10
            a //= 100
        return True


if __name__ == '__main__':
    result = Solution().isPalindrome(121121)
    print(result)
