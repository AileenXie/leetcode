# nums = list(map(int, input().strip().split(',')))

def func(nums):
    nums.sort()
    i = 0
    zero_count = 0
    while i < len(nums) and nums[i] == 0:
        zero_count += 1
        i += 1
    if i >= len(nums):
        return "So Luchy!"
    for j in range(i+1,len(nums)):
        gap = nums[j] - nums[j-1] - 1
        zero_count -= gap  # 填补
        if zero_count < 0:
            return "Oh My God!"
    return "So Luchy!"

nums=[0,1,3,4,5]
nums=[0,0,0,0,2]
# nums=[3,4,5,7,8]
# nums=[3,2,1,5,4]
print(func(nums))