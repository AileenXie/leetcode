# Time: O(m), m is the shortest length of string in array
# Space: O(l), l is the length of array

# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.




class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]
        sub = []
        for x in zip(*strs):
            if len(set(x)) == 1:
                sub.append(x[0])
            else:
                break
        return "".join(sub)


if __name__ == '__main__':
    result = Solution().longestCommonPrefix(["abs", "abf", "ab"])
    print(result)
