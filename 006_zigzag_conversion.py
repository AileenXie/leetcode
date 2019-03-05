# Time: O(n)
# Space: O(n)
#
# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows == 1:
            return s
        max_gap = 2 * numRows - 2
        out = ""
        for start in range(numRows):
            gap = max_gap - start * 2
            if gap == 0:
                gap = max_gap
            i = start
            while i < len(s):
                out = out + s[i]
                i = i + gap
                gap = max_gap - gap
                if gap == 0:
                    gap = max_gap
        return out


if __name__ == '__main__':
    result = Solution().convert("AB", 1)
    print(result)
    result = Solution().convert("PAHNAPLSIIGYIR", 4)
    print(result)
