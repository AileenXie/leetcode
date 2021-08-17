#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/4/25 9:51 AM
# @Author : aileen
# @File : 02完全背包问题.py
# @Software: PyCharm

"""
小Q今天在上厕所时想到了这个问题：有n个数，两两组成二元组，相差最小的有多少对呢？相差最大呢？


输入描述:

 输入包含多组测试数据。

 对于每组测试数据：

 N - 本组测试数据有n个数

 a1,a2...an - 需要计算的数据

 保证:

 1<=N<=100000,0<=ai<=INT_MAX.



输出描述:

对于每组数据，输出两个数，第一个数表示差最小的对数，第二个数表示差最大的对数。


输入例子1:
6
45 12 45 32 5 6

输出例子1:
1 2

例子2：
247
19933 19933 19933 19933 11771 2289 17937 9434 1394 28284 19930 28546 23988 8782 19678 12869 10299 4997 27414 21834 19559 27795 18295 24767 17021 21047 2842 21357 24559 3756 14235 18319 14558 32032 13503 23012 15069 18791 24921 1795 25848 22513 11118 29423 16629 27129 29591 20203 473 20992 16295 20879 27566 19578 142 29980 26756 20679 28541 28685 28342 28260 17995 7150 7278 2659 22296 15985 11371 4376 18224 26815 10242 28694 28977 24844 31331 27738 12913 19054 18718 10437 10138 32495 13798 28880 7319 20449 28052 7035 13236 8305 10351 6790 2048 3711 32682 2532 20214 7597 15406 21357 15709 6326 666 15059 13165 7426 136 26071 29747 1143 32531 13500 27703 8593 32406 32508 19291 437 16309 2107 30214 10690 23970 16761 4482 234 23961 10891 12195 24000 22445 26572 23978 27025 7367 24592 6760 19960 32236 30425 30631 24749 6334 14030 27333 16798 19782 104 4258 8001 16624 4335 26813 5416 4823 30117 19353 22742 9539 16193 8294 10449 8304 2462 5597 12792 4754 11189 25196 24343 20757 9161 20371 18105 32553 5089 5262 11069 23934 25211 17460 16684 18252 21375 21023 12234 151 11634 29453 32747 14769 16108 23686 27912 27648 22604 10175 19602 29697 3498 23487 32646 3213 21773 25280 8770 3932 21726 28376 28311 7879 30365 4568 1055 7378 4563 3189 2769 4969 17224 6309 25554 29162 17525 13132 23694 17380 22332 10520 6152 17695 6615 27305 8814 30428 22287 27638 25329 6749 9902 4844 24532 13480 29238 31064

输出：
7 1
"""
import sys



def func(nums):
    n = len(nums)
    if n < 2:
        print("0 0")
        return
    nums = sorted(nums)
    print(len(nums))
    print(nums)
    # 检查头尾相同个数，计算最大间隔对数
    if nums[0]==nums[-1]:
        min_count = n*(n-1)//2
        print("{} {}".format(min_count,min_count))
        return
    pre, same_pre = nums[0],1
    for i in range(1,n):
        if nums[i] == pre:
            same_pre += 1
        else:
            break
    end, same_end = nums[n-1],1
    for i in range(2,n):
        if nums[n-i] == end:
            same_end += 1
        else:
            break
    max_count = same_pre*same_end
    # 统计相邻间隔，计算最小间隔对数
    min_count = 0
    pre = nums[0]
    dic = {}  # 统计
    min_key = float('inf')
    for num in nums[1:]:
        if min_key == 0:
            break
        a = num - pre
        pre = num
        if a > min_key:
            continue
        if a < min_key:
            min_key = a
            dic.setdefault(min_key,0)
        dic[min_key] += 1
    # 最小间隔=0的情况
    if min_key == 0:
        i = 1
        while i < n:
            start = i-1
            while i<n and nums[i-1]==nums[i]:
                i += 1
            m = i-start
            if m>1:
                min_count += m*(m-1)//2
            i+=1
    if min_key !=0:
        min_count = dic[min_key]
    print(dic)
    print("{} {}".format(min_count,max_count))
    return


# n = int(sys.stdin.readline())
# line = sys.stdin.readline()
# nums = list(map(int,line.strip().split()))
# func(nums)


if __name__ == '__main__':
    while True:
        num = sys.stdin.readline().strip()
        if not num:
            break
        n = int(num)
        line = sys.stdin.readline().strip()
        if not line:
            break   # 这一步不能少，否则退出时会报错
        strlst = line.split(' ')
        nums = list(map(int,strlst))
        func(nums[:n])
