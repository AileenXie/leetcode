class Solution:
    def solve(self, n, a):
        # write code here
        """
        尽可能买多个，同样多个里选余量能买最大的数
        """
        price = []
        max_count = 0  # 单件最多购买数量
        available = []  # 备选单件
        for i, p in enumerate(a):
            cur_count = n // p
            if cur_count > max_count:
                available = [(p, i+1)]  # 价格、数字
                max_count=cur_count
            elif cur_count == max_count:
                available.append((p, i+1))
            price.append((p, i+1))
        print(max_count,available)
        if max_count == 0: return "-1"
        if len(available) == 1: return str(available[0][1]) * max_count
        print("case 3")
        price.sort(key=lambda x: (x[0], -x[1]))  # 价格升序，数字降序
        print(price)
        max_num = 0
        base_num = 0
        for p, num in available:
            res = n % p + p
            j = len(available)
            cur_max = num  # 自己
            while price[j][0] <= res:
                if price[j][1]>cur_max:
                    cur_max=price[j][1]
                j += 1
            if cur_max > max_num or (cur_max == max_num and num > base_num):
                max_num = cur_max
                base_num = num
        print(max_num,base_num)
        return str(max_num) + str(base_num) * (max_count - 1)

if __name__ == "__main__":
    # n,a=5,[5,4,3,2,1,2,3,4,5]
    # n,a=2,[9,11,1,12,5,8,9,10,6]
    # n,a=5,[2,2,2,2,3,3,5,6,7]
    # n,a=5,[2,2,2,2,3,4,5,3,5]
    n,a=11,[3,3,3,4,5,2,5,3,6]
    print(Solution().solve(n,a))