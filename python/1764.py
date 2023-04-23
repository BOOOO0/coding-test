import sys

N , M = map(int,sys.stdin.readline().split())

Dd = set()
Bo = set()

for i in range(N):
    Dd.add(sys.stdin.readline().rstrip())

for i in range(M):
    Bo.add(sys.stdin.readline().rstrip())
    
answer = sorted(list(Dd & Bo))

print(len(answer))

for i in answer:
    print(i)