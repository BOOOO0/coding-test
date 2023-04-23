import sys
from collections import deque


def BFS(x, y):

    deq = deque()
    deq.append((x, y))
    graph[x][y] = 0
    cnt = 1
    while deq:
        x, y = deq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= N or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                deq.append((nx, ny))
                cnt += 1
    return cnt


N = int(sys.stdin.readline().rstrip())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

apart = []


result = 0

for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            apart.append(BFS(i, j))
apart.sort()
print(len(apart))
for a in apart:
    print(a)
