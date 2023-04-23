import sys
from collections import deque

# 상하좌우 모든 1에 출발점부터 해당 노드까지의 거리를 갖게한다
# 각각의 1이 모든 거리값을 다 가지게 되면서 함수가 종료되는데
# 우리가 원하는 것은 오른쪽 최하단 마지막 노드까지의 최단경로이기 때문에
# 마지막 노드의 값을 출력하면 된다.


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
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                deq.append((nx, ny))
    return graph[N - 1][M - 1]


N, M = map(int, sys.stdin.readline().split())

graph = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(BFS(0, 0))
