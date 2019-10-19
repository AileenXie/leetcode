#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
#
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:
#
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:
#
# What should we return when needle is an empty string? This is a great question to ask during an interview.
#
# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        la = len(haystack)
        lb = len(needle)
        i, j = 0, 0
        if lb == 0:
            return 0
        match_flag = 0
        match_loc = -1
        while i < la and j < lb:
            if haystack[i] == needle[j]:
                if match_flag == 0:
                    match_loc = i
                    match_flag = 1
                i += 1
                j += 1
            else:
                if match_flag == 1:
                    match_flag = 0
                    i = match_loc+1
                    j = 0
                else:
                    i += 1
        if j < lb:  # needle还没比对完
            match_loc = -1
        return match_loc


if __name__ == '__main__':
    # result = Solution().strStr("aaabaa", "ab")
    # result = Solution().strStr("aaa", "aaaa")
    result = Solution().strStr("mississippi", "issip")
    print(result)