# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


#  本题注意点：list传的是地址，同增同减，也不需要return
#  不想更改原本list值的时候，要copy()一份
class Solution:

    def permute(self, nums):
        cur_list = []
        result = []
        self.sub_permute(nums, cur_list, result)
        return result


    def sub_permute(self, nums, list, result):
        if nums==[]:
            result.append(list)
        for item in nums:
            cur_list = list.copy()
            cur_list.append(item)
            next_nums = nums.copy()
            next_nums.remove(item)
            next_cul_list = cur_list.copy()
            self.sub_permute(next_nums, next_cul_list, result)


if __name__ == '__main__':
    result = Solution().permute([1,2,3])  # 6种
    print(result)
