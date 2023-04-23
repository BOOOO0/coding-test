import sys
from collections import deque


# def DFS(x, y):
#     dx = [0, 0, -1, 1]
#     dy = [1, -1, 0, 0]

#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if x >= 0 and x < N and y > 0 and y < M:
#             if graph[x][y] == 1:
#                 graph[x][y] = 0
#                 DFS(nx, ny)


def BFS(x, y):
    deq = deque()
    deq.append((x, y))
    graph[x][y] = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                deq.append((nx, ny))


answer = []

T = int(sys.stdin.readline().rstrip())

for _ in range(T):
    N, M, K = map(int, sys.stdin.readline().split())

    graph = [[0 for _ in range(M)] for _ in range(N)]

    for _ in range(K):
        v1, v2 = map(int, sys.stdin.readline().split())
        graph[v1][v2] = 1

    result = 0

    for i in range(N):
        for j in range(M):
            if graph[i][j] == 1:
                BFS(i, j)
                result += 1
    answer.append(result)
for a in answer:
    print(a)
