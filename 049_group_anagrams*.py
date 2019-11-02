"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

## 开始试了： 1. 直接两词set后的长度，来比较它们组成是否一样，但是对'aad','add'这种无法判断
#  2. 又尝试字母转成数字，set长度和数字求和都一样则判断组成一样，但发现字母转数字后，还需要转回字母太麻烦
#  3. 改试了直接sorted(item)==sorted(cmp)来比较，可行 但Time Limit了
#  4. 最终参考别人的算法，是直接用字典，排序的字母组成作为key，巧用dir.get()查找方法

class Solution:

    def groupAnagrams(self, strs):
        d = {}
        for w in strs:
            key = tuple(sorted(w))
            d[key] = d.get(key, []) + [w]
        return list(d.values())


    #   #   Time Limit
    # def groupAnagrams(self, strs):
    #     if len(strs) < 2:
    #         return [strs]
    #     re = []
    #     for item in strs:
    #         match_flag = 0
    #         for i in range(len(re)):
    #             cmp = re[i][0]
    #             if sorted(cmp)==sorted(item):
    #                 re[i].append(item)
    #                 match_flag = 1
    #                 break
    #         if not match_flag:
    #             re.append([item])
    #     return re


if __name__ == '__main__':
    # result = Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    # result = Solution().groupAnagrams(["eat", "tea", "", "ate", "", "bat"])
    # result = Solution().groupAnagrams(["tea","and","ace","ad","eat","dans"])
    result = Solution().groupAnagrams(["paw","dad","bog","day","day","mig","len","rat"])
    print(result)
