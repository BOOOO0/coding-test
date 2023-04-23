import sys

N , K = map(int, sys.stdin.readline().split())

coins = []

for _ in range(N):
    coins.append(int(sys.stdin.readline().rstrip()))

cnt = 0

for i in reversed(range(N)):
    cnt += K//coins[i]
    K = K % coins[i]
    
print(cnt)