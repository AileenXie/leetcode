"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time.

The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

"""

#  递归算法 + 记忆化搜索
#  问题等同于：计算二叉树叶子节点数
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        sum = [[None]*(n+1) for _ in range(m+1)]
        return self._uniquePaths(m, n, sum)
    def _uniquePaths(self, m, n, sum):
        if m == 1 or n == 1:
            return 1
        if sum[m][n]== None:
            sum[m][n]= self._uniquePaths(m-1,n,sum)+self._uniquePaths(m,n-1,sum)
        return sum[m][n]

if __name__ == '__main__':
    # result = Solution().uniquePaths(3,2)
    result = Solution().uniquePaths(23,12)
    print(result)
