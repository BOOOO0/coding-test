import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


visited = [0 for _ in range(N + 1)]

deq = deque()

# 루트 노드를 1로
deq.append(1)


while deq:
    x = deq.popleft()
    for y in graph[x]:
        if visited[y] == 0:
            visited[y] = x
            deq.append(y)

for v in visited[2:]:
    print(v)


# for e in edge:
#     e.sort()

# deq = deque()
# deq.append(1)

# b_check = [0 for _ in range(N+1)]

# def BFS():
#     while deq:
#         x = deq.popleft()

#         for y in edge[x]:
#             if b_check[y] == 0:
#                 b_check[y] = x
#                 deq.append(y)

# BFS()
# answer = b_check[2:]

# for a in answer:
#     print(a)
