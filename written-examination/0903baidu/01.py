n, m, k = map(int, input().strip().split())
goods = []
for _ in range(n):
    p, w, v = map(int, input().strip().split())
    goods.append((p, w, v))


def func(n, m, k, goods):
    if not goods: return 0
    goods.sort(key=lambda x:(-x[2],x[0],x[1]))
    # print(goods)
    cur,price = 0,0
    i=0
    count = 0
    # while cur<=m and price<=k and i<n:
    #     cur += goods[i][1]
    #     price += goods[i][0]
    #     i+=1
    # return i-1
    while i<n:
        while cur <= m and price <= k and i < n:
            cur += goods[i][1]
            price += goods[i][0]
            i += 1
            count +=1
        if i<n:
            cur -= goods[i-1][1]
            price -= goods[i-1][0]
            count -= 1
    return count

print(func(n,m,k,goods))

"""
4 10 1000
100 5 3
50 3 2
100 1 1
300 3 3
"""