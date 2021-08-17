"""
有若干个6点环，每个结点有一个数字，顺时针描述每个结点
判断给出的环是否有相同的

输入：
T个测试用例
n个环
环1
环2
...
环n

输出：
"YES"存在相同环
"NO"不存在相同环

例如：
输入：
2
3
1 2 3 4 5 6
2 3 4 5 6 1
2 4 3 5 1 7
2
1 2 3 4 5 6
4 5 6 2 3 1

输出：
YES
NO

"""


def func(n, a):
    ans = set()
    for aa in a:
        aa.sort()
        aa = "".join(str(aa))
        ans.add(aa)
    if len(ans) < n:
        return "YES"
    else:
        return "NO"


t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = []
    for i in range(n):
        nums = list(map(int, input().strip().split()))
        a.append(nums)
    print(func(n, a))
