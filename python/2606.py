import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())

M = int(sys.stdin.readline().rstrip())


graph = [[] for _ in range(N + 1)]


for _ in range(M):
    v1, v2 = map(int, sys.stdin.readline().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


cnt = 0

visited = [False for _ in range(N + 1)]

deq = deque()

# 1번 노드에서 출발한다
deq.append(1)

while deq:
    x = deq.popleft()
    visited[x] = True
    for y in graph[x]:
        if visited[y] == False:
            deq.append(y)
            visited[y] = True
            cnt += 1
print(cnt)

# d_check = [ False for _ in range(N+1)]

# stk = []

# stk.append(1)

# while stk:
#     x = stk.pop()
#     d_check[x] = True

#     for y in edge[x]:
#         if d_check[y] == False:
#             stk.append(y)
# 이게 더 빠른듯?
# print(d_check.count(True)-1)
