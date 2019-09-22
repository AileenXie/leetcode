# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
#
#
#
# Example:
#
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
# Note:
#
# Although the above answer is in lexicographical order, your answer could be in any order you want.


class Solution:
    # ——————————————————————————————————————————————————————————
    # 思路： 建立字典，回溯法
    # 建立树结构，递归求解
    #             '2'
    #        /     |     \
    #       a      b      c
    #     / | \  / | \  / | \
    #    d  e  f d e f d  e  f   '3'
    # ——————————————————————————————————————————————————————————
    def letterCombinations(self, digits: str):
        dir = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        result = []

        def letter(cur, res):
            if len(res) == 0:
                result.append(cur)
            else:
                for d in dir[res[0]]:
                    letter(cur + d, res[1:])

        if digits:
            letter("", digits)
        return result


if __name__ == '__main__':
    result = Solution().letterCombinations('23')
    print(result)