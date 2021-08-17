# class Solution:
#     def convert(self,s,numRows):
#         ans = ""
#         i=0
#         base = 0
#         while i<numRows:
#             ans+=s[i]
#             cur_i=i  # 当前竖列
#             j = i + 2 * numRows - 2  # 下一个竖列
#             mid = j-base  # 中间点-
#             while mid<len(s):
#                 if mid != cur_i:  # 第一次跳跃
#                     ans+=s[mid]
#                 if j<len(s) and mid!=j:  # 第二次跳跃
#                     ans+=s[j]
#                 cur_i = j
#                 j += 2 * numRows - 2
#                 mid = j-base
#             i+=1
#             base += 2
#         return ans
# # s = "LEETCODEISHIRING"
# # numRows=3
# # s = "123456789"
# # numRows=3
# s = "01234567890123"
# numRows=5
# print(Solution().convert(s,numRows))



class Solution:
    def func(self,s):
        n = len(s)
        # number = 0
        # ans = ""
        flag = False
        index = -1
        for i in range(n):
            if i>0 and s[i]=="1" and s[i]==s[i-1] and not flag:
                flag = True
                index = i-1
            # cur = int(s[i])
            # number+=cur
            # number<<1
        # print(index)
        if not flag: return s
        rest = "1"
        for j in range(index,n):
            rest += "0"
        ans =s[:(index-1)]+rest if index!=0 else rest
        return ans




# s = "101010"
# s = "10011"
# s = "1001101"
# s = "10010101"
# s = "11001101"
# s = "1101101"
print(Solution().func(s))

