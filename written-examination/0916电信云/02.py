import collections

s = input().strip()
min_c = set()
min_count=float('inf')
count = collections.Counter(s)
for key in count:
    if count[key]<min_count:
        min_count=count[key]
        min_c=set()
        min_c.add(key)
    elif count[key]==min_count:
        min_c.add(key)
ans = ""
for a in s:
    if a not in min_c:
        ans+=a
print(ans)
