# Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.
#
# '?' Matches any single character.
# '*' Matches any sequence of characters (including the empty sequence).
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like ? or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "*"
# Output: true
# Explanation: '*' matches any sequence.
# Example 3:
#
# Input:
# s = "cb"
# p = "?a"
# Output: false
# Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
# Example 4:
#
# Input:
# s = "adceb"
# p = "*a*b"
# Output: true
# Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
# Example 5:
#
# Input:
# s = "acdcb"
# p = "a*c?b"
# Output: false

## 这题和 010几乎一样，010还更难一些

class Solution:

    # # ——————————————————————————————————————————————————————————
    # # 1. 基础递归算法思想(会 Time Limit)
    # # len(p) = 0 :
    # #   s 是否同为空;
    # # len(p) > 0 :
    # #   第一位是'*':(*p[0]匹配0次、多次 -->p[1:]匹配与否);
    # #   第一位不是* 即 是字母、'？'或空  -->(p[0]及p[1:]匹配与否);
    # # ——————————————————————————————————————————————————————————
    # def isMatch(self, s: str, p: str) -> bool:
    #     lp = len(p)
    #     ls = len(s)
    #     if lp == 0:
    #         return ls == 0
    #     if p[0] == '*':
    #         # * 匹配0次 or 匹配1到多次
    #         return self.isMatch(s, p[1:]) or (ls > 0 and self.isMatch(s[1:], p))
    #     # lp=1 或 lp>1但后一位不是*
    #     else:
    #         return ls > 0 and (s[0] == p[0] or p[0] == '?') and self.isMatch(s[1:], p[1:])


    # ——————————————————————————————————————————————————————————
    # 2. 递归算法 + 记忆化搜索
    # mem是记忆化搜索
    # ——————————————————————————————————————————————————————————
    def isMatch(self, s: str, p: str) -> bool:
        lp = len(p)
        ls = len(s)
        mem = [[None]*(lp+1) for _ in range(ls+1)]
        return self._isMatch(s,p,mem)

    def _isMatch(self,s,p,mem):
        lp = len(p)
        ls = len(s)

        if lp == 0:
            return ls == 0
        if mem[ls][lp] != None:
            return mem[ls][lp]

        if lp > 0 and p[0] == '*':
            # * 匹配0次 or 匹配1到多次
            mem[ls][lp] = self._isMatch(s, p[1:],mem) or (ls > 0 and self._isMatch(s[1:], p,mem))
            return mem[ls][lp]
        # lp=1 或 lp>1但后一位不是*
        else:
            mem[ls][lp] = ls > 0 and (s[0] == p[0] or p[0] == '?') and self._isMatch(s[1:], p[1:], mem)
            return mem[ls][lp]


if __name__ == '__main__':
    # result = Solution().isMatch("acdcb", "a*c?b")  # False
    result = Solution().isMatch("adceb", "*a*b")  # True
    print(result)
