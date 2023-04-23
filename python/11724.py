import sys
from collections import deque


N, M = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N + 1)]
visited = [False for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

result = 0


def BFS(x):
    deq = deque()
    deq.append(x)
    visited[x] = True
    while deq:
        x = deq.popleft()
        for y in graph[x]:
            if not visited[y]:
                deq.append(y)
                visited[y] = True


for i in range(1, N + 1):
    if visited[i] == False:
        BFS(i)
        result += 1


print(result)
