# Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
#
# 1. Each row must contain the digits 1-9 without repetition.
# 2. Each column must contain the digits 1-9 without repetition.
# 3. Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# The Sudoku board could be partially filled, where empty cells are filled with the character '.'.
#
# Example 1:
#
# Input:
# [
#   ["5","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: true
# Example 2:
#
# Input:
# [
#   ["8","3",".",".","7",".",".",".","."],
#   ["6",".",".","1","9","5",".",".","."],
#   [".","9","8",".",".",".",".","6","."],
#   ["8",".",".",".","6",".",".",".","3"],
#   ["4",".",".","8",".","3",".",".","1"],
#   ["7",".",".",".","2",".",".",".","6"],
#   [".","6",".",".",".",".","2","8","."],
#   [".",".",".","4","1","9",".",".","5"],
#   [".",".",".",".","8",".",".","7","9"]
# ]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being
#     modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
# Note:
#
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# The given board contain only digits 1-9 and the character '.'.
# The given board size is always 9x9.


class Solution:
    def isValidSudoku(self, board) -> bool:
        for i in range(9):
            if not self.isNotRepeat(board[i]):  # row重复判断
                return False
            vec = []
            for j in range(9):
                vec += board[j][i]
            if not self.isNotRepeat(vec):  # col重复判断
                return False
        for i in [0, 3, 6]:
            for j in [0, 3, 6]:
                vec = board[i][j:j+3] + board[i+1][j:j+3] + board[i+2][j:j+3]  # 3x3子块数字向量化
                if not self.isNotRepeat(vec):  # 子块重复判断
                    return False
        return True


    def isNotRepeat(self, vec):
        count = 0
        for i in range(len(vec)):
            if vec[i] != ".":
                count = count + 1
        if len(set(vec)) < count + 1:  # 去重序列比未去重短 --> 有重复
            return False
        else:
            return True


if __name__ == '__main__':
    matrix = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
    # print(matrix[0][0:3])
    # print(matrix[1])
    # vec = []
    # for j in range(9):
    #     vec += matrix[j][0]
    # print(vec)

    result = Solution().isValidSudoku(matrix)
    print(result)