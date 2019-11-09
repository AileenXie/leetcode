"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:

Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""

# 顺时针从外到里输出序列
# 00 01 02 - 12 22 - 21 20 - 10 - 11

class Solution:
    """
    方法一： 硬写，设置横竖flag、方向flag、边界值
    """
    # def spiralOrder(self, matrix):
    #     i_length = len(matrix)
    #     if not i_length:
    #         return []
    #     j_length = len(matrix[0])
    #     i = j = 0
    #     flag = 1  # 1-j, 0-i
    #     i_flag = 0  # 1-up, 0-down
    #     j_flag = 0  # 1-left, 0-right
    #     output = []
    #     max_i = i_length
    #     min_i = -1
    #     max_j = j_length
    #     min_j = -1
    #     while len(output) < i_length*j_length:
    #         if flag:  # 横向移动
    #             if not j_flag:  # 向右
    #                 while j < max_j:
    #                     output.append(matrix[i][j])
    #                     j += 1
    #                 j -= 1
    #                 max_j -= 1
    #                 i += 1
    #                 flag = 0  # 竖向移动
    #                 i_flag = 0  # down
    #             else:
    #                 while j > min_j:
    #                     output.append(matrix[i][j])
    #                     j -= 1
    #                 j += 1
    #                 min_j += 1
    #                 i -= 1
    #                 flag = 0  # 竖向移动
    #                 i_flag = 1  # up
    #         else:  # 竖向移动
    #             if not i_flag:  # 向下
    #                 while i < max_i:
    #                     output.append(matrix[i][j])
    #                     i += 1
    #                 i -= 1
    #                 max_i -= 1
    #                 min_i += 1
    #                 j -= 1
    #                 flag = 1  # 横向移动
    #                 j_flag = 1  # left
    #             else:
    #                 while i > min_i:
    #                     output.append(matrix[i][j])
    #                     i -= 1
    #                 i += 1
    #                 j += 1
    #                 flag = 1  # 横向移动
    #                 j_flag = 0  # right
    #     return output
    """
    方法二： 如048，先取第一行，对剩余矩阵做逆时针选择，重复直至矩阵为空
    """
    def spiralOrder(self, matrix):
        i = len(matrix)
        result = []
        if i < 1:
            return result

        while i > 0:
            result.extend(matrix[0])
            del matrix[0]
            matrix = self.reverseMatrix(matrix)

            i = len(matrix)

        return result

    def reverseMatrix(self, matrix):  # 逆时针旋转
        matrix[:] = map(list, zip(*matrix))  # 转置
        type = "ni"
        if type == "ni":  # 逆时针
            matrix[:] = matrix[::-1]  # 第一个冒号表示起始位置，第二个结束位置，第三项为步长，-1表示逆序。等于每列逆序
        else:
            for i in matrix:
                # matrix[i] = matrix[i].reverse()  # 等同
                matrix[i] = matrix[i][::-1]  # 每行逆序
        return matrix



if __name__ == '__main__':
#     matrix = [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
    matrix = [
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
    result = Solution().spiralOrder(matrix)
    print(result)
