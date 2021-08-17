# Time: -
# Space: -

# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
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
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".
# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

class Solution:
    # # ——————————————————————————————————————————————————————————
    # # 1. 基础递归算法思想（会超时）
    # # len(p) = 0 :
    # #   s 是否同为空;
    # # len(p) > 0 :
    # #   '*'不可能出现在第一位：
    # #        第二位是'*':(*p[0]匹配0次、多次且p[2:]匹配与否);
    # #        第二位不是* 即 是字母、'.'或空:(p[0]及p[1:]匹配与否);
    # # ——————————————————————————————————————————————————————————
    # def isMatch(self, s: str, p: str) -> bool:
    #     lp = len(p)
    #     ls = len(s)
    #     if lp == 0:
    #         return ls == 0
    #     if lp > 1 and p[1] == '*':
    #         # * 匹配0次 or 匹配1到多次
    #         return self.isMatch(s, p[2:]) or (ls > 0 and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p))
    #     # lp=1 或 lp>1但后一位不是*
    #     else:
    #         return ls > 0 and (s[0] == p[0] or p[0] == '.') and self.isMatch(s[1:], p[1:])

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

        if lp > 1 and p[1] == '*':
            # * 匹配0次 or 匹配1到多次
            mem[ls][lp] = self._isMatch(s, p[2:],mem) or (ls > 0 and (s[0] == p[0] or p[0] == '.') and self._isMatch(s[1:], p,mem))
            return mem[ls][lp]
        # lp=1 或 lp>1但后一位不是*
        else:
            mem[ls][lp] = ls > 0 and (s[0] == p[0] or p[0] == '.') and self._isMatch(s[1:], p[1:],mem)
            return mem[ls][lp]

    # # ——————————————————————————————————————————————————————————
    # # 3. 动态规划DP
    # # 从后往前, f(i,j)表示输入s[:i]和p[:j]时的匹配结果:
    # # f(i,j)=f(i-1,j-1)                                   if s[i-1]==p[j-1] || p[j-1]=='.'
    # # f(i,j)=f(i,j-2)                                     if p[j-1]=='*' （匹配0次）
    # # f(i,j)=f(i-1,j) and s[i-1]==p[j-2]||p[j-2]=='.'     if p[j-1]=='*' （匹配多次）
    # # ——————————————————————————————————————————————————————————
    # def isMatch(self, s, p):
    #     s_len, p_len = len(s), len(p)
    #     mem = [[False] * (p_len + 1) for _ in range(s_len + 1)]
    #     mem[0][0] = True
    #     for i in range(s_len + 1):
    #         for j in range(1, p_len + 1):
    #             if p[j - 1] == '*':
    #                 mem[i][j] = j > 1 and mem[i][j - 2] or \
    #                             (i > 0 and (s[i - 1] == p[j - 2] or j > 1 and p[j - 2] == ".")
    #                              and i > 0 and mem[i - 1][j])
    #             else:
    #                 mem[i][j] = i > 0 and mem[i - 1][j - 1] and ((i > 0 and s[i - 1] == p[j - 1]) or p[j - 1] == ".")
    #
    #     return mem[-1][-1]


if __name__ == '__main__':
    # result = Solution().isMatch("mississippi", "mis*is*p*.")
    result = Solution().isMatch("aaa", "aa*")

    print(result)
