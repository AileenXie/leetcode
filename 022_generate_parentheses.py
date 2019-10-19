# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
#
# For example, given n = 3, a solution set is:
#
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]


class Solution:
    def generateParenthesis(self, n: int):
        if n == 0:
            return [""]
        if n == 1:
            return ["()"]
        List = []
        item = "("  # 第一个和最后一个是确定的
        num_left = n-1
        num_right = n-1
        self.addParentresisLeft(item, num_left, num_right, List)
        self.addParentresisRight(item, num_left, num_right, List)
        for i in range(len(List)):
            List[i] += ")"  # 第一个和最后一个是确定的
        return List

    def addParentresisLeft(self, item, num_left, num_right, List):
        item_new = item + "("
        num_left -= 1
        if num_left == 0 and num_right == 0:
            List.append(item_new)
        elif num_left == 0:
            self.addParentresisRight(item_new, num_left, num_right, List)
        elif num_right == 0:
            self.addParentresisLeft(item_new, num_left, num_right, List)
        else:
            self.addParentresisLeft(item_new, num_left, num_right, List)
            self.addParentresisRight(item_new, num_left, num_right, List)


    def addParentresisRight(self, item, num_left, num_right, List):
        item_new = item + ")"
        num_right -= 1
        if num_left == 0 and num_right == 0:
            List.append(item_new)
        elif num_left == 0:
            self.addParentresisRight(item_new, num_left, num_right, List)
        elif num_right == 0 or num_left - num_right >=1:  # 剩余的左括号不能比右括号多2个，如"())(()"
            self.addParentresisLeft(item_new, num_left, num_right, List)
        else:
            self.addParentresisLeft(item_new, num_left, num_right, List)
            self.addParentresisRight(item_new, num_left, num_right, List)


# # 简化写法：
# class Solution(object):
#     def generateParenthesis(self, N):
#         ans = []
#         def backtrack(S = '', left = 0, right = 0):
#             if len(S) == 2 * N:
#                 ans.append(S)
#                 return
#             if left < N:
#                 backtrack(S+'(', left+1, right)  # 确保第一个是左括号
#             if right < left:
#                 backtrack(S+')', left, right+1)  # 确保最后一个是右括号
#
#         backtrack()
#         return ans

if __name__ == '__main__':
    result = Solution().generateParenthesis(4)
    print(result)