import sys

sick = input().split("-")
num = []


for s in sick:
    cnt = 0
    add = s.split("+")
    for a in add:
        cnt += int(a)
    num.append(cnt)


n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)
