class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = nums1, nums2
        cur1, cur2 = 0, 0
        res = []
        while cur1 < len(a) and cur2 < len(b):
            if a[cur1] <= b[cur2]:
                res.append(a[cur1])
                cur1 += 1
            else:
                res.append(b[cur2])
                cur2 += 1
        while cur1 < len(a):
            res.append(a[cur1])
            cur1 += 1
        while cur2 < len(b):
            res.append(b[cur2])
            cur2 += 1

        n, s = len(res) // 2, len(res) % 2
        if s:
            median = res[n]
        else:
            median = (res[n-1] + res[n]) / 2
        return median


if __name__ == '__main__':
    result = Solution().findMedianSortedArrays([1,5,8], [7])
    print(result)
