import sys

n = int(input())
level = 1
num = 1
while num < n :
    num += level * 6
    level += 1
print(level)
# 1 7 19 37 61 