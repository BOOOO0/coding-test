import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

result = -1
deq = deque()
deq.append((A, 1))
while deq:
    A, cnt = deq.popleft()
    if A == B:
        result = cnt
        break
    if A * 2 <= B:
        deq.append((A * 2, cnt + 1))
    if (A * 10) + 1 <= B:
        deq.append((A * 10 + 1, cnt + 1))

print(result)
