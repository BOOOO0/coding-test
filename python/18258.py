import sys
from collections import deque


N = int(sys.stdin.readline().rstrip())

deq = deque()

for i in range(N):
    deq.append(i+1)

while len(deq) > 1 :
    deq.popleft()   
    deq.rotate(-1)

print(deq[0])


