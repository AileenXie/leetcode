"""
给定一个字符串"aasREdsrDS"

输出最小修改次数
"""
s=input().strip()

n=len(s)
up,low=0,0
for i in range(n):
    if s[i].isupper(): up+=1
    if s[i].islower(): low+=1
# print(up,low)
print(max(up,low)-n//2)