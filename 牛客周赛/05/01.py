class Solution:
    def solve(self, x):
        # write code here
        base = 0

        while base<100000:
            num = 100000 * base + x
            # print(num)
            if self.sqrt(num):
                return True
            else:
                base += 1
        return False

    def sqrt(self,num):
        if num == 0 or num == 2: return False
        if num == 1: return True
        pre = num
        half = num // 2
        while pre != half:
            if half * half > num:
                pre = half
                half //= 2
            elif half * half == num:
                return True
            else:
                tmp = half
                half = (half + pre) // 2
                pre = tmp
        return False


if __name__ == "__main__":
    print(Solution().solve(99))
    # print(Solution().sqrt(10324))