"""
大鱼吃小鱼，每轮大鱼可吃右数第一小的鱼，同步进行。问几轮下来不会再有鱼被吃

————————————————————
输入： n条鱼，每条鱼体积
8
7 6 4 6 5 1 3 9

输出： 轮数
2

解释：
第一轮：7，6，9
第二轮：7，9
————————————————————
输入：
6
4 3 2 3 2 1

输出：
2

解释：
第一轮：4，3
第二轮：4
————————————————————
输入：
3
1 4 7

输出：
0
"""

n = int(input().strip())
fish = list(map(int, input().strip().split()))


def func(n, fish):
    if not n: return 0
    def judge(rest):  # 判断是否不会再变了
        m=len(rest)
        for i in range(1,m):
            if fish[rest[i]]<fish[rest[i-1]]:
                return False
        return True

    if judge(list(range(n))): return 0
    step=1
    i=0
    rest=list(range(len(fish)))
    while True:
        cur_rest = [i]  # 本轮本次会被留下
        new_rest = []
        visited = set()
        while cur_rest:
            ii=cur_rest.pop(0)
            new_rest.append(ii)  # 本轮最终剩下的
            cur_min = fish[rest[ii]]
            for j in range(ii+1,len(rest)):
                if j in visited: continue
                if fish[rest[j]]>=cur_min:
                    if j not in cur_rest:
                        cur_rest.append(j)
                else:  # 被吃
                    cur_min=fish[rest[j]]
                    visited.add(j)
                    if j in cur_rest:
                        cur_rest.remove(j)
        rest = new_rest
        if judge(rest): break
        else:
            step+=1
            i=0

    return step

print(func(n,fish))
