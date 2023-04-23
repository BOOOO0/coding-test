import sys
from collections import deque


def BFS(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    deq = deque()
    deq.append((x, y))
    graph[x][y] = 0
    while deq:
        x, y = deq.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= H or ny < 0 or ny >= W:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                deq.append((nx, ny))


answer = []
while True:
    result = 0
    W, H = map(int, sys.stdin.readline().split())

    if W == 0 and H == 0:
        break

    graph = [list(map(int, sys.stdin.readline().split())) for _ in range(H)]
    for i in range(H):
        for j in range(W):
            if graph[i][j] == 1:
                BFS(i, j)
                result += 1
    answer.append(result)

for a in answer:
    print(a)
