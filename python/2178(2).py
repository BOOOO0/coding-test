import sys
from collections import deque


def BFS(x, y):
    deq = deque()
    deq.append((x, y))

    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue
            else:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[x][y] + 1
                    deq.append((nx, ny))
    return graph[N - 1][M - 1]


N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(BFS(0, 0))
