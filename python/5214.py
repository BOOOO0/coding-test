import sys
from collections import deque


N, M, K = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(K):
    v1, v2, v3 = map(int, sys.stdin.readline().split())


deq = deque()
deq.append(1)

visited = [False for _ in range(N + 1)]
cnt = 0

while deq:
    x = deq.popleft()
