# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.
#
# Example 1:
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:
#
# Input: "cbbd"
# Output: "bb"


class Solution:
    def longestPalindrome(self, s: str) -> str:
        sub = ''
        for i in range(len(s)):
            # odd case
            tmp = self.palindrome(s, i, i)
            if len(tmp) > len(sub):
                sub = tmp
            # even case
            tmp = self.palindrome(s, i, i + 1)
            if len(tmp) > len(sub):
                sub = tmp
        return sub

    # Compare s[left] & s[right]，from the middle to the sides
    def palindrome(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1: right]


if __name__ == '__main__':
    result = Solution().longestPalindrome("abacdadcbd")
    print(result)
