# The count-and-say sequence is the sequence of integers with the first five terms as following:
#
# 1.     1
# 2.     11
# 3.     21
# 4.     1211
# 5.     111221
# 1 is read off as "one 1" or 11.
# 11 is read off as "two 1s" or 21.
# 21 is read off as "one 2, then one 1" or 1211.
#
# Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence.
#
# Note: Each term of the sequence of integers will be represented as a string.
# Example 1:
#
# Input: 1
# Output: "1"
# Example 2:
#
# Input: 4
# Output: "1211"



class Solution:

    def countAndSay(self, n: int) -> str:
        return self.countsay('1', n)

    def countsay(self, pre, n):
        if n == 1:
            return pre
        save = {}
        say = ""
        for i in range(len(pre)):
            if pre[i] not in save.keys():
                if save != {}:  # 字典只存当前数字与个数，避免之后出现的相同数字被统计在一起
                    say = say + str(save[pre[i-1]]) + pre[i-1]  # 清空之前把字典里的数字-个数记下来
                    save.clear()
                save[pre[i]] = 1
            else:
                save[pre[i]] += 1
        say = say + str(save[pre[-1]]) + pre[-1]  # 记上字典最后剩下的数字-个数
        return self.countsay(say, n - 1)


if __name__ == '__main__':
    # result = Solution().countAndSay(1)
    # result = Solution().countAndSay(5)
    result = Solution().countAndSay(30)
    print(result)