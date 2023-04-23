import sys

N, M = map(int,sys.stdin.readline().split())

#S = set(map(str,sys.stdin.readline().rstrip()))
S = set()

for i in range(N):
    S.add(sys.stdin.readline().rstrip())

count = 0

for i in range(M):
    str = sys.stdin.readline().rstrip()
    if str in S:
        count += 1
        
print(count)
