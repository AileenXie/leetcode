"""
对数据移位
每个数据的二进制表达奇偶位对调
整个数向右移动两位，多出的数放到下一个数的开头。最后的2位放置第一个数的开头

1 2

1073741824 2147483648
"""

nums = list(map(int,input().strip().split()))

def func(nums):
    even_mask=0xAAAAAAAA  # 1010*8  32位
    odd_mask=0x55555555  # 0101*8  32位
    new_num=[]
    ans =[]
    for num in nums:
        tmp1=(num&even_mask)>>1  # 偶数位
        tmp2=(num&odd_mask)<<1  # 奇数位
        cur=tmp1|tmp2  # 对调
        new_num.append(cur)
    pre_mask=new_num[0]&3  # 末尾2位
    pre=new_num[0]>>2  # 右移2位，记录第一个数
    for i in range(1,len(new_num)):
        tmp=new_num[i]&3  # 新的数末尾2位
        cur=(new_num[i]>>2)|(pre_mask<<30)  # 拼接成新的数
        ans.append(cur)
        pre_mask=tmp
    cur=pre|(pre_mask<<30)  # 最后一个数末尾2位拼接到第一个数前面
    ans=[cur]+ans  # 添加第一个数
    result = ""
    for i in ans:
        result+=" "+str(i)
    return result[1:]

print(func(nums))



