import sys

N = int(sys.stdin.readline().rstrip())
cnt = 0
arr = [500, 100, 50, 10]

for coin in arr:
    cnt += N // coin
    N %= coin

print(cnt)
