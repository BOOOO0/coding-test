import sys
from collections import deque


N, K = map(int, sys.stdin.readline().split())

max = 100000
visited = [0] * (max + 1)

deq = deque()
deq.append(N)

while deq:
    x = deq.popleft()
    if x == K:
        print(visited[x])
        break
    for nx in (x - 1, x + 1, x * 2):
        if 0 <= nx <= max and not visited[nx]:
            visited[nx] = visited[x] + 1
            deq.append(nx)
