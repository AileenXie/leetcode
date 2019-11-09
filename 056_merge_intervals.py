"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
"""

#  重叠的部分合并
class Solution:
    """
    ## 方法一： 先排序， 然后根据pre[1]和cur[0]比较是否有重合来修正当前[start,end]，进行合并
    """
    # def merge(self, intervals):
    #     if intervals==[]:
    #         return []
    #     intervals = sorted(intervals, key=(lambda x: x[0]))
    #     start = intervals[0][0]
    #     end = intervals[0][1]
    #     result = []
    #     for ra in intervals:
    #         if ra[0] <= end:  # 重合
    #             if ra[1] > end:
    #                 end = ra[1]
    #         else:  # 没重合
    #             result.append([start, end])
    #             start = ra[0]
    #             end = ra[1]
    #     result.append([start, end])
    #     return result

    """
    ## 方法二： 定义指针 i 记录待合并项，与i+1进行合并
    ##         若重合 ---> 合并、i-=1  （确保前面的不受影响）
    ##         不重合 ---> 不合并，i+=1
    """
    def merge(self, intervals):
        length = len(intervals)
        if length < 2:
            return intervals
        i = 0
        while i < length - 1 and i >= 0:
            if intervals[i + 1][1] < intervals[i][0]:  # 不重合： 后一项整个在前一项前面
                intervals[i + 1], intervals[i] = intervals[i], intervals[i + 1]
                if i > 0:  # 如果是第一项，不往前移动
                    i -= 1
            elif intervals[i + 1][0] > intervals[i][1]:  # 不重合： 后一项在前一项后面
                    i += 1
            else:  # 重合情况
                intervals[i][0] = min(intervals[i + 1][0], intervals[i][0])  # 左边界
                intervals[i][1] = max(intervals[i + 1][1], intervals[i][1])  # 右边界
                del intervals[i + 1]
                length -= 1
                if i > 0:  # 如果是第一项，不往前移动
                    i -= 1
        return intervals

if __name__ == '__main__':
    # result = Solution().merge([[1,3],[2,6],[8,10],[15,18]])
    # result = Solution().merge([[1,4],[4,5]])
    # result = Solution().merge([[1,4],[0,5]])
    # result = Solution().merge([[1,4],[0,1]])
    # result = Solution().merge([[1,4],[0,1]])
    result = Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]])
    print(result)
