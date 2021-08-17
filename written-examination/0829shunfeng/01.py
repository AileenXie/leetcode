"""
长度为n的数组nums，其中-1表示不确定数，
给所有不确定数赋值后，使得数组中等比数列个数最少
输出最少的等比数列个数

输入：第一行n，第二行nums

例：
输入：
3
-1 -1 -1
3
-1 -1 1
3
1 -1 2
7
-1 -1 -1 4 5 1 2

输出：
1，1，2，2

"""

def func(n, nums):
    if n < 3: return 1
    count = 1
    interval=None
    pre,index=None,None
    i=0
    while i<n:
        if not pre:  # 开头是-1
            if nums[i] == -1:
                i += 1
                continue
            pre=nums[i]  # 记录开头
            index=i
        else:  # 已有开头
            if not interval:  # 还没间隔
                if nums[i] == -1:
                    i += 1
                    continue
                if (nums[i]-pre)%(i-index)==0:  # 计算间隔
                    interval=(nums[i]-pre)//(i-index)
                    pre=nums[i]
                    index=i
                else:  # 必定分为2个间隔
                    count+=1
            else:  # 已有间隔
                if nums[i]==-1:
                    pre+=interval
                    index=i
                else:
                    if nums[i]!=pre+interval:  # 新的开头
                        count+=1
                        pre=nums[i]
                        index=i
                        interval=None
        i+=1
    return count



try:
    while True:
        n = int(input().strip())
        nums = list(map(int, input().strip().split()))
        print(func(n, nums))
except:
    pass

# import sys
# while True:
#     line = sys.stdin.readline()
#     print("----",line)
#     n = int(line.strip())
#     nums = list(map(int, input().strip().split()))
#     # n,nums=7,[-1, -1, -1, 4 ,5, 1, 2]
#     print(func(n,nums))


# import sys
# i=1
# for line in sys.stdin:
#     if i%2:
#         n=int(line.strip())
#     else:
#         nums = list(map(int, line.strip().split()))
#         print(func(n, nums))
#     i+=1