#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/3/31 9:50 AM
# @Author : aileen
# @File : my_sort.py
# @Software: PyCharm
"""
排序汇总

"""
import time
import random

class Solution():

    def bubble_sort(self, lst):
        """
        【交换 - 冒泡排序】：
        时间复杂度：平均 O(n^2),  最坏（本身逆序）O(n^2)，最好（本身有序）O(n)
        空间复杂度：O(1)，就地排序
        """
        n = len(lst)
        if n<= 1:
            return lst
        move_flag = False  # 发现本轮未发生移动，即可停止排序
        for i in range(n):
            for j in range(n-i-1):
                if lst[j] > lst[j+1]:
                    lst[j], lst[j+1] = lst[j+1], lst[j]
                    move_flag = True
            if not move_flag:
                break
        return lst

    def quick_sort(self, lst):
        """
        【交换 - 快速排序】
        时间复杂度：平均 O(nlogn),  最坏（本身有序，单支树）O(n^2)，最好（基准点在中间，左右子树差不多）O(nlogn)
        空间复杂度：O(h)，其中 h 为快速排序递归调用的层数。
        说明：我们需要额外的 O(h) 的递归调用的栈空间，由于划分的结果不同导致了快速排序递归调用的层数也会不同，
             最坏情况下需O(n) 的空间，最优情况下每次都平衡，此时整个递归树高度为 nlogn，空间复杂度为O(logn)。
        """
        def patition(lst, left, right):
            pivot = left
            # pivot = random.randint(left,right)
            while left < right:
                while left < right and lst[right] >= lst[pivot]:  # 从右向左找到比基准值小的位置
                    right -= 1
                while left < right and lst[left] <= lst[pivot]:  # 从左向右找到比基准值大的位置
                    left += 1
                lst[left], lst[right] = lst[right], lst[left]  # 交换位置，保证left及左边的都比基准小，right及右边都大

            lst[left], lst[pivot] = lst[pivot], lst[left]  # 保证基准值（此时在Left位置）左边的都比基准小，右边都比基准值大大
            return left

        def quicksort(lst, left, right):
            if left >= right:
                return
            mid = patition(lst, left, right)  # mid位置已到达最终位置！现在分治左右两个片区

            quicksort(lst, left, mid-1)
            quicksort(lst, mid+1, right)

        n = len(lst)
        if n <= 1:
            return lst
        quicksort(lst, 0, n-1)
        return lst

    # 堆排序的应用：TopK算法，只用O(nlogk)，比先排序再选topk更快，因为堆排序只用排k个元素的序，剩下的不用管
    # 如：找【第k大】的元素——构建【小顶堆】，新的元素和堆顶元素比，比堆顶大的进入堆置换堆顶。遍历完后堆里就是前k个大的元素，堆顶就是第k大。
    #    找【第k小】的元素——构建【大顶堆】，。。。。。。。。。。。。。。小。。。。。。
    def heap_sort(self, nums):
        """
        【选择-堆排序】
        通过构建大顶堆，进行升序排序（每次堆顶位置最大值放到最后，达到最终位置）
        + 时间复杂度：平均、最好、最坏都是O(nlogn)， 包括两个方面：
            1. 初始化建堆过程时间：O(n)
            2. 更改堆元素后重建堆时间：O(nlogn)：循环 n -1 次，每次都是从根节点往下循环查找，所以每一次时间是 logn，
                                             共(n-1)logn ，所以复杂度是 O(nlogn)
        + 空间复杂度O(1)： 因为堆排序是就地排序
        """
        i, l = 0, len(nums)
        self.nums = nums
        # 构造大顶堆，从非叶子节点开始倒序遍历，因此是l//2 -1 就是最后一个非叶子节点
        for i in range(l // 2 - 1, -1, -1):
            self.build_heap(i, l - 1)
        # print(nums)
        # 上面的循环完成了大顶堆的构造，那么就开始把根节点跟末尾节点交换(当前堆顶元素到达最终位置)，然后重新调整大顶堆
        for j in range(l - 1, -1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.build_heap(0, j - 1)
        return nums

    def build_heap(self, i, l):
        """ 构建大顶堆"""
        nums = self.nums
        left, right = 2 * i + 1, 2 * i + 2  # 左右子节点的下标
        large_index = i
        if left <= l and nums[i] < nums[left]:
            large_index = left

        if right <= l and nums[large_index] < nums[right]:
            large_index = right
        # 通过上面跟左右节点比较后，得出三个元素之间较大的下标，如果较大下表不是父节点的下标，说明交换后需要重新调整大顶堆
        if large_index != i:
            nums[i], nums[large_index] = nums[large_index], nums[i]
            self.build_heap(large_index, l)


if __name__ == "__main__":
    # lst = [2,-1,0]
    # lst = [2,4,14,5,3,1,7,9,10,22,31,11]
    lst = [1,2,3,4,5,6,7,9,10,15,16,22,31]
    # lst.reverse()
    solution = Solution()
    start = time.time()
    print(solution.bubble_sort(lst.copy()))  # 就地排序
    print(time.time()-start)

    start = time.time()
    print(solution.quick_sort(lst.copy()))
    print(time.time()-start)

    start = time.time()
    print(solution.heap_sort(lst.copy()))  # 就地排序
    print(time.time()-start)

