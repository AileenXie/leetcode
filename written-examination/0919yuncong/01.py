a = input().strip()
b = input().strip()


def func(a, b):
    if a == b:
        return 0
    diff = []
    for i in range(len(a)):
        if a[i] != b[i]:
            diff.append(i)
    double = 0
    for index,i in enumerate(diff):
        for j in diff[index + 1:]:
            print(i,j)
            find = False
            if a[i] == b[j] and a[j] == b[i]:
                double += 1
                find = True
            if find:
                print("____")
                break
    c = len(diff)
    if double:
        c-=2*double
        return c-1+double if c else double
    return c-1

print(func(a, b))

"""
aaaabbbbcccc
abbcaaccacbb
5

abc
cba
1

abc
abc
0
"""