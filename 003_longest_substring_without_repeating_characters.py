# Time: O(n)
# Space: O(1)
#
# Given a string, find the length of the longest substring without repeating characters.
#
# Example 1:
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        bak = ''
        start = 0
        end = 0
        max_len = 0
        for cur in s:
            if max_len == 0:
                bak = bak+cur
                max_len = 1

            else:
                for i in range(start, end+1):
                    if cur == bak[i]:
                        start = i+1
                        break
                bak = bak + cur
                end = end + 1
                len = end - start+1
                if len > max_len:
                    max_len = len
        return max_len


if __name__ == '__main__':
    result = Solution().lengthOfLongestSubstring('asderababcba')
    print(result)
